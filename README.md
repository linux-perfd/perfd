# perfd
Linux daemon for automatic profile collection and post-link binary optimization


import os
command = "sudo perf record -e cycles:u -j any,u -a -o perf.data -- sleep 10"
os.system( command ) 
