import Keshav.GrammarFlow
import CYK.ChomskyForm

class GrammarTranform:
	def __init__(self,grammar):
		self.grammar = grammar

	@staticmethod
	def toGFG(grammar):
		return Keshav.GrammarFlow.GrammarFlow(grammar)

	@staticmethod
	def toCNF(grammar):
		CNF = CYK.ChomskyForm.ChomskyForm()
		return CNF.toCNF(grammar)

	@staticmethod
	def toNonEpsilon(grammar):
		CNF = CYK.ChomskyForm.ChomskyForm()
		return CNF.toNonEpsilon(grammar)