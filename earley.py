# -*- coding: utf-8 -*-

from recognizer import Recognizer

class Earley():
	def __init__(self,grammar,lexical):
		self.grammar = grammar
		self.lexcical = lexical
		self.algor = Recognizer(grammar,lexical)

	def recognize(self,txt):
		return self.algor.recognize(txt)
		
	


G9 = [
		{"l":"ROOT","r":["A"]},
		{"l":"A","r":["B","C"]},
		{"l":"B","r":["n"]},
		{"l":"C","r":["op"]},
	]


G1 = [
		{"l":"ROOT","r":["E"]},
		{"l":"E","r":["T","op","n"]},
		{"l":"E","r":["n"]},
		{"l":"T","r":["E"]},
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


p  = Earley(G9,L)


st = raw_input()
p.recognize(st.split(" "))
