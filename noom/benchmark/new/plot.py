from matplotlib import pyplot as plt
import numpy as np
import sys

print ">> input file : ",sys.argv[1]
f = open(sys.argv[1],'r')


perf = {"Keshav":[],"Earley":[],"CYK":[]}
isLabel = True
algor = ["Keshav","Earley","CYK"]
noline = 1
for line in f:
	if noline < 9:
		noline+=1
		continue

	line = line.strip()
	sp = line.split(":")
	for i in range(len(sp)-1):
		perf[algor[i]].append( sp[i])
	
f.close()


x = range(len(perf[algor[0]]))
if len(perf["CYK"]) == 0:
	algor.pop(2)

with plt.style.context('fivethirtyeight'):
    for k in algor:
    	if k=="":
    		continue
    	plt.plot(x, perf[k],label=k.strip())
	
    legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')

    legend.get_frame()

plt.title('Benchmark with expression grammar')

if "time" in sys.argv[1]:
	plt.ylabel('Execution Time (s)')
else:
	plt.ylabel('Memory usage (kb)')
plt.show()
