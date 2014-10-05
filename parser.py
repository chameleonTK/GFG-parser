# -*- coding: utf-8 -*-

from earley import Earley

class Parser():
	def __init__(self,grammar,lexical):
		self.grammar = grammar
		self.lexcical = lexical
		self.algor = Earley(grammar,lexical)

	def recognize(self,txt):
		return self.algor.recognize(txt)
		
	


G1 = [
		{"l":"ROOT","r":["E"]},
		{"l":"E","r":["E","op","E"]},
		{"l":"E","r":["n"]},
	]


G2 = [
		{"l":"ROOT","r":["E"]},
		{"l":"E","r":["E","op","E"]},
		{"l":"E","r":["leftpar","E","rightpar"]},
		{"l":"E","r":["n"]},
	]

L = {
		"1":"n",
		"2":"n",
		"3":"n",
		"4":"n",
		"5":"n",
		"6":"n",
		"7":"n",
		"8":"n",
		"9":"n",
		"(":"leftpar",
		")":"rightpar",
		"+":"op",
		"-":"op",
	}


p  = Parser(G1,L)


st = raw_input()
p.recognize(st.split(" "))
