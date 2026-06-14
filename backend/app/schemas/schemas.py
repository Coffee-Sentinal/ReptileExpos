from datetime import date
from pydantic import BaseModel, ConfigDict
class VenueOut(BaseModel):
    model_config=ConfigDict(from_attributes=True); id:str; name:str; city:str; country:str; latitude:float; longitude:float
class EventDateOut(BaseModel):
    model_config=ConfigDict(from_attributes=True); start_date:date; end_date:date; label:str
class WebsiteOut(BaseModel):
    model_config=ConfigDict(from_attributes=True); id:str; name:str; url:str; type:str; notes:str; confidence:str; last_checked_date:date|None=None
class EventWebsiteOut(BaseModel):
    model_config=ConfigDict(from_attributes=True); website:WebsiteOut
class TaxonOut(BaseModel):
    model_config=ConfigDict(from_attributes=True); id:str; scientific_name:str; common_name:str; taxon_group:str; cites_appendix:str; eu_annex:str; native_range_countries:list; origin_countries:list; transit_countries:list; id_notes:str
class EventTaxonOut(BaseModel):
    model_config=ConfigDict(from_attributes=True); taxon:TaxonOut; reason_for_inclusion:str; evidence_basis:str; confidence:str
class RouteRiskOut(BaseModel):
    model_config=ConfigDict(from_attributes=True); id:str; direction:str; origin:str; destination:str; transit_hubs:list; window_start:date; window_end:date; rationale:str; confidence:str
class EvidenceOut(BaseModel):
    model_config=ConfigDict(from_attributes=True); id:str; title:str; evidence_type:str; url:str; date_observed:date; date_posted:date|None=None; event_id:str|None=None; related_taxa:list; related_actor:str|None=None; summary:str; extracted_red_flags:list; screenshot_path:str|None=None; content_hash:str|None=None; analyst_notes:str; confidence:str
class RiskScoreOut(BaseModel):
    model_config=ConfigDict(from_attributes=True); species_risk:int; online_signal_risk:int; route_risk:int; paperwork_risk:int; courier_export_risk:int; overall_score:int; priority:str; confidence:str; explanation:dict
class EventOut(BaseModel):
    model_config=ConfigDict(from_attributes=True); id:str; name:str; slug:str; description:str; status:str; confidence:str; venue:VenueOut; dates:list[EventDateOut]=[]; websites:list[EventWebsiteOut]=[]; taxa:list[EventTaxonOut]=[]; evidence:list[EvidenceOut]=[]; routes:list[RouteRiskOut]=[]; risk_score:RiskScoreOut|None=None
class EventCreate(BaseModel):
    name:str; slug:str; description:str; venue_id:str; confidence:str="unknown"
class EvidenceCreate(BaseModel):
    title:str; evidence_type:str; url:str=""; date_observed:date; event_id:str|None=None; summary:str; extracted_red_flags:list=[]; analyst_notes:str=""; confidence:str="unknown"
