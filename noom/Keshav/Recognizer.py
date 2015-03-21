from GrammarFlow import GrammarFlow
from Chart import * 

class Recognizer():
	def __init__(self,GFG,debug = False):
		self.GFG = GFG
		self.debug = debug

	def recognize(self,token):
		i=0
		self.init(token)
		
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

			i+=1


		fin = State(self.GFG.final,0)
		self.fin = None
		for state in self.charts[len(self.charts)-1].states:
			if fin == state:
				self.fin = state

		if self.fin is None:
			raise Exception("The input is not in this grammar")

		return self.charts

	def  init(self,token):
		self.token = token
		self.charts=[Chart(n,self.token[n],self.debug) for n in range(len(self.token))]
		self.charts.append( Chart(len(self.token),None,self.debug) )

		if self.debug:
			print "Initial"

		s = State(self.GFG.start ,0)
		self.charts[0].add_state(s)
				
				

	
	def predictor(self,state,j):
		for next in self.GFG.edge[str(state.rule)]:
			node = self.GFG.edge[str(state.rule)][next].end
			s = State(node,j)
			self.charts[j].add_state(s)

	
	def scanner(self,state,j):
		if j >= len(self.token):
			return False

		if self.GFG.isToken(state.next,self.token[j]):
			for next in self.GFG.edge[str(state.rule)]:
				node = self.GFG.edge[str(state.rule)][next].end

				s = State(node,state.start)
				self.charts[j+1].add_state(s)
			
	
	def completer(self,state,j):

		if state.rule.isType("end"):

			for st in self.charts[state.start].states:
				if not st.rule.isType("pro"):
					continue
				
				if st.next == state.rule.ele:

					for next in self.GFG.edge[str(state.rule)]:
						node = self.GFG.edge[str(state.rule)][next].end
						if node.ele == st.rule.ele and node.dot == st.rule.dot+1 :

							s = State(node,st.start)
							self.charts[j].add_state(s)
				
		else:
			for next in self.GFG.edge[str(state.rule)]:
				node = self.GFG.edge[str(state.rule)][next].end
				s = State(node,state.start)
				self.charts[j].add_state(s)

		
		#return False
	

