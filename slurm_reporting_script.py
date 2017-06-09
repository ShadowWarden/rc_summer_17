# Compute time calc
# Omkar H. Ramachandran
# omkar.ramachandran@colorado.edu
#
# To run, type python script.py startdate enddate
# Dates should be in the form yyyy-mm-dd
#

from datetime import datetime
import numpy as np
import os
import sys

if(len(sys.argv) < 3):
	print("Usage: python script.py <startdate> <enddate>")
	sys.exit(0)

start = str(sys.argv[1])
end = str(sys.argv[2])

os.system("sacct -P -n -T -a --start=%s --end=%s --format=jobid,submit,start,end,alloccpus,maxrss,account | grep -v '[0-9]\.' > /tmp/calc_time_dump.txt" % (start,end))

ins = open("/tmp/calc_time_dump.txt", "r")
data = []
for line in ins:
    number_strings = line.split('|') # Split the line on runs of whitespace
    data.append(number_strings)

# Now sort data
data = sorted(data, key=lambda x: x[6])

# Data should now have the Slurm output in lists further subdivided. Therefore, the start time is
# in position 3 and the end time at position 4. Thus,

# Calculating SU

deltaWaitT = []

SU = []
Cons = [] # Consumption by user
for i in range(len(data)):
	d1 = datetime.strptime(data[i][1], "%Y-%m-%dT%H:%M:%S")
	d2 = datetime.strptime(data[i][2], "%Y-%m-%dT%H:%M:%S")
	d3 = datetime.strptime(data[i][3], "%Y-%m-%dT%H:%M:%S")
	deltaT = (d3-d2).total_seconds()
	deltaWaitT.append((d2-d1).total_seconds()/3600.0)
	
	SU.append(deltaT*int(data[i][4])/3600.0)

print "There were %d jobs consuming a total of %f compute hours\n" % (len(data), np.sum(SU)) 
print "The average wait time was %f hours and the median was %f hours" % (np.mean(deltaWaitT),np.median(deltaWaitT))

# Cleanup
os.system("rm /tmp/calc_time_dump.txt")
