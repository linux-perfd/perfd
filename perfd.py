#!/usr/bin/python3
import os
#os.system("perf record -e cycles:u -j any,u -a -o perf.data -- sleep 10")
import subprocess
batcmd="perf script -F ip,dso -f -i perf.data"
result = subprocess.check_output(batcmd, shell=True, text =True)
lines= result.splitlines()
samples_per_obj_file = dict()

for line in lines:
    cols = line.split()
    name_parens = cols[1]
    name = name_parens[1:-1] 

    if name in samples_per_obj_file:
        samples_per_obj_file[name] += 1
    else:
        samples_per_obj_file[name] = 0
for name in samples_per_obj_file:      
    print(name, samples_per_obj_file[name])

import tempfile




from sql30 import db
name_perf_file = NamedTemporaryFile(delete=False)
name_perf_file.name 
name_perf_file.read()

class Perfd(db.Model):
    TABLE = 'reviews'
    PKEY = 'rid'
    DB_SCHEMA = {
        'db_name': './perfd.dp',
        'tables': [
            {
                'name': TABLE,
                'fields': {
                    'perf_name': 'text',
                    'name_obj_file': 'text',
                    'amount_of_samples': 'int'
                },
            'primary_key': PKEY
            }
        ]
    }
    VALIDATE_WRITE = True