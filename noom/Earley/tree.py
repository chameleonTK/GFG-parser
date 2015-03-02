class Tree:
	def __init__(self,root_index,nodes):
		self.edges = []
		self.nodes = nodes
		self.root_index = root_index

	def merge(self,tree):
		self.edges.extend(tree.edges)

	def add_edge(self,e):
		self.edges.append(e)

	def set_end(self,end):
		self.end = end
	
	def print_(self,node_index,tab):
		i=0
		s=""
		node = self.nodes[node_index[0]][node_index[1]]
		while i< tab:
			s+="  "
			i+=1
		return s+node.rule["l"]+"\n"

	def tranverse(self,root_index,tab):

		s= self.print_(root_index,tab)
		for e in self.edges:
			if e[0] == root_index:
				s+= self.tranverse(e[1],tab+1)
		return s
		

	def __str__(self):
		return self.tranverse(self.root_index,0)
	