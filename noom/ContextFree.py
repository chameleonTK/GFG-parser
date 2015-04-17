from GrammarTranform import GrammarTranform
from Production import Production
import re, types, imp


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

	def toCNF(self):
		return GrammarTranform.toCNF(self)

	def toGFG(self):
		return GrammarTranform.toGFG(self)

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
					raise Exception("too Many root symbol")			
				start = 'root'
				
			for rule in r.split("|"):
				production.append( Production(l,rule,None) )

		if start == None:
			raise Exception("did you forget root symbol?")		
		return production

	def get_production_semantic_file(self,gram):
		mod = imp.load_source("*", gram)
		for x in dir(mod):
			if not x.startswith("sem_"):
				continue
				
			obj = getattr(mod,x)
			if isinstance(obj, types.FunctionType):
				line = obj.__doc__

				sp = line.split("->")

				l,r = sp
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

	def isTerminal(self,s):
		return ContextFree.isTerminal(s)

	def isNonTerminal(self,s):
		return ContextFree.isNonTerminal(s)


	@staticmethod
	def isTerminal(s):
		return s.isupper() #(token in self.terminal) 

	@staticmethod
	def isNonTerminal(s):
		return (not s.isupper()) #(token in self.nonterminal) 

	

