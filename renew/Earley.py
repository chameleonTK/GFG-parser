
from ContextFree import ContextFree,Production
from GrammarFlow import GrammarFlow
from Parser import Parser
from Recognizer import Recognizer

class Earley():
	def __init__(self,GFG):
		self.grammar = GFG.grammar
		self.recg = Recognizer(GFG,False)
		self.pars = Parser(GFG,True)

	def recognize(self,token):
		return self.recg.recognize(token)

	def parse(self,charts):
		return self.pars.parse(charts)
		


#G = ContextFree("example/grammar","example/lexicon")	
G = ContextFree("example/grammar","example/lexicon")	

GFG = GrammarFlow(G)

E  = Earley(GFG)


st = raw_input()
print "Enter your code : ",st

charts = E.recognize(st.split(" "))


AST = E.parse(charts);

print AST
