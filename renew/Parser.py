from ContextFree import ContextFree,Production
from GrammarFlow import GrammarFlow
from Chart import * 
from AST import * 

class Parser():
	def __init__(self,GFG,debug = False):
		self.GFG = GFG
		self.debug = debug

	def parse(self,charts):
		self.start = None
		self.charts = charts
		state = State(self.GFG.final,0)
		
		last_index = len(self.charts)-1
		for s in self.charts[last_index].states:
			if s.is_completer() and s.rule.isType("pro") and s.rule.ele.left == state.rule.ele:
				self.start = s

		self.index = last_index		
		if self.debug:
			print "START : "
			print "recur",self.start,self.index

		
		return self.recur(self.start)

		
	
	def recur(self,state):

		rule = state.rule.ele
		rule_index = len(rule.right)-1


		tree = AST(rule.left)

		while rule_index >= 0 :
			child = None
			if ContextFree.isTerminal(rule.right[rule_index]):
				child = AST(rule.right[rule_index])
				self.index -=1
			else:
				for s in self.charts[self.index].states:
					if s.is_completer() and s.rule.isType("pro") and s.rule.ele.left == rule.right[rule_index]:

						if self.debug:
							print "recur",s,self.index

						child = self.recur(s)

			tree.children.insert(0,child)
			rule_index -=1		
					
		return tree