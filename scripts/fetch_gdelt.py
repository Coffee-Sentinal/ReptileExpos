#!/usr/bin/env python3
"""Optional public GDELT search summary placeholder. No API keys; safe failure."""
import json, urllib.parse, urllib.request
from pathlib import Path
query='("reptile expo" OR "wildlife seizure" OR "reptile smuggling" OR CITES reptile)'
url='https://api.gdeltproject.org/api/v2/doc/doc?'+urllib.parse.urlencode({'query':query,'mode':'artlist','format':'json','maxrecords':25})
Path('data/raw').mkdir(parents=True,exist_ok=True)
try:
    data=json.loads(urllib.request.urlopen(url,timeout=30).read())
    Path('data/raw/gdelt_results.json').write_text(json.dumps(data,indent=2))
    print('wrote data/raw/gdelt_results.json; analyst review required before merging into public evidence')
except Exception as exc: print(f'GDELT optional fetch failed safely: {exc}')
