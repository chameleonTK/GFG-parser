class State:
	def __init__(self,state,parent=None,complete=None):
		self.rule = state[0]
		self.dot = state[1]
		self.start = state[2]
		self.parent = parent
		self.complete = complete
	
	def is_complete(self):
		return self.dot==len(self.rule["r"])

	def next(self):
		if self.dot >= len(self.rule["r"]):
			return None
		return self.rule["r"][self.dot]

	def prev(self):
		if self.dot < 0:
			return None
		return self.rule["r"][self.dot-1]

	def __cmp__(self,s):
		if self.rule == s.rule and self.dot == s.dot and self.start == s.start :
			return 0
		return -1

	def __str__(self):

		s = self.rule["l"]+" -> "
		for i in range(len(self.rule["r"])):
			if	i == self.dot:
				s+="."
			s += self.rule["r"][i]+" "

		if self.dot== len(self.rule["r"]):
			s += ". \t\t" + str(self.start)
		else:
			s += "\t\t" + str(self.start)
		return s


class Chart:
	def __init__(self, states , j =0 ,debug = False):
		self.states = states
		self.index = j
		self.debug = debug

	def __str__(self):
		return str(self.states[0])

	def add_state(self, state):
		if not state in self.states:
			self.states.append(state)
			if self.debug:
				print "\t",state,self.index
		#else:
		#	print "BOO",state.start

	def completeness(self):
		complete = []
		for state in self.states:
			if state.is_complete():
				complete.append(state)
		return complete