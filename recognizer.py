# -*- coding: utf-8 -*-

from chart import * 

class Recognizer:

	def __init__(self,grammar,lexical):
		self.grammar = grammar
		self.lexical = lexical

	def recognize(self,txt):

		i=0
		self.init(txt)
		while i < len(self.chart):
			print " =================== "
			for state in self.chart[i].states:

				if not state.is_complete():
					if not state.next().islower():
						self.predictor(state,i)
					else:
						self.scanner(state,i)
				else:
					#print state,state.start,i
					self.completer(state,i)
			i+=1

		return self.chart


	def  init(self,txt):
		self.txt = txt
		self.chart=[Chart([],n) for n in range(len(txt)+1)]

		print "Initial"
		for g in self.grammar:
			if g["l"]=="ROOT":
				#tuple (grammar,dot,start)
				s = State((g,0,0))
				self.chart[0].add_state(s)


	def predictor(self,state,j):
		print "predict"
		for g in self.grammar:
			if state.next() == g["l"]:
				s = State((g,0,j))

				self.chart[j].add_state(s)
		
	def scanner(self,state,j):
		print "scanner"
		if j >= len(self.txt):
			return False

		if state.next() == self.lexical[self.txt[j]]:
			g = {"l":state.next(),"r":[self.txt[j]]}
			s = State((g,1,j))
			

			self.chart[j+1].add_state(s)
			

	def completer(self,state,j):

		print "completer"
		for st in self.chart[state.start].states:
			if st.next() == state.rule["l"]:
				#print "before",st
				s = State((st.rule,st.dot+1,st.start))
				#print s , state
				self.chart[j].add_state(s)
				#print "after",s,j

		#return False


