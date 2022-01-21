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
    perf_file = database.read(name_obj_file=objfile)
    print(perf_file)

perf2bolt = "/path/to/perf2bolt objfile -p perf_file -o perf_file.fdata"
merge_fdata = "/path/to/merge-fdata perf_file1.fdata perf_file2.fdata perf_file > tmp_fdata" 

temp_fdata = tempfile.NamedTemporaryFile(delete=False)
# temp_fdata.name

tmp_fdata = "perf script -F ip,dso -f -i " + temp_fdata.name
print(tmp_fdata)

def prepare_fdata(tmp_fdata):
    return tmp_fdata 

tmp_fdata.commit()
print(tmp_fdata.commit())