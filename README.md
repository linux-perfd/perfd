# perfd
Linux daemon for automatic profile collection and post-link binary optimization


import os
import stdout
results_of_one = os.system('perf.record')
print("perf.record run with exit code" % results_of_one)
results_of_two = os.system('perf.repot')
print("perf.report run with exit code" % results_of_two)
stdout.copy('perf.report') 
