WEIGHTS = {
    "high_risk_proxy_taxa_present": 25,
    "online_advert_or_handover_signal": 20,
    "courier_import_export_linkage": 15,
    "source_country_route_feasibility": 15,
    "outbound_consumer_route_feasibility": 10,
    "seizure_or_report_history": 10,
    "weak_paperwork_source_claim_indicators": 5,
}
def priority(score:int)->str:
    return "high" if score>=70 else "medium" if score>=45 else "low"
def calculate_event_score(event):
    taxa_count=len(event.taxa); evidence=len(event.evidence); routes=event.routes
    courier=any(w.website.type=="courier/import-export service" for w in event.websites)
    seizure=any(e.evidence_type in ["seizure report","journalist report"] for e in event.evidence)
    factors={
        "high_risk_proxy_taxa_present": min(1, taxa_count/5),
        "online_advert_or_handover_signal": min(1, evidence/3),
        "courier_import_export_linkage": 1 if courier else 0,
        "source_country_route_feasibility": 1 if any(r.direction=="inbound" for r in routes) else 0,
        "outbound_consumer_route_feasibility": 1 if any(r.direction=="outbound" for r in routes) else 0,
        "seizure_or_report_history": 1 if seizure else 0,
        "weak_paperwork_source_claim_indicators": .5 if taxa_count else 0,
    }
    overall=round(sum(WEIGHTS[k]*v for k,v in factors.items()))
    return {"species_risk":round(factors["high_risk_proxy_taxa_present"]*100),"online_signal_risk":round(factors["online_advert_or_handover_signal"]*100),"route_risk":round(max(factors["source_country_route_feasibility"],factors["outbound_consumer_route_feasibility"])*100),"paperwork_risk":round(factors["weak_paperwork_source_claim_indicators"]*100),"courier_export_risk":round(factors["courier_import_export_linkage"]*100),"overall_score":overall,"priority":priority(overall),"confidence":"medium" if evidence>=2 else "low","explanation":{"weights":WEIGHTS,"factor_scores":factors,"caveat":"Deterministic monitoring-priority score; not proof of criminality."}}
