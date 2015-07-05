class AST:
	def __init__(self,ele,ref):
		self.ele = ele
		self.ref = ref
		self.children = []
	
	def set_children(self,children):
		self.children = children

	def set_reference(self,ref):
		self.ref = ref

	def __str__(self):
		return AST.printAST(self,0)

	@staticmethod
	def printAST(t,n):
		s=""
		s+="    "*n	
		s+= str(t.ele)+"\n"

		for e in t.children:
			s += AST.printAST(e,n+1)
		return s
