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
	
	def __cmp__(self,s):
		if str(self) == str(s):
			return 0
		return -1
		
	def __str__(self):
		return self.left+" -> "+" ".join(self.right)



class ContextFree:
	def __init__(self,gram,lex):
		fin = open(gram)
	
		self.nonterminal = set()
		self.terminal = set()
		for t in lex.tokens:
			self.terminal.add(t)
		
		self.production = []
		self.start = None
	
		for line in fin:
			l,r = line.split("->")

			l = l.strip()
			self.nonterminal.add(l)
			if l == "root":
				if self.start != None:
					raise Exception("too Many start symbol")

				self.start = "root"


			for rule in r.split("|"):
				self.production.append( Production(l,rule) )

		self.lexicon = lex
		'''
		fin = open(lex)
		self.lexicon = {}
		for line in fin:
			l,r = line.split("->")
			l = l.strip()
			r = r.strip()	
			self.terminal.add(l)
			self.lexicon[l] = re.compile(r""+r)
		'''

	def isToken(self,type_,token):
		#return (self.lexicon[lex].match(st) is not None)
		return ( token.type == type_ )

	def __str__(self):
		s=""
		for rule in self.production:
			s+= str(rule)+"\n"
		return s

	@staticmethod
	def isTerminal(s):
		return s.isupper() #(token in self.terminal) 

	@staticmethod
	def isNonTerminal(s):
		return (not s.isupper()) #(token in self.nonterminal) 

	

