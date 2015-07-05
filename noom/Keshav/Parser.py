from noom.AST import AST

from GrammarFlow import GrammarFlow
from Chart import * 
from Condition import Condition

class Parser():
	def __init__(self,GFG,debug = False):
		self.GFG = GFG
		self.grammar = self.GFG.grammar
		self.debug = debug
		self.multiple = True

	def semantic(self,ast):		
		p = []
		for ch in ast.children:
			if self.grammar.isTerminal(ch.ele):
				p.append(ch.ref)
			else:
				s = self.semantic(ch)
				p.append(s)

		if not self.grammar.isTerminal(ast.ele):
			return ast.ref.action(p)
		return p


	def parse(self,obj):
		
		self.charts,self.start = obj

		last_index = len(self.charts)-1
		self.seq = []
		p = self.start.track
		while p is not None:
			self.seq.append(p.child)
			p = p.parent

		self.index = 0
		print self.recur()

		raise Exception("stop it")

		# print a.ele # left production
		# print a.ref # production
		# print a.children # [ AST obj]
	
	def recur(self):
		pass
		s = self.seq[self.index]	
		print s,
		if s.rule.isType("pro"):
			print "production"
			children = []
			target = self.seq[self.index]
			while target.rule.dot != 0:
				if self.grammar.isTerminal(target.prev):
					self.index +=1
					node = AST(target.prev)
					#set reference to terminal 
				else:
					self.index +=1
					print "\n\nbefore",target
					node = self.recur()
					self.index+=1
					print "after",target,"\n\n"

				children.append(node)
				target = self.seq[self.index]
				print "next ",target,target.rule.type

			print s.rule.ele ," wooooo"
			self.index +=1
			return children, s.rule
		else:
			print "terminal"
			if s.rule.isType("end"):
				ast = AST(s.rule.ele)

				self.index += 1
				children,ref = self.recur()
				ast.set_children(children)
				ast.set_reference(ref)
				return ast
			else:
				print s.rule.type
				raise Exception("start")
				
