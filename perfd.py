#!/usr/bin/python3
import os
#os.system("perf record -e cycles:u -j any,u -a -o perf.data -- sleep 10")  
import subprocess
batcmd="perf script -F ip,dso -f -i perf.data"
result = subprocess.check_output(batcmd, shell=True, text =True)
lines= result.splitlines()
for line in lines:
    print(line)
print(line.split()) 

#print( ", ".join( repr(e) for e in result ) ) #пытался удалить скобки