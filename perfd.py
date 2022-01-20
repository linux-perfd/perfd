#!/usr/bin/python3
import os
import tempfile
import subprocess
import db

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

database = db.Database()
database.table = 'database'
for name in samples_per_obj_file:
    database.write(
        perf_name=temp_perf_file.name,
        name_obj_file=name,
        amount_of_samples=samples_per_obj_file[name])

database.commit()
print(database.read())

#step4
def prepare_fdata(objfile):
    database.read(objfile)
    print( database.read(objfile))
    