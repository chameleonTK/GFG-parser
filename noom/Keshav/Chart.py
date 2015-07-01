from noom.ContextFree import ContextFree
from Track import Track
class State:
	def __init__(self,rule,start,track):
		self.rule = rule
		self.start = start
		self.next = self.rule.next()
		self.prev = self.rule.prev()
		self.track = None
		self.set_parent(track)
		
	
	def set_parent(self,track):
		self.track = Track(track,self)
		
	def is_predictor(self):
		return not( self.is_scanner() or self.is_completer() )

	def is_scanner(self):
		return (self.next is not None) and ContextFree.isTerminal(self.next)

	def is_completer(self):
		return self.next is None

	def __cmp__(self,s):
		if self.rule == s.rule and self.start == s.start :
			return 0
		return -1

	def __str__(self):
		return str(self.rule)+"["+str(self.start)+"]"

	def __hash__(self):
		return hash(str(self))

class Chart:
	def __init__(self , index ,token , debug = False):
		self.states = set()
		self.index = index
		self.debug = debug
		self.token = token
		self.queue = []

	def __str__(self):
		s = " ========= "+str(self.index)+" ========== \n"
		for state in self.states:
			s+= "\t"+str(state)+"\n"
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
		# else:
		# 	for s in self.states:
		# 		if s==state:
		# 			#print s.track
		# 			break
		# 	#print " --------differ---------"
		# 	#print state.track



			
		#if not state in self.states:
			#if self.debug:
				#print "\t",state,"[",state.start,",",self.index,"]"
		#else:
		#	print "BOO",state.start

		

	

