#!/usr/bin/python3
import os
#os.system("perf record -e cycles:u -j any,u -a -o perf.data -- sleep 10")  
import subprocess
batcmd="perf script -F ip,dso -f -i perf.data"
result = subprocess.check_output(batcmd, shell=True, text =True)
lines= result.splitlines()
samples_per_obj_file = {}
print(len(samples_per_obj_file))
for line in lines:
    print(line.split()[1] [1:-1] ) 
for i in lines:
    samples_per_obj_file[i] = samples_per_obj_file.get(i , 0) + 1
    print(samples_per_obj_file[i] - 1 , sep = '/n')
