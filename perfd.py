#!/usr/bin/python3
import os
#os.system("perf record -e cycles:u -j any,u -a -o name_perf_file.name -- sleep 10")
import subprocess
batcmd ="perf script -F ip,dso -f -i name_perf_file.name"
result = subprocess.check_output(batcmd, shell=True, text =True)
lines = result.splitlines()
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
    print(samples_per_obj_file[name], name)

import tempfile
name_perf_file = tempfile.TemporaryFile()
name_perf_file.name 
name_perf_file.read()


#from db import perfd ( I haven't understood this line in the comment yet) 
from sql30 import db
class Perfd(db.Model):
    TABLE = 'perfd_database'
    DB_SCHEMA = {
        'db_name': './perfd.db',
        'tables': [
            {
                'name': TABLE,
                'fields': {
                    'perf_name': 'text',
                    'name_obj_file': 'text',
                    'amount_of_samples': 'int'
                },
            }
        ]
    }
    VALIDATE_WRITE = True
import os 
import perfd  
db.tbl = ' perfd_database '
db = perfd.Perfd()
db.write(perf_name = ' ', name_obj_file = ' ', amount_of_samples = )  #Tried to call up the information like this it's not correct though   
db.read() 