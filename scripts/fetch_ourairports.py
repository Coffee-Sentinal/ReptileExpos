#!/usr/bin/env python3
"""Optional OurAirports fetch. No API key required; app works if this fails."""
import csv, json, urllib.request
from pathlib import Path
url='https://davidmegginson.github.io/ourairports-data/airports.csv'; raw=Path('data/raw/airports.csv'); out=Path('public/data/airports.json')
raw.parent.mkdir(parents=True,exist_ok=True)
try:
    raw.write_bytes(urllib.request.urlopen(url,timeout=30).read())
    rows=[]
    for r in csv.DictReader(raw.open()):
        if r.get('iata_code') and r.get('type') in {'large_airport','medium_airport'}:
            rows.append({'id':'airport-'+r['iata_code'].lower(),'iata':r['iata_code'],'name':r['name'],'city':r.get('municipality') or '', 'country':r.get('iso_country') or '', 'latitude':float(r['latitude_deg']),'longitude':float(r['longitude_deg']),'eventIds':[]})
    out.write_text(json.dumps(rows[:5000],indent=2)); print(f'wrote {out}')
except Exception as exc:
    print(f'OurAirports optional fetch failed safely: {exc}')
