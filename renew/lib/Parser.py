from ContextFree import ContextFree,Production
from GrammarFlow import GrammarFlow
from Chart import * 
from AST import AST 
from Condition import Condition

class Parser():
	def __init__(self,GFG,debug = False):
		self.GFG = GFG
		self.debug = debug
		self.multiple = True

	def semantic(self,AST):		
		p = []
		for ch in AST.children:
			if ContextFree.isTerminal(ch.ele):
				p.append(ch.ref)
			else:
				s = self.semantic(ch)
				p.append(s)

		if not ContextFree.isTerminal(AST.ele):
			return AST.ref.action(p)
		return p


	def parse(self,charts):
		self.start = None
		self.charts = charts
		state = State(self.GFG.final,0)
		
		last_index = len(self.charts)-1
		for s in self.charts[last_index].states:
			if s.is_completer() and s.rule.isType("pro") and s.rule.ele.left == state.rule.ele:
				self.start = s

		self.index = last_index		
		start_cond = Condition(0,len(self.charts)-1,"==")

		if self.debug:
			print "START : "
			print "recur",self.start,self.index , " with condition [",start_cond,"]"
		return self.recur(self.start , start_cond )

	def recur(self,state,left_cond):

		rule = state.rule.ele
		rule_index = len(rule.right)-1

		right_cond = left_cond.make_condition(rule)

		tree = AST(rule.left,rule)

		while rule_index >= 0 :
			child = None
			if ContextFree.isTerminal(rule.right[rule_index]):
				if self.debug:
					print "terminal " ,rule.right[rule_index], self.charts[self.index-1].token.value
				#child = AST(rule.right[rule_index])
				token = self.charts[self.index-1].token
				child = AST(token.type,token)
				self.index -=1
			else:
				cardidate_state = []
				for s in self.charts[self.index].states:
					if s.is_completer() and s.rule.isType("pro") and s.rule.ele.left == rule.right[rule_index]:

						if self.debug:
							print "\t>> cardidate ",s,self.index
						cardidate_state.append(s)

				is_ambiguous = 0
				next_state = None
				next_cond = None
				for c in cardidate_state:
					#Condition.compatible(a,b)
					a = right_cond[rule_index]
					b = Condition(c.start,self.index,"==")
					cond_ = Condition.compatible( a ,b)

					if cond_:
						is_ambiguous += 1
						next_state = c
						next_cond = cond_

				if is_ambiguous == 1:
					if self.debug:
						print "recur ",next_state,self.index, " with condition > [",next_cond,"]"
					child = self.recur(next_state,next_cond)
					if self.debug:
						print "end recur"
				else:
					raise Exception("ambiguous")

			tree.children.insert(0,child)
			rule_index -=1		
					
		return tree