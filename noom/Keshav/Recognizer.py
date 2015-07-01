from GrammarFlow import GrammarFlow
from Chart import * 

class Recognizer():
	def __init__(self,GFG,debug = False):
		self.GFG = GFG
		self.debug = debug
		self.size = len(self.GFG.node)

	def recognize(self,token):
		i=0
		self.init(token)
		self.fin = None

		while i < len(self.charts):
			if self.debug:
				print " =========",i,"========== "

			state = self.charts[i].next()
			while state is not None:
				if self.debug:
					print "\t",state

				if state.is_scanner():
					self.scanner(state,i)
				elif state.is_completer():
					self.completer(state,i);
				else:
					self.predictor(state,i);

				state = self.charts[i].next()

			# for s in self.charts[i].states:
			# 	print s,i
			# raw_input()
			i+=1
		
		if self.fin is None:
			raise Exception("The input is not in this grammar")
		return self.charts,self.fin

	def  init(self,token):
		self.token = token
		self.charts=[Chart(n,self.token[n],self.debug) for n in range(len(self.token))]
		self.charts.append( Chart(len(self.token),None,self.debug) )

		if self.debug:
			print "Initial"

		s = State(self.GFG.start ,0,None)
		self.charts[0].add_state(s)
				
	def predictor(self,state,j):
		for node in state.rule.edgeTo:
			s = State(node,j,state.track)
			self.charts[j].add_state(s)

	
	def scanner(self,state,j):
		if j >= len(self.token):
			return False

		if self.GFG.isToken(state.next,self.token[j]):
			for node in state.rule.edgeTo:
				s = State(node,state.start,state.track)
				self.charts[j+1].add_state(s)
			
	
	def completer(self,state,j):

		if state.rule.isType("end"):

			for st in self.charts[state.start].states:
				if not st.rule.isType("pro"):
					continue
				
				if st.next == state.rule.ele:
					s = State( st.rule.returnNode,st.start,state.track)
					self.charts[j].add_state(s)

					# for node in state.rule.edgeTo:
					# 	if node.ele == st.rule.ele and node.dot == st.rule.dot+1 :
					# 		s = State(node,st.start,state.track)
					# 		self.charts[j].add_state(s)
				
		else:
			for node in state.rule.edgeTo:
				s = State(node,state.start,state.track)
				self.charts[j].add_state(s)
				if j == len(self.charts)-1 and state.start == 0 and node == self.GFG.final :
					self.fin = s

		
		#return False
	

