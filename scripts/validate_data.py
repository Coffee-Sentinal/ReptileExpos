#!/usr/bin/env python3
import json, sys
from pathlib import Path
BASE=Path('public/data'); allowed_conf={'unknown','low','medium','high'}; allowed_risk={'low','medium','high','critical'}
def load(n): return json.loads((BASE/n).read_text())
errors=[]
events=load('events.json'); taxa=load('taxa.json'); et=load('event_taxa.json'); web=load('websites.json'); ew=load('event_websites.json'); evd=load('evidence.json'); airports=load('airports.json'); routes=load('route_risks.json')
ids={e['id'] for e in events}; taxa_ids={t['id'] for t in taxa}; web_ids={w['id'] for w in web}; airport_ids={a['id'] for a in airports}
for e in events:
    for f in ['id','name','venue','eventDates','monitoringPriority','confidence']: 
        if f not in e: errors.append(f"event missing {f}: {e.get('id')}")
    if e.get('monitoringPriority') not in allowed_risk: errors.append(f"bad risk {e.get('id')}")
    if e.get('confidence') not in allowed_conf: errors.append(f"bad confidence {e.get('id')}")
for row in et:
    if row['eventId'] not in ids: errors.append(f"event_taxa broken event {row['id']}")
    if row['taxonId'] not in taxa_ids: errors.append(f"event_taxa broken taxon {row['id']}")
for row in ew:
    if row['eventId'] not in ids or row['websiteId'] not in web_ids: errors.append(f"event_websites broken {row['id']}")
for row in evd:
    if row['relatedEventId'] not in ids: errors.append(f"evidence broken event {row['id']}")
    if row['confidence'] not in allowed_conf: errors.append(f"evidence bad confidence {row['id']}")
for row in routes:
    if row['eventId'] not in ids: errors.append(f"route broken event {row['id']}")
    if row['destinationAirportId'] not in airport_ids: errors.append(f"route broken airport {row['id']}")
    if row['confidence'] not in allowed_conf: errors.append(f"route bad confidence {row['id']}")
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f"Validated {len(events)} events, {len(taxa)} taxa, {len(routes)} route-risk corridors, {len(evd)} evidence items.")
