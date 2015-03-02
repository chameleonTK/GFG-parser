from noom.ContextFree import ContextFree

class Condition():
	def __init__(self,start,end,state):
		self.start = start
		self.end = end
		self.state = [state[0],state[1]]

	def __str__(self):
		return "["+self.state[0]+str(self.start)+" : "+self.state[1]+str(self.end)+"]"

	def is_start_with_equal(self):
		if self.state[0]=="=":
			return True
		return False

	def is_end_with_equal(self):
		if self.state[1]=="=":
			return True
		return False

	def set_start_end(self,type_,val):
		if type_  == 0:
			self.start =val
		else:
			self.end =val

	def get_start_end(self,type_):
		if type_  == 0:
			return self.start
		else:
			return self.end

	def set_state(self,type_,val):
		self.state[type_] = val

	@staticmethod
	def compatible(a,b):
		c = Condition(0,0,"==")
		if not a:
			return False
		if not b:
			return False

		for i in range(2):
			a_val = a.get_start_end(i)
			b_val = b.get_start_end(i)
			if a.state[i] == "=":
				if b.state[i] == "=":
					if  a_val != b_val:
						return False
					else:
						c.set_start_end(i,a_val)
						c.set_state(i,"=")

				elif b.state[i] == ">":
					if a_val > b_val:
						c.set_start_end(i,a_val)
						c.set_state(i,"=")
					else:
						return False						
				else:
					if a_val < b_val:
						c.set_start_end(i,a_val)
						c.set_state(i,"=")
					else:
						return False
			elif a.state[i] == ">":
				if b.state[i] == "=":
					if b_val > a_val:
						c.set_start_end(i,b_val)
						c.set_state(i,"=")
					else:
						return False
				elif b.state[i] == ">":
					if a_val > b_val:
						c.set_start_end(i,a_val)
						c.set_state(i,">")
					else:
						c.set_start_end(i,b_val)
						c.set_state(i,">")
				else:
					if a_val+1 == b_val-1:
						c.set_start_end(i,a_val+1)
						c.set_state(i,"=")
					else:
						c.set_start_end(i,a_val)
						c.set_state(i,">")
			else:
				if b.state[i] == "=":
					if b_val < a_val:
						c.set_start_end(i,b_val)
						c.set_state(i,"=")
					else:
						return False

				elif b.state[i] == ">":
					if a_val-1 == b_val+1:
						c.set_start_end(i,a_val-1)
						c.set_state(i,"=")
					else:
						c.set_start_end(i,a_val)
						c.set_state(i,"<")
					
				else:
					if a_val < b_val:
						c.set_start_end(i,a_val)
						c.set_state(i,"<")
					else:
						c.set_start_end(i,b_val)
						c.set_state(i,"<")
		return c

	def make_condition(self,rule):

		condition_forward = []
		start_equal_state = False
		if self.is_start_with_equal():
			start_equal_state = True

		start = self.start
		for i in range(len(rule.right)):
			if ContextFree.isTerminal(rule.right[i]) and start_equal_state:
				condition_forward.append( Condition(start,start+1,"==") )
			else:
				if start_equal_state:
					start_equal_state = False
					condition_forward.append( Condition(start,start,"=>") )
				else:
					condition_forward.append( Condition(start-1,start,">>") )
			start += 1

		############### backword state ############
		condition_backward = []
		end_equal_state = False
		if self.is_end_with_equal():
			end_equal_state = True

		end = self.end
		for i in range(len(rule.right)-1,-1,-1):
			if ContextFree.isTerminal(rule.right[i]) and end_equal_state:
				condition_backward.append( Condition(end-1,end,"==") )
			else:
				if end_equal_state:
					end_equal_state = False
					condition_backward.insert(0, Condition(end,end,"<=") )
				else:
					condition_backward.insert(0, Condition(end,end+1,"<<") )
			end -= 1

		############# compatible ########
		condition = []
		for i in range(len(rule.right)):
			c = Condition.compatible( condition_forward[i],condition_backward[i])
			#print condition_forward[i],condition_backward[i]," >> ",c
			condition.append(c)

		return condition