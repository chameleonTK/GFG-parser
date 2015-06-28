class Track:
	def __init__(self,parent,child):
		self.parent = parent  #track object
		self.child = child    #state object

	def __str__(self):
		s = str(self.child)+"\n"
		p = self.parent
		while p is not None:
			s += "->"+str(p.child)+"\n"
			p = p.parent
		return s