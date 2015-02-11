
from ContextFree import ContextFree,Production
from GrammarFlow import GrammarFlow
from Parser import Parser
from Recognizer import Recognizer


class Earley:
	def __init__(self,grammar_path,tokenizer):
		G = ContextFree(grammar_path ,tokenizer)
		GFG = GrammarFlow(G)

		self.tokenizer = tokenizer
		self.grammar = GFG.grammar
		self.recg = Recognizer(GFG,False)
		self.pars = Parser(GFG,False)

	def recognize(self,token):
		return self.recg.recognize(token)

	def parse(self,charts):
		return self.pars.parse(charts)

	def run(self,code):
		token = self.tokenizer.tokenize(code)
		charts = self.recognize(token)
		AST = self.parse(charts)
		return AST
