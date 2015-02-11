import ply.lex as lex

class Tokenizer:

	tokens = (
	   'NUMBER',
	   'PLUS',
	   'MINUS',
	   'TIMES',
	   'DIVIDE',
	   'LPAREN',
	   'RPAREN',
	)

	
	t_PLUS	= r'\+'
	t_MINUS   = r'-'
	t_TIMES   = r'\*'
	t_DIVIDE  = r'/'
	t_LPAREN  = r'\('
	t_RPAREN  = r'\)'

	def t_NUMBER(self,t):
		r'\d+'
		t.value = int(t.value)	
		return t

	def t_newline(self,t):
		r'\n+'
		t.lexer.lineno += len(t.value)

	t_ignore  = ' \t'

	def t_error(self,t):
		print "Illegal character '%s'" % t.value[0]
		t.lexer.skip(1)

	def build(self,**kwargs):
		self.lexer = lex.lex(module=self, **kwargs)
	
	# Test it output
	def __init__(self,lexicon):
		self.lexicon = lexicon
		print " WARNING : not support lexicon-file input"
		self.build()

	def tokenize(self,data):
		self.lexer.input(data)
		token = []
		while True:
			 tok = self.lexer.token()
			 if not tok: break
			 token.append(tok)
		return token