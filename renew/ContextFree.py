import re

class Production:
	def __init__(self,l,r):
		l = l.strip()
		r = r.strip().split(" ")

		self.left = l
		self.right = r

	def __str__(self):
		return self.left+" -> "+" ".join(self.right)


class ContextFree:
	def __init__(self,gram,lex):
		fin = open(gram)
	
		
		self.nonterminal = set()
		self.terminal = set()
		
		self.production = []
		self.start_sym = None
	
		for line in fin:
			l,r = line.split("->")

			l = l.strip()
			self.nonterminal.add(l)
			if l == "root":
				self.start_sym = "root"


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

	def isTerminal(self,s):
		return s.isupper()

	def isNonTerminal(self,s):
		return (not s.isupper())

	
	def isToken(self,lex,st):
		return (self.lexicon[lex].match(st) is not None)

