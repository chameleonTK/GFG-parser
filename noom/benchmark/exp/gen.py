s="1"
for i in range(5000):
	s+="+1"
	f= open("exp"+str(i)+".in","w")
	f.write(s)
	f.close()
