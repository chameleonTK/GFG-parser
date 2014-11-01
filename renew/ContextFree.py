import re

class Production:
	def __init__(self,l,r):
		l = l.strip()
		r = r.strip().split(" ")

		self.left = l
		self.right = r

	def isEpsilon(self):
		if len(self.right)==1 and self.right[0]=="EPSILON":
			return True
		return False
	
	
	def __str__(self):
		return self.left+" -> "+" ".join(self.right)



class ContextFree:
	def __init__(self,gram,lex):
		fin = open(gram)
	
		
		self.nonterminal = set()
		self.terminal = set()
		
		self.production = []
		self.start = None
	
		for line in fin:
			l,r = line.split("->")

			l = l.strip()
			self.nonterminal.add(l)
			if l == "root":
				self.start = "root"


			for rule in r.split("|"):
				self.production.append( Production(l,rule) )

		fin = open(lex)

		self.lexicon = {}
		for line in fin:
			l,r = line.split("->")
			l = l.strip()
			r = r.strip()	
			self.terminal.add(l)
			self.lexicon[l] = re.compile(r""+r)


	def __str__(self):
		s=""
		for rule in self.production:
			s+= str(rule)+"\n"
		return s

	@staticmethod
	def isTerminal(s):
		return s.isupper()

	@staticmethod
	def isNonTerminal(s):
		return (not s.isupper())

	@staticmethod
	def isToken(lex,st):
		return (self.lexicon[lex].match(st) is not None)

