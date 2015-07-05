# -*- coding: utf-8 -*-
from Chart import * 
from profilehooks import profile

class Recognizer():
	def __init__(self,grammar,debug=False):
		self.grammar = grammar
		self.debug = debug
		self.size = len(self.grammar.production)

	
	def recognize(self,token):

		i=0
		self.init(token)
		self.fin = None

		while i < len(self.chart):
			if self.debug:
				print " =========",i,"========== "

			state = self.chart[i].next()
			while state is not None:
				if self.debug:
					print "\t",state

				if state.is_complete():
					self.completer(state,i)
				elif state.is_scanner():
					self.scanner(state,i)
				else:
					self.predictor(state,i)
				state = self.chart[i].next()

			i+=1
		if self.fin is None:
			raise Exception("The input is not in this grammar")

		return self.chart


	def init(self,token):
		self.token = token
		self.chart=[Chart(n,self.debug) for n in range(len(token)+1)]

		if self.debug:
			print "Initial"
			
		for prod in self.grammar.production:
			if prod.left == self.grammar.start:
				#tuple (grammar,dot,start)
				s = State(prod,0,0)
				self.chart[0].add_state(s)


	def predictor(self,state,j):
		if self.debug:
			print "predict"

		for prod in self.grammar.production:
			if state.next() == prod.left:
				s = State(prod,0,j)
				self.chart[j].add_state(s)
		
	def scanner(self,state,j):
		if self.debug:
			print "scanner"

		if j >= len(self.token):
			return False

		if state.next() == self.token[j].type:
			s = State(state.rule,state.dot+1,state.start)
			self.chart[j+1].add_state(s)
			# for prod in self.grammar.production:
			# 	s = State(prod,1,j)
			# 	self.chart[j+1].add_state(s)
			

	def completer(self,state,j):
		if self.debug:
			print "completer"

		for st in self.chart[state.start].states:
			if st.next() == state.rule.left:
				#print "before",st
				s = State(st.rule,st.dot+1,st.start)
				#print s , state
				self.chart[j].add_state(s)
				#print "after",s,j

		if j==len(self.chart)-1:
			if state.rule.left==self.grammar.start and state.start==0:
				self.fin = True
		#return False



