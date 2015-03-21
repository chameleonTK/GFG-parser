import Keshav.GrammarFlow

class GrammarTranform:
	def __init__(self,grammar):
		self.grammar = grammar

	def toGFG(self):
		return Keshav.GrammarFlow.GrammarFlow(self.grammar)

	def toCNF(self):
		return self.grammar