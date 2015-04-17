class Production:
	def __init__(self,l,r,action):
		l = l.strip()
		r = r.strip()

		self.left = l
		if r=="EPSILON":
			r=""

		self.right = r.split(" ")
		self.action = action

	def isEpsilon(self):
		if len(self.right)==1 and self.right[0]=="":
			return True
		return False
	
	def __cmp__(self,s):
		if str(self) == str(s):
			return 0
		return -1
		
	def __str__(self):
		return self.left+" -> "+" ".join(self.right)