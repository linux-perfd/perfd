#!/usr/bin/python3
import os
import tempfile
import subprocess
import db

temp_perf_file = tempfile.NamedTemporaryFile(delete=False, dir='.')
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

def prepare_fdata(objfile):
    fdata_files = []
    records = database.read(name_obj_file = objfile) # find some sampels in the db, which have the same name_obj_file
    for record in records:
        fdata_file = tempfile.mktemp()
        perf_name = record[0] 
        os.system(f"perf2bolt {objfile} -p {perf_name} -o {fdata_file}") # for every single perf files use perf2bolt
        fdata_files.append(fdata_file) # add the fdata files in the list  
    merge_fdata = tempfile.mktemp()
    os.system(f"merge-fdata {' '.join(fdata_files)} > {merge_fdata}") # merge all fdata files that i got 
    for fdata_file in fdata_files: 
        os.remove(fdata_file) # delete the mid-term fdata files and save only a last one
    return merge_fdata

a = []
b = dict()
def invoke_bolt(objfile, fdata_file):
    outfile = tempfile.mktemp() #create a new name for an optimized file
    os.system(f"llvm-bolt {objfile} -data={fdata_file} -o {outfile} -dyno-stats") #trigger BOLT
    return outfile  #return an optimized file 
 
records = database.read() #the information's from db.py
for _, name_obj_file, number_of_samples in records: #looking for obj_files which are larger or equal 100 samples 
    if name_obj_file in b: #count samples in an every perf_file
        b[name_obj_file] += number_of_samples
    else:
        b[name_obj_file] = number_of_samples 
for name_obj_file in b:
    if b[name_obj_file] >= 100: #find obj_files which are more or equel 100 samples
        if name_obj_file.split('.')[-1] != 'map' and name_obj_file[0] == "/": #skipping lines on certain conditions 
            a.append(name_obj_file) # add it to the list
new_list = sorted(a, key=lambda name: b[name], reverse=True) #sort object files by the numbers of samples in decreasing order
 
M = 2 
for objfile in new_list[:M]: #for every new objfile 
    fdata_file = prepare_fdata(objfile) #prepare a profile 
    outfile = invoke_bolt(objfile, fdata_file) #trigger BOLT
    os.remove(fdata_file)
    os.remove(outfile)