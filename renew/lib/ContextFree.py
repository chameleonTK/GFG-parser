import re
import types
import imp

class Production:
	def __init__(self,l,r,action):
		l = l.strip()
		r = r.strip().split(" ")

		self.left = l
		self.right = r
		self.action = action

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
		
		self.nonterminal = set()
		self.terminal = set()
		for t in lex.tokens:
			self.terminal.add(t)
		
		self.production = []
		self.start = None
		self.get_production_semantic_file(gram)

		self.lexicon = lex

	@staticmethod
	def get_production_grammar_file(gram):
		fin = open(gram)
		start = None
		production = []
		for line in fin:
			l,r = line.split("->")
			l = l.strip()
			if l == "root":
				if start != None:
					raise Exception("too Many start symbol")			
				start = 'root'
			for rule in r.split("|"):
				production.append( Production(l,rule,None) )
		return production

	def get_production_semantic_file(self,gram):
		mod = imp.load_source("*", gram)
		for x in dir(mod):
			obj = getattr(mod,x)
			if isinstance(obj, types.FunctionType):
				line = obj.__doc__
				l,r = line.split("->")
				l = l.strip()
				self.nonterminal.add(l)
				if l == "root":
					self.start = "root"

				p = Production(l,r,obj)
				self.production.append(p)
		#raise Exception("xxx")	

		
		

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

	

