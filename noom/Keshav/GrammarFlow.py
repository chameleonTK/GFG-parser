from noom.ContextFree import ContextFree
		
class Node:
	def __init__(self,ele,dot):
		self.ele = ele
		self.dot = dot
		self.type = set()
		if isinstance(self.ele,basestring):
			if self.dot == 0:
				self.type.add("start")
			else:
				self.type.add("end")
		else:
			self.type.add("pro")

		self.key = Node.label(self.ele,self.dot)
		self.edgeTo = set()

	def next(self):
		if isinstance(self.ele,basestring):
			if self.dot == 0:
				return self.ele
			else:
				return None
		else:
			if self.dot < len(self.ele.right):
				return self.ele.right[self.dot]
			else:
				return None

	def prev(self):
		if isinstance(self.ele,basestring):
			if self.dot == 1:
				return self.ele
			else:
				return None
		else:
			if self.dot >= 1:
				return self.ele.right[self.dot-1]
			else:
				return None


	def isType(self,tp):
		return (tp in self.type)
		
	def __str__(self):
		return self.key

	def __cmp__(self,s):
		if str(self) == str(s):
			return 0
		return -1

	def __hash__(self):
		return hash(self.key)
		
	@staticmethod
	def label(ele,dot):
		#print ele
		if isinstance(ele,basestring):
			if dot ==0:
				return "."+str(ele)+" "
			else:
				return str(ele)+". "
		else:
			s = ele.left+" -> "
			for i in range(len(ele.right)):
				if i==dot:
					s+= ". "
				s+= ele.right[i]+" "

			if len(ele.right)==dot:
				s+=". "
			return s
'''
class Edge:
	def __init__(self,nodeA,nodeB,label=None):
		self.start = nodeA
		self.end = nodeB
		self.label = label

	def __str__(self):
		if self.label is None:
			return "("+str(self.start)+" , "+str(self.end)+")"
		else:
			return "("+str(self.start)+" , "+str(self.end)+") with "+self.label
'''

class GrammarFlow:
	def __init__(self,grammar):
		self.grammar = grammar
		
		self.node = {}

		for non in self.grammar.nonterminal:
			start = Node(non,0)
			end = Node(non,1)
			self.node[ str(start)] = start
			self.node[ str(end)] = end
		
		for prod in self.grammar.production:
			if prod.isEpsilon():
				raise Exception("not support epsilon production")
			else:
				for i in range(len(prod.right)+1):
					n = Node(prod,i)
					self.node[str(n)] = n
				#entry
				self.node[Node.label(prod.left,0)].edgeTo.add( self.node[Node.label(prod,0)])

				#exit
				self.node[Node.label(prod,len(prod.right))].edgeTo.add( self.node[Node.label(prod.left,1)] )

				for i in range(len(prod.right)):

					if ContextFree.isTerminal(prod.right[i]):
						# scan with label : prod.right[i]
						self.node[Node.label(prod,i)].edgeTo.add( self.node[Node.label(prod,i+1)] )
						
					if ContextFree.isNonTerminal(prod.right[i]):
						#call
						self.node[Node.label(prod,i)].edgeTo.add( self.node[Node.label(prod.right[i],0)] )
						#return
						self.node[Node.label(prod.right[i],1)].edgeTo.add(self.node[Node.label(prod,i+1)])

		self.start = self.node[Node.label(grammar.start,0)]
		self.final = self.node[Node.label(grammar.start,1)]

	def isToken(self,a,b):
		return self.grammar.isToken(a,b)
		
	def __str__(self):

		s=""
		mark = {}
		for k in self.node.keys():
			mark[k]=False

		queue = [str(self.start)]
		mark[str(self.start)] = True

		nMark = 0
		while len(queue) > 0:
			focus = queue.pop(0)
			nMark +=1
			s += focus+"\n"

			if self.edge.has_key(focus):			
				for k in self.edge[focus].keys():
					if not mark[k]:
						mark[k] = True
						queue.append(k)

					s+= " >>>> "+str(self.edge[focus][k]) +"\n"
			s+="\n"
			
		return s