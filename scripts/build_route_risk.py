#!/usr/bin/env python3
import json, subprocess, sys
print('Route-risk corridors are maintained as public-safe static JSON. Re-validating current file...')
subprocess.check_call([sys.executable,'scripts/validate_data.py'])
