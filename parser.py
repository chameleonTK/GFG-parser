# -*- coding: utf-8 -*-
import copy
from tree import *

class Parser:
	def __init__(self,grammar,lexical):
		self.grammar = grammar
		self.lexical = lexical


	def completeness(self,charts):
		self.complete = []
		for chart in charts:
			self.complete.append(chart.completeness())


	def get_root(self):

		for i,state in enumerate(self.complete[-1]):
			if state.rule["l"] =="ROOT" and state.start == 0 and state.is_complete():
				return (i,state)
		return None

	def parse(self,charts):

		self.charts = charts
		self.completeness(charts);

		self.root = self.get_root()

		if not self.root:
			return None

		

		for i,chart in enumerate(self.complete):
			print "------ LOOP",i,"-----"
			for state in chart:
				print state

		print "\n"
		parsetree = []
		i,state = self.root
		index = (state.end,i)
		for tree in self.build_nodes(index):
			PT = Tree(index,self.complete)
			PT.merge(tree)
			print "---- Tree ----"
			print PT
			parsetree.append(PT)

		return parsetree



	def build_nodes(self,root_index):
		x = root_index[0]
		y = root_index[1]
		root = self.complete[x][y]
		parsetree = []

		if not root.rule["l"].isupper():
			return []

		if len(root.rule['r']) == 1:
			for i,node in enumerate(self.complete[root.end]):
				if node.start == root.start and node.end == root.end:
					if node != root and root.prev() == node.rule["l"]:

						node_index = (root.end,i)
						for t in self.build_nodes(node_index):
							tree = Tree(root_index,self.complete)

							tree.add_edge( (root_index,node_index))
							tree.merge(t)
							parsetree.append(tree)
			
		else:
			#for rule in reversed(root.rule["r"]):
			for i,node in enumerate(self.complete[root.end]):
				if node.end == root.end and node != root and root.prev() == node.rule["l"]:
					
					node_index = (root.end,i)
					for t in self.build_nodes(node_index):
						tree = Tree(root_index,self.complete)

						tree.add_edge( (root_index,node_index))
						tree.merge(t)

						parsetree.append(tree)
			
			#for tree in parsetree:
			#	end = tree.end

					
						
		#print root.prev()
		
		return parsetree



