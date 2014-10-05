# -*- coding: utf-8 -*-

class State:
	def __init__(self,state):
		self.rule = state[0]
		self.dot = state[1]
		self.start = state[2]
	
	def incomplete(self):
		return self.dot!=len(self.rule["r"])

	def next(self):
		if self.dot >= len(self.rule["r"]):
			return ""
		return self.rule["r"][self.dot]

	def compare(self,s):
		if self.rule == s.rule and self.dot == self.dot and self.start == s.start :
			return True
		return False

	def __str__(self):

		s = self.rule["l"]+" -> "
		for i in range(len(self.rule["r"])):
			if	i == self.dot:
				s+="."
			s += self.rule["r"][i]+" "

		if self.dot== len(self.rule["r"]):
			s += "."
		return s

class Earley:

	def __init__(self,grammar,lexical):
		self.grammar = grammar
		self.lexical = lexical

	def recognize(self,txt):

		self.txt = txt
		self.chart=[[] for n in range(len(txt)+1)]

		for g in self.grammar:
			if g["l"]=="ROOT":
				#tuple (grammar,dot,start)
				s = State((g,0,0))
				self.chart[0].append(s)

		print "Initial"
		for st in self.chart[0]:
			print "\t",st

		for i in range(len(txt)+1):
			print " =================== "
			for state in self.chart[i]:
				if state.incomplete():
					if not state.next().islower():
						self.predictor(state,i)
					else:
						self.scanner(state,i)
				else:
					#print state,state.start,i
					self.completer(state,i)

		self.parse()

		return self.chart

	def parse(self):
		print "PARSE"
		tree = []
		for state in self.chart[len(self.txt)]:
			if state.rule["l"] =="ROOT" and state.start == 0 and (not state.incomplete()):
				tree.append(state)
		print tree
		'''
		for root in tree:
			print " === Tree ==="
			tmp_root = root
			while tmp_root is not None:
				print tmp_root,tmp_root.start
				tmp_root = tmp_root.parent
		'''


	def repeat_chart(self,j,s):
		for state in self.chart[j]:
			if state.compare(s):
				return True
		return False
				

	def predictor(self,state,j):
		#print "predict"
		for g in self.grammar:
			if state.next() == g["l"]:
				s = State((g,0,j))

				if self.repeat_chart(j,s):
					continue

				#print "\t",s,s.start,j		
				self.chart[j].append(s)
		
	def scanner(self,state,j):
		#print "scanner"
		if j >= len(self.txt):
			return False

		if state.next() == self.lexical[self.txt[j]]:
			g = {"l":state.next(),"r":[self.txt[j]]}
			s = State((g,1,j))
			if self.repeat_chart(j+1,s):
				return False

			self.chart[j+1].append(s)
			#print "\t",s,s.start,j+1
			return True

	def completer(self,state,j):

		print "completer"
		print state

		for st in self.chart[state.start]:
			if st.next() == state.rule["l"]:
				print "next",st
				s = State((st.rule,st.dot+1,st.start))
				#print s , state
				#print "\t",s,s.start,j
				self.chart[j].append(s)
				print "add",s
				#if s.rule["l"]=="ROOT" and (not s.incomplete()) and j == len(self.txt):
				#	return True

		#return False


