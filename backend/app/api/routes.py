from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select
from app.core.database import get_db
from app.core.auth import current_role, Role
from app.models.models import *
from app.schemas.schemas import *
from app.services.windows import monitoring_windows
from app.services.risk_scoring import calculate_event_score
router=APIRouter(prefix="/api")
def event_query():
    return select(Event).options(selectinload(Event.venue),selectinload(Event.dates),selectinload(Event.websites).selectinload(EventWebsite.website),selectinload(Event.taxa).selectinload(EventTaxon.taxon),selectinload(Event.evidence),selectinload(Event.routes),selectinload(Event.risk_score))
def get_event(db,id):
    ev=db.execute(event_query().where((Event.id==id)|(Event.slug==id))).scalar_one_or_none()
    if not ev: raise HTTPException(404,"Event not found")
    return ev
@router.get("/health")
def health(): return {"status":"ok","service":"ExpoWatch API"}
@router.get("/events", response_model=list[EventOut])
def events(db:Session=Depends(get_db), country:str|None=None, risk_level:str|None=None, confidence:str|None=None):
    data=db.execute(event_query()).scalars().all()
    if country: data=[e for e in data if e.venue.country.lower()==country.lower()]
    if confidence: data=[e for e in data if e.confidence==confidence]
    if risk_level: data=[e for e in data if e.risk_score and e.risk_score.priority==risk_level]
    return data
@router.get("/events/{event_id}", response_model=EventOut)
def event(event_id:str, db:Session=Depends(get_db)): return get_event(db,event_id)
@router.post("/events", response_model=EventOut)
def create_event(payload:EventCreate, db:Session=Depends(get_db), role:Role=Depends(current_role)):
    ev=Event(**payload.model_dump()); db.add(ev); db.add(AuditLog(actor=role, action="create", entity_type="event", entity_id=ev.id, details={"name":ev.name})); db.commit(); return get_event(db, ev.id)
@router.put("/events/{event_id}", response_model=EventOut)
def update_event(event_id:str, payload:EventCreate, db:Session=Depends(get_db), role:Role=Depends(current_role)):
    ev=get_event(db,event_id); [setattr(ev,k,v) for k,v in payload.model_dump().items()]; db.add(AuditLog(actor=role, action="update", entity_type="event", entity_id=ev.id, details={})); db.commit(); return get_event(db,ev.id)
@router.delete("/events/{event_id}")
def delete_event(event_id:str, db:Session=Depends(get_db), role:Role=Depends(current_role)):
    ev=get_event(db,event_id); db.delete(ev); db.add(AuditLog(actor=role, action="delete", entity_type="event", entity_id=event_id, details={})); db.commit(); return {"deleted":event_id}
@router.get("/calendar/upcoming")
def calendar(db:Session=Depends(get_db)):
    evs=db.execute(event_query()).scalars().all(); out=[]
    for e in evs:
        if e.dates:
            d=sorted(e.dates,key=lambda x:x.start_date)[0]; out.append({"event":EventOut.model_validate(e).model_dump(mode="json"),"windows":monitoring_windows(d.start_date,d.end_date)})
    return out
@router.get("/events/{event_id}/monitoring-windows")
def windows(event_id:str, db:Session=Depends(get_db)):
    e=get_event(db,event_id); d=sorted(e.dates,key=lambda x:x.start_date)[0]; return monitoring_windows(d.start_date,d.end_date)
