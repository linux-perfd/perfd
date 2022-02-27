#!/usr/bin/python3
from heapq import merge
from multiprocessing.spawn import prepare
import os
import tempfile
import subprocess
import db
'''
temp_perf_file = tempfile.NamedTemporaryFile(delete=False)
# temp_perf_file.name

os.system("perf record -e cycles:u -j any,u -a -o  " +
          temp_perf_file.name + "  -- sleep 10")
batcmd = "perf script -F ip,dso -f -i " + temp_perf_file.name

result = subprocess.check_output(batcmd, shell=True, text=True)
lines = result.splitlines()
samples_per_obj_file = dict()

for line in lines:
    cols = line.split()
    name_parens = cols[1]
    name = name_parens[1:-1]

    if name in samples_per_obj_file:
        samples_per_obj_file[name] += 1
    else:
        samples_per_obj_file[name] = 1
'''
samples_per_obj_file = dict() # i'll have to delete this line when i fimish the step 4
database = db.Database()
database.table = 'database'
for name in samples_per_obj_file:
    database.write(
        perf_name=temp_perf_file.name,
        name_obj_file=name,
        amount_of_samples=samples_per_obj_file[name])

database.commit()
print(database.read())

def pepare_fdata(objfile):
    fdata_files = []
    records = database.read(name_obj_file = objfile)
    for record in records:
        fdata_file = tempfile.NamedTemporaryFile(delete=False)
        perf_name = record[0]
        os.system(f"perf2bolt {objfile} -p {perf_name} -o {fdata_file.name}")
        fdata_files.append(fdata_file.name) 
    merge_fdata = tempfile.NamedTemporaryFile(delete=False)
    os.system(f"merge-fdata {' '.join(fdata_files)} > {merge_fdata.name}")
    return merge_fdata.name


objfile = '/usr/lib/x86_64-linux-gnu/libresolv-2.31.so'
pepare_fdata(objfile)
tempfile.NamedTemporaryFile(delete=True)