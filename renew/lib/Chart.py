from ContextFree import ContextFree

class State:
	def __init__(self,rule,start):
		self.rule = rule
		self.start = start
		self.next = self.rule.next()
		self.prev = self.rule.prev()
	
	def is_predictor(self):
		return not( self.is_scanner() or self.is_completer() )

	def is_scanner(self):
		return self.next!=None and ContextFree.isTerminal(self.next)

	def is_completer(self):
		return self.next==None

	def __cmp__(self,s):
		if self.rule == s.rule and self.start == s.start :
			return 0
		return -1

	def __str__(self):
		return str(self.rule)+"["+str(self.start)+"]"


class Chart:
	def __init__(self , index ,token , debug = False):
		self.states = []
		self.index = index
		self.debug = debug
		self.token = token

	def __str__(self):
		s = " ========= "+str(self.index)+" ========== \n"
		for state in self.states:
			s+= "\t"+str(state)+"\n"
		return s

	def add_state(self, state):
		if not state in self.states:
			self.states.append(state)
			#if self.debug:
				#print "\t",state,"[",state.start,",",self.index,"]"
		#else:
		#	print "BOO",state.start

	

