# -*- coding: utf-8 -*-

from recognizer import Recognizer
from parser import Parser


class Earley():
	def __init__(self,grammar,lexical):
		self.grammar = grammar
		self.lexcical = lexical
		self.recg = Recognizer(grammar,lexical)
		self.pars = Parser(grammar,lexical)

		self.charts = None

	def recognize(self,txt):
		self.charts = self.recg.recognize(txt)
		return self.charts

	def parse(self,charts):
		return self.pars.parse(charts)
		
	


G9 = [
		{"l":"ROOT","r":["A"]},
		{"l":"A","r":["B","C"]},
		{"l":"B","r":["n"]},
		{"l":"C","r":["op"]},
	]


G5 = [
		{"l":"ROOT","r":["E"]},
		{"l":"E","r":["E","mul","E"]},
		{"l":"E","r":["E","plus","E"]},
		{"l":"E","r":["n"]},
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
		"+":"plus",
		"-":"minus",
		"*":"mul",
	}


p  = Earley(G5,L)


st = raw_input()
charts = p.recognize(st.split(" "))
AST = p.parse(charts);

#print AST[0]
