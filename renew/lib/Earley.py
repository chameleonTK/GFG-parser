
import os
import argparse
from ContextFree import ContextFree,Production
from GrammarFlow import GrammarFlow
from Parser import Parser
from Recognizer import Recognizer
from Tokenizer import Tokenizer



class Earley:
	def __init__(self,grammar_path):

		tokenizer = Tokenizer()
		G = ContextFree(grammar_path ,tokenizer)
		GFG = GrammarFlow(G)

		self.tokenizer = tokenizer
		self.grammar = GFG.grammar
		self.recg = Recognizer(GFG,False)
		self.pars = Parser(GFG,False)

	def recognize(self,token):
		return self.recg.recognize(token)

	def parse(self,charts):
		return self.pars.parse(charts)

	def run(self,code):
		token = self.tokenizer.tokenize(code)
		charts = self.recognize(token)
		AST = self.parse(charts)
		self.pars.semantic(AST)
		return AST

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

if __name__ == "__main__":
    
	parser = argparse.ArgumentParser()

	parser.add_argument("-o", "--output",type=str,
                    help="name of your compiler")

	parser.add_argument("lexicon", type=str,
                    help="path to lexicon file")

	parser.add_argument("grammar", type=str,
                    help="path to grammar file")
	args = parser.parse_args()
	
	output_file = ""
	if args.output:
		output_file = args.output
	else:
		output_file = "compiler.py"

	#E.set_semantic_file()
	productions = ContextFree.get_production_grammar_file(args.grammar)
	Earley.set_semantic_file(productions,output_file)

	f = open(output_file,"a")
	s = ""
	s += '\nimport sys\n'
	s += "from lib import Earley\n\n\n"
	s += 'if __name__ == "__main__":\n\n'
	s += '\tE  = Earley.Earley("'+output_file+'")\n'
	s += "\tif len(sys.argv) == 2 :\n"
	s += "\t\tf = open(sys.argv[1])\n"
	s += "\t\tE.run(f.read())\n"
	s += "\telse:\n"
	s += '\t\tprint "PLEASE INPUT YOUR CODE!!"\n'
	f.write(s)
