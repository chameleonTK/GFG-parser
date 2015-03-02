from noom.ContextFree import ContextFree,Production
		
class Node:
	def __init__(self,ele,dot):
		self.ele = ele
		self.dot = dot

		if isinstance(self.ele,Production):
			self.type = ["pro"]
		else:
			if self.dot == 0:
				self.type = ["start"]
			else:
				self.type = ["end"]

	def next(self):
		if isinstance(self.ele,Production):
			if self.dot < len(self.ele.right):
				return self.ele.right[self.dot]
			else:
				return None

		else:
			if self.dot == 0:
				return self.ele
			else:
				return None

	def prev(self):
		if isinstance(self.ele,Production):
			if self.dot >= 1:
				return self.ele.right[self.dot-1]
			else:
				return None

		else:
			if self.dot == 1:
				return self.ele
			else:
				return None


	def isType(self,tp):
		return (tp in self.type)
		
	def __str__(self):
		return Node.label(self.ele,self.dot)

	def __cmp__(self,s):
		if str(self) == str(s):
			return 0
		return -1
		
	@staticmethod
	def label(ele,dot):
		#print ele
		if isinstance(ele,Production):
			s = ele.left+" -> "
			for i in range(len(ele.right)):
				if i==dot:
					s+= ". "
				s+= ele.right[i]+" "

			if len(ele.right)==dot:
				s+=". "
			return s

		else:
			if dot ==0:
				return "."+str(ele)+" "
			else:
				return str(ele)+". "
        
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

class GrammarFlow:
	def __init__(self,grammar):
		self.grammar = grammar
		
		self.node = {}
		self.edge = {}

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

				entry = Edge(self.node[Node.label(prod.left,0)],self.node[Node.label(prod,0)])
				self.addEdge(entry)

				exit = Edge(self.node[Node.label(prod,len(prod.right))],self.node[Node.label(prod.left,1)])
				self.addEdge(exit)

				for i in range(len(prod.right)):
					if ContextFree.isTerminal(prod.right[i]):
						scan = Edge(self.node[Node.label(prod,i)],self.node[Node.label(prod,i+1)],prod.right[i])
						self.addEdge(scan)
						
					if ContextFree.isNonTerminal(prod.right[i]):
						call = Edge(self.node[Node.label(prod,i)],self.node[Node.label(prod.right[i],0)])
						retn = Edge(self.node[Node.label(prod.right[i],1)],self.node[Node.label(prod,i+1)])
				
						self.addEdge(call)
						self.addEdge(retn)

		self.start = self.node[Node.label(grammar.start,0)]
		self.final = self.node[Node.label(grammar.start,1)]

	def addEdge(self,edge):
		s = str(edge.start)
		t = str(edge.end)
	
		if self.edge.has_key(s):
			if not self.edge[s].has_key(t):
				self.edge[s][t] = edge
		else:
			self.edge[s] = {}
			self.edge[s][t] = edge

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