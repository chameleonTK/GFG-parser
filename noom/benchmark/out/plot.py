from matplotlib import pyplot as plt
import numpy as np

f = open("earley.out",'r')

perf = {}
isLabel = True
algor = []
noline = 1
for line in f:
	line = line.strip()
	sp = line.split(":")
	if noline < 5:
		noline+=1
		continue

	if isLabel:
		for s in sp:
			perf[s] = []
		algor = sp
		isLabel=False
		print sp
	else:
		for i in range(len(sp)):
			perf[algor[i]].append( sp[i])

f.close()


x = range(len(perf[algor[0]]))

with plt.style.context('fivethirtyeight'):
    for k in algor:
    	if k=="":
    		continue
    	plt.plot(x, perf[k],label=k.strip())
	
    legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')

    legend.get_frame()

plt.title('Benchmark with expression grammar')
plt.ylabel('Execution Time')

plt.show()
