
from ContextFree import ContextFree,Production
from GrammarFlow import GrammarFlow
from Parser import Parser
from Recognizer import Recognizer

class Earley():
	def __init__(self,GFG):
		self.grammar = GFG.grammar
		self.recg = Recognizer(GFG.grammar)
		self.pars = Parser(GFG.grammar)

	def recognize(self,txt):
		return self.recg.recognize(txt)

	def parse(self,charts):
		return self.pars.parse(charts)
		


G = ContextFree("example/grammar","example/lexicon")	
GFG = GrammarFlow(G)

E  = Earley(GFG)

print "Enter your code : ",
st = raw_input()
charts = E.recognize(st.split(" "))
AST = E.parse(charts);

#print AST[0]
