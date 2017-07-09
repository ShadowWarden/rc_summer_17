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

def column(matrix,i):
	return [row[i] for row in matrix]

if(len(sys.argv) < 3):
	print("Usage: python script.py <startdate> <enddate>")
	sys.exit(0)

start = str(sys.argv[1])
end = str(sys.argv[2])

os.system("sacct -P -n -T -a --start=%s --end=%s --format=jobid,submit,start,end,alloccpus,account | grep -v '[0-9]\.' > /tmp/calc_time_dump.txt" % (start,end))

ins = open("/tmp/calc_time_dump.txt", "r")
# Get rid of trailing \n
ins = [line.rstrip() for line in ins.readlines()]
data = []

# Seperate by |
for line in ins:
    number_strings = line.split('|') # Split the line on runs of whitespace
    data.append(number_strings)

# Pull out unique users and define a list of zeros where the SU consumed by each user will be
# stored
users = set(column(data,5))
SU_users = [0 for i in users]

# Data should now have the Slurm output in lists further subdivided. Therefore, the start time is
# in position 3 and the end time at position 4. Thus,

# Calculating SU

deltaWaitT = []

SU = []
for i in range(len(data)):
	# Pull out date/Time for submit (d1), start (d2) and end (d3)
	d1 = datetime.strptime(data[i][1], "%Y-%m-%dT%H:%M:%S")
	d2 = datetime.strptime(data[i][2], "%Y-%m-%dT%H:%M:%S")
	d3 = datetime.strptime(data[i][3], "%Y-%m-%dT%H:%M:%S")
	# Compute runtime for job in integer seconds
	deltaT = (d3-d2).total_seconds()

	# Search through users and find the index to write to in SU_users
	flag = 0
	for j in users:
		if(j == data[i][5]):
			break
		flag += 1

	# Throw away negative runtimes (Why do these exist, anyway?)
	if(deltaT >= 0):
		# Create an SU entry for job 'i'
		SU.append(deltaT*int(data[i][4])/3600.0)
		# Add into SU_users for user 'flag'
		SU_users[flag] += deltaT*int(data[i][4])/3600.0
		# Compute waittime for job in int seconds
		deltaWaitT.append((d2-d1).total_seconds()/3600.0)


print "There were %d jobs consuming a total of %f compute hours\n" % (len(data), np.sum(SU)) 
print "The average wait time was %f hours and the median was %f hours\n\n" % (np.mean(deltaWaitT),np.median(deltaWaitT))
print "Consumption by account: \n"
flag = 0
for i in users:
	print "%s : %f" % (i,SU_users[flag])
	flag += 1

# Cleanup
os.system("rm /tmp/calc_time_dump.txt")
