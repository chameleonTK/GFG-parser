
from ContextFree import ContextFree,Production
from GrammarFlow import GrammarFlow
from Parser import Parser
from Recognizer import Recognizer

class Earley():
	def __init__(self,GFG):
		self.grammar = GFG.grammar
		self.recg = Recognizer(GFG,True)
		self.pars = Parser(GFG)

	def recognize(self,token):
		return self.recg.recognize(token)

	def parse(self,charts):
		return self.pars.parse(charts)
		


G = ContextFree("example/grammar","example/lexicon")	
GFG = GrammarFlow(G)

E  = Earley(GFG)


st = "( 1 + 2 )" #raw_input()
print "Enter your code : ",st

charts = E.recognize(st.split(" "))

#for ch in charts:
#	print ch

AST = E.parse(charts);

print AST
