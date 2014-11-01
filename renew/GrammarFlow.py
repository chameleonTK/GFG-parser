
from ContextFree import ContextFree,Production
		
class Node:
	def __init__(self,ele,dot):
		self.ele = ele
		self.dot = dot
		if ele is Production:
			self.type = ["pro"]
		else:
			if self.dot == 0:
				self.type = ["start"]
			else:
				self.type = ["end"]

	def isType(self,tp):
		return (tp in self.type)
		
	def __str__(self):
		return Node.label(self.ele,self.dot)
		
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
				s+="."
			return s

		else:
			if dot ==0:
				return "."+str(ele)
			else:
				return str(ele)+"."
        
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
				print "epsilon production"
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
		nMark = 0
		while len(queue) > 0:
			focus = queue.pop(0)
			mark[focus] = True
			nMark +=1
			s += focus+"\n"
			
			if self.edge.has_key(focus):			
				for k in self.edge[focus].keys():
					if not mark[k]:
						queue.append(k)
					s+= " >>>> "+str(self.edge[focus][k]) +"\n"
			s+="\n"
		return s


G = ContextFree("example/grammar","example/lexicon")	
print " ----- "
GFG = GrammarFlow(G)
print GFG
