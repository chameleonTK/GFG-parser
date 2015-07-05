from matplotlib import pyplot as plt
import numpy as np
import sys

print ">> input file : ",sys.argv[1]
f = open(sys.argv[1],'r')


perf = {"GFG":[],"Earley":[],"CYK":[]}
marker = {"GFG":"s","Earley":"o","CYK":"D"}
isLabel = True
algor = ["GFG","Earley","CYK"]
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
    #perf["Earley"][0]=10
    
    for k in algor:
    	if k=="":
    		continue
    	simple = {"x":[],"y":[]}
    	for i in range(0,len(x),2):
    		simple["x"].append(x[i])
    		simple["y"].append(perf[k][i])

    	plt.plot(simple["x"], simple["y"],label=k.strip(),marker=marker[k])
    	#plt.plot(simple["x"], simple["y"])

	
    legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')

    legend.get_frame()

#plt.title('Benchmark with expression grammar')

plt.xlabel('length of input string')
if "time" in sys.argv[1]:
	plt.ylabel('Execution Time (s)')
else:
	plt.ylabel('Memory usage (kb)')

# x1,x2,y1,y2 = plt.axis()
# plt.axis((x1,x2,0,.6))
plt.tight_layout()

plt.show()
