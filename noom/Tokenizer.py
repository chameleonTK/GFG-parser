import ply.lex as lex
import imp

class Tokenizer:

	def t_error(self,t):
		print "Illegal character '%s'" % t.value[0]
		t.lexer.skip(1)

	def build(self,**kwargs):
		obj = imp.load_source("*", self.lexicon)
		self.tokens = obj.tokens
		self.lexer = lex.lex(module=obj, **kwargs)
		self.obj = obj
		
	
	# Test it output
	def __init__(self,lexicon):
		self.lexicon = lexicon
		self.build()

	def tokenize(self,data):
		self.lexer.input(data)
		token = []
		while True:
			 tok = self.lexer.token()
			 if not tok: break
			 token.append(tok)
		return token