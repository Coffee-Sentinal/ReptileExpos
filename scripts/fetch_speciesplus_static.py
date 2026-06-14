#!/usr/bin/env python3
import os, shutil
from pathlib import Path
if not os.getenv('SPECIESPLUS_TOKEN'):
    shutil.copyfile('public/data/taxa.json','data/processed/taxa.json'); print('No Species+ token; using local seed taxa data.')
else: print('Species+ enrichment placeholder: token present but static MVP does not require API access.')
