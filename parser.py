# -*- coding: utf-8 -*-

class Node:
	def __init__(self, body, children):
		self.body = body
		self.children = children


	def print_(self,tab):
		i=0
		s=""
		while i< tab:
			s+="  "
			i+=1
		return s+self.body

	def tranverse(self,tab):
		s = self.print_(tab)
		for child in self.children:
			s += " [ "+child.body+"]"
		s+='\n'

		for child in self.children:
			s += child.tranverse(tab+1)
		return s

	def __str__(self):
		return self.tranverse(0)

	def is_leaf(self):
		return len(self.children) == 0


class Parser:
	def __init__(self,grammar,lexical):
		self.grammar = grammar
		self.lexical = lexical


	def completeness(self,charts):
		self.complete = []
		for chart in charts:
			self.complete.append(chart.completeness())


	def get_root(self):
		root = []
		for state in self.complete[-1]:
			if state.rule["l"] =="ROOT" and state.start == 0 and state.is_complete():
				root.append(state)
		print root
		return root

	def parse(self,charts):

		self.charts = charts
		self.completeness(charts);

		self.root = self.get_root()

		if len(self.root)==0:
			return None



	def build_nodes(self, root):
		return "A"

