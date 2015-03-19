#! /usr/bin/python

import os
import argparse
from ContextFree import ContextFree,Production
import Keshav.GrammarFlow
import Keshav.Recognizer
import Keshav.Parser


import Earley.Recognizer
import CYK.Recognizer

import timeit

from Tokenizer import Tokenizer

class Noom:
	def __init__(self,grammar_path,lex_path, mode="Keshav"):

		self.tokenizer = Tokenizer(lex_path)
		self.grammar = ContextFree(grammar_path,self.tokenizer)
		
		if mode == "Keshav":
			GFG = Keshav.GrammarFlow.GrammarFlow(self.grammar)
			self.recg = Keshav.Recognizer.Recognizer(GFG,False)
			self.pars = Keshav.Parser.Parser(GFG,False)

		elif mode == "Earley":
			self.recg = Earley.Recognizer.Recognizer()
			print "**************** not implement *****************"

		elif mode == "CYK":
			self.recg = CYK.Recognizer.Recognizer()
			print "**************** not implement *****************"

		else:
			raise Exception("What? What Algorithm do you want?")

	def recognize(self,token):
		return self.recg.recognize(token)

	def parse(self,charts):
		return self.pars.parse(charts)

	def run(self,code):
		token = self.tokenizer.tokenize(code)
		charts = self.recognize(token)
		self.AST = self.parse(charts)
		return self.pars.semantic(self.AST)

	def benmark(self,code):
		token = self.tokenizer.tokenize(code)
		self.recognize(token)

	@staticmethod
	def set_semantic_file(productions,semantic_path):
		
		f = open(semantic_path,'w')
		prod_left = {}
		for rule in productions:
			
			if rule.left in prod_left:
				prod_left[rule.left]+=1
			else:
				prod_left[rule.left]=1

			s = "def sem_"+rule.left+"_"+str(prod_left[rule.left])+"(p):\n"
			s += "\t'"+str(rule)+"'\n"
			s += "\treturn p\n\n"
			f.write(s)

def create_compiler_file(args,output_file):

	f = open(output_file,"a")
	s = ""
	s += '\nimport sys,os\n'
	s += "from noom.Noom import Noom\n\n\n"
	s += 'if __name__ == "__main__":\n\n'
	s += '\tE  = Noom(os.path.abspath(__file__),"'+args.lexicon+'")\n'
	s += "\tif len(sys.argv) == 2 :\n"
	s += "\t\tf = open(sys.argv[1])\n"
	s += "\t\tE.run(f.read())\n"
	s += "\telse:\n"
	s += '\t\tprint "PLEASE INPUT YOUR CODE!!"\n'
	f.write(s)


if __name__ == "__main__":
    
	parser = argparse.ArgumentParser()

	parser.add_argument("-o", "--output",type=str,
                    help="name of your compiler")

	parser.add_argument("lexicon", type=str,
                    help="path to lexicon file")

	parser.add_argument("grammar", type=str,
                    help="path to grammar file")

	parser.add_argument("-b", "--benmark",type=str,
                    help="benmark [with other parsing algorithm] mode")

	args = parser.parse_args()
	
	output_file = ""
	if args.output:
		output_file = args.output
	else:
		output_file = "compiler.py"

	args.lexicon = os.path.abspath(args.lexicon)
	output_file = os.path.abspath(".")+"/"+output_file

	#E.set_semantic_file()
	productions = ContextFree.get_production_grammar_file(args.grammar)
	Noom.set_semantic_file(productions,output_file)

	if args.benmark:
		f = open(args.benmark)
		code = f.read()
		f.close()
		algorithms = ["Keshav","Earley","CYK"]
		n = 100
		print n," times to recognize"
		for alg in algorithms:
			setup_statement = "from noom.Noom import Noom;"+'E = Noom("'+output_file+'","'+args.lexicon+'",mode="'+alg+'")'
			t = timeit.timeit("E.benmark('"+code+"')",setup=setup_statement,number=n)
			print "Algorithm : " , alg  ," : ",t," us"

	else:
		create_compiler_file(args,output_file)

	
