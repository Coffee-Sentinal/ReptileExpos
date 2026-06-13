#!/usr/bin/env python3
import subprocess, sys
print('Static seed data already lives in public/data. Running validation.')
subprocess.check_call([sys.executable,'scripts/validate_data.py'])
