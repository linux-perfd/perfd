#!/usr/bin/python3
import os
command = "perf record -e cycles:u -j any,u -a -o perf.data -- sleep 10"
os.system( command ) 