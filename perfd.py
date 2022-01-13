#!/usr/bin/python3
import os
import tempfile

name_perf_file = tempfile.TemporaryFile() 
file = name_perf_file.name

os.system("perf record -e cycles:u -j any,u -a -o file -- sleep 10")
batcmd ="perf script -F ip,dso -f -i file"
import subprocess
result = subprocess.check_output(batcmd, shell=True, text =True)
lines = result.splitlines()
samples_per_obj_file = dict()

for line in lines:
    cols = line.split()
    name_parens = cols[1]
    name = name_parens[1:-1] 
 
    #if name in samples_per_obj_file:
    #    samples_per_obj_file[name] += 1
   # else:
 #       samples_per_obj_file[name] = 0
#for name in samples_per_obj_file:      
    #print(samples_per_obj_file[name], name)

db = Database()
db.tbl = 'database'
db.write(name) 
db.commit() 
db.read() 