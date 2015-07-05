from noom.ContextFree import ContextFree

class State:
	def __init__(self,rule,dot,start):
		self.rule = rule
		self.dot = dot
		self.start = start
		self.end = None

	def set_end(self,end):
		self.end = end
	
	def is_complete(self):
		return self.dot==len(self.rule.right)

	def is_scanner(self):
		return  ContextFree.isTerminal(self.next())


	def next(self):
		if self.dot >= len(self.rule.right):
			return None

		return self.rule.right[self.dot]

	def prev(self):
		if self.dot < 0:
			return None

		return self.rule.right[self.dot-1]

	def __cmp__(self,s):
		if self.rule == s.rule and self.dot == s.dot and self.start == s.start :
			return 0

		return -1

	def __str__(self):
		return str(self.rule)+"["+str(self.dot)+"] "+"["+str(self.start)+"]"

	def __hash__(self):
		return hash(str(self))

class Chart:
	def __init__(self ,index = 0 , debug = False):
		self.states = set()
		self.index = index
		self.debug = debug
		self.queue = []

	def __str__(self):
		s=""
		for i in self.states:
			s+= str(self.states[i])+"\n"

		return s
		
	def next(self):
		if len(self.queue) <= 0:
			return None
		return self.queue.pop(0)

	def add_state(self, state):
		len_prev = len(self.states)
		self.states.add(state)
		if len_prev != len(self.states):
			self.queue.append(state)

		# if not state in self.states:
		# 	state.set_end(self.index)
		# 	self.states.append(state)
		# 	if self.debug:
		# 		print "\t",state
		# 