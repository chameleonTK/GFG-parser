class AST:
	def __init__(self,ele):
		self.ele = ele
		self.children = []
	
	def __str__(self):
		return AST.printAST(self,0)

	@staticmethod
	def printAST(t,n):
		s=""
		for i in range(n):
			s+="    "	
		s+= str(t.ele)+"\n"

		for e in t.children:
			s += AST.printAST(e,n+1)
		return s