@router.get("/taxa", response_model=list[TaxonOut])
def taxa(db:Session=Depends(get_db)): return db.execute(select(Taxon)).scalars().all()
@router.get("/taxa/{taxon_id}", response_model=TaxonOut)
def taxon(taxon_id:str, db:Session=Depends(get_db)): return db.get(Taxon,taxon_id)
@router.get("/events/{event_id}/taxa", response_model=list[EventTaxonOut])
def event_taxa(event_id:str, db:Session=Depends(get_db)): return get_event(db,event_id).taxa
@router.post("/events/{event_id}/taxa")
def add_event_taxa(event_id:str): return {"status":"MVP relation endpoint pending full form wiring"}
@router.get("/websites", response_model=list[WebsiteOut])
def websites(db:Session=Depends(get_db)): return db.execute(select(Website)).scalars().all()
@router.get("/events/{event_id}/websites", response_model=list[EventWebsiteOut])
def event_websites(event_id:str, db:Session=Depends(get_db)): return get_event(db,event_id).websites
@router.post("/events/{event_id}/websites")
def add_event_website(event_id:str): return {"status":"MVP relation endpoint pending full form wiring"}
@router.get("/evidence", response_model=list[EvidenceOut])
def evidence(db:Session=Depends(get_db)): return db.execute(select(EvidenceItem)).scalars().all()
@router.get("/events/{event_id}/evidence", response_model=list[EvidenceOut])
def event_evidence(event_id:str, db:Session=Depends(get_db)): return get_event(db,event_id).evidence
@router.post("/evidence", response_model=EvidenceOut)
def create_evidence(payload:EvidenceCreate, db:Session=Depends(get_db), role:Role=Depends(current_role)):
    item=EvidenceItem(**payload.model_dump(), related_taxa=[]); db.add(item); db.add(AuditLog(actor=role, action="create", entity_type="evidence", entity_id=item.id, details={"title":item.title})); db.commit(); db.refresh(item); return item
@router.get("/routes", response_model=list[RouteRiskOut])
def routes(db:Session=Depends(get_db)): return db.execute(select(RouteRisk)).scalars().all()
@router.get("/events/{event_id}/routes/{direction}", response_model=list[RouteRiskOut])
def event_routes(event_id:str, direction:str, db:Session=Depends(get_db)): return [r for r in get_event(db,event_id).routes if r.direction==direction]
@router.get("/events/{event_id}/risk-score", response_model=RiskScoreOut)
def risk(event_id:str, db:Session=Depends(get_db)): return get_event(db,event_id).risk_score
@router.post("/events/{event_id}/risk-score/recalculate", response_model=RiskScoreOut)
def recalc(event_id:str, db:Session=Depends(get_db)):
    e=get_event(db,event_id); data=calculate_event_score(e)
    if e.risk_score: [setattr(e.risk_score,k,v) for k,v in data.items()]
    else: db.add(RiskScore(event_id=e.id, **data))
    db.commit(); return get_event(db,event_id).risk_score
@router.get("/events/{event_id}/lead-package/preview")
def lead_preview(event_id:str, db:Session=Depends(get_db)):
    e=get_event(db,event_id); d=e.dates[0]; origins=sorted({c for et in e.taxa for c in et.taxon.origin_countries})
    html=f"<h1>{e.name} lead package</h1><p><strong>Caveat:</strong> This is an intelligence lead package, not proof of criminality.</p><p>Event dates: {d.start_date} to {d.end_date}. Monitoring priority: {e.risk_score.priority if e.risk_score else 'pending'}.</p><h2>Proxy taxa to watch for</h2><ul>{''.join(f'<li>{et.taxon.scientific_name} — {et.reason_for_inclusion}</li>' for et in e.taxa)}</ul><h2>Possible origin countries</h2><p>{', '.join(origins)}</p><h2>Recommended verification</h2><ul><li>Validate permits and source claims through competent authorities.</li><li>Preserve online evidence with date, URL, and analyst notes.</li><li>Coordinate route-risk intersections only with authorized partners.</li></ul>"
    return {"event_id":e.id,"title":f"{e.name} lead package","html":html,"export_status":"MVP export pending"}
@router.post("/events/{event_id}/lead-package/generate")
def generate_lead(event_id:str, db:Session=Depends(get_db)):
    p=lead_preview(event_id,db); lp=LeadPackage(event_id=event_id,title=p["title"],html=p["html"],caveat="This is an intelligence lead package, not proof of criminality."); db.add(lp); db.commit(); return p
@router.get("/lead-packages")
def lead_packages(db:Session=Depends(get_db)): return db.execute(select(LeadPackage)).scalars().all()
