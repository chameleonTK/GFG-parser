# -*- coding: utf-8 -*-

class Parser:

	def __init__(self,grammar,lexical):
		self.grammar = grammar
		self.lexical = lexical

	def parse(self):
		print "PARSE"
		tree = []
		for state in self.chart[len(self.txt)]:
			if state.rule["l"] =="ROOT" and state.start == 0 and (not state.incomplete()):
				tree.append(state)
		print tree
		'''
		for root in tree:
			print " === Tree ==="
			tmp_root = root
			while tmp_root is not None:
				print tmp_root,tmp_root.start
				tmp_root = tmp_root.parent
		'''
