class Tritable:
	def __init__(self,n):
		self.n = n
		self.data = [[set() if i <= j else None for j in range(n) ] for i in range(n)]

	def __str__(self):
		s = ""
		for i in range(self.n):
			for j in range(self.n):
				if j+i > self.n-1:
					break
				s+="{"
				for p in self.data[j][j+i]:
					 s+= p+","
				s+="} : "
			s+="\n"

		return s

	def __getitem__(self,key):
		return self.data[key]

class Recognizer:
	def __init__(self,CNF,debug = False):
		self.CNF = CNF
		self.debug = debug
		self.index = self.indexing()
		#print "GRAMMAR SIZE : ",len(self.CNF.production)

	def recognize(self,token):

		self.token = token
		self.triTable = Tritable(len(self.token))
		self.n = len(token)

		for i in range(self.n):
			t = self.token[i].type
			if t in self.index:
				for prod in self.index[t]:
					self.triTable[i][i].add(prod.left)

		if self.debug:
			print "== initial =="
			print self.triTable

		for i in range(1,self.n):
			for j in range(i,self.n):
				for k in range(j-i,j):
					A = self.triTable[j-i][k]
					B = self.triTable[k+1][j]
					C = self.cross(A,B)
					for c in C:
						if c in self.index:
							for prod in self.index[c]:
								self.triTable[j-i][j].add(prod.left)

				if self.debug:
					print "== update ("+str(j-i)+","+str(j)+") =="
					print self.triTable

		if not self.CNF.start in self.triTable[0][self.n-1]:
			raise Exception("The input is not in this grammar")

		return self.triTable

	def cross(self,A,B):
		ret = set()
		for a in A:
			for b in B:
				ret.add(a+b)
		return ret

	def indexing(self):
		index = {}
		for p in self.CNF.production:
			key = ""
			for r in p.right:
				key +=r

			if key in index:
				index[key].append(p)
			else:
				index[key] = [p]
		return index