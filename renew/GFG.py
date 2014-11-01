from ContextFree import ContextFree

class GFG:
	def __init__(self,grammar):
		self.grammar = grammar

	def __str__(self):
		return str(self.grammar)


g = ContextFree("example/grammar","example/lexicon")	

print GFG(g)
