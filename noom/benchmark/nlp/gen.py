s="a cute"
end =" man eat a cute man"
for i in range(100):
	s+=" cute"
	f= open("eng"+str(i)+".in","w")
	f.write(s+end)
	f.close()
