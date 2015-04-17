def sem_root_1(p):
	'root -> single_input'
	return p[0]

def sem_single_input_1(p):
	'single_input -> NEWLINE'
	return []

def sem_single_input_2(p):
	'single_input -> simple_stmt'
	return p[0]

def sem_single_input_3(p):
	'single_input -> compound_stmt'
	return p[0]

def sem_single_input_4(p):
	'single_input -> compound_stmt NEWLINE'
	return p[0]

def sem_simple_stmt_1(p):
	'simple_stmt -> small_stmts NEWLINE'
	return p[0]

def sem_simple_stmt_2(p):
	'simple_stmt -> small_stmts SEMICOLON NEWLINE'
	return p[0]

def sem_small_stmts_1(p):
	'small_stmts -> small_stmts SEMICOLON small_stmt'
	p[0].append(p[2])
	return p[0]

def sem_small_stmts_2(p):
	'small_stmts -> small_stmt'
	return [ p[0] ]

def sem_small_stmt_1(p):
	'small_stmt -> flow_stmt'
	p[0]["type"] = "flow"
	return p[0]

def sem_small_stmt_2(p):
	'small_stmt -> expr_stmt'
	return p[0]

def sem_small_stmt_3(p):
	'small_stmt -> print_stmt'
	return {"type":"print","print": p[0] }

def sem_expr_stmt_1(p):
	'expr_stmt -> testlist ASSIGN testlist'
	return {"type":"assign","a": p[0],"b": p[2]}

def sem_expr_stmt_2(p):
	'expr_stmt -> testlist'
	return {"type":"expr","a": p[0] }

def sem_print_stmt_1(p):
	'print_stmt -> PRINT tests'
	return p[1]

def sem_flow_stmt_1(p):
	'flow_stmt -> return_stmt'
	return p[0]

def sem_flow_stmt_2(p):
	'flow_stmt -> break_stmt'
	return p[0]

def sem_flow_stmt_3(p):
	'flow_stmt -> continue_stmt'
	return p[0]

def sem_break_stmt_1(p):
	'break_stmt -> BREAK'
	return {"mode":"break"}

def sem_continue_stmt_1(p):
	'continue_stmt -> CONTINUE'
	return {"mode":"continue"}

def sem_return_stmt_1(p):
	'return_stmt -> RETURN testlist'
	return {"mode":"return","val": p[1] }


def sem_compound_stmt_1(p):
	'compound_stmt -> if_stmt'
	return [p[0]]

def sem_compound_stmt_2(p):
	'compound_stmt -> funcdef'
	return [p[0]]

def sem_compound_stmt_3(p):
	'compound_stmt -> while_stmt'
	return [p[0]]

def sem_if_stmt_1(p):
	'if_stmt -> IF test COLON suite'
	return {"type":"if","cond":p[1],"then":p[3],"else": None}

def sem_if_stmt_2(p):
	'if_stmt -> IF test COLON suite ELSE COLON suite'
	return {"type":"if","cond":p[1],"then" : p[3],"else":p[6]}

def sem_while_stmt_1(p):
	'while_stmt -> WHILE test COLON suite'
	return {"type":"while","cond":p[1],"do" : p[3]}

def sem_funcdef_1(p):
	'funcdef -> DEF NAME parameters COLON suite'
	return {"type":"def","name":p[1].value, "param":p[2] ,"do" : p[4]}

def sem_parameters_1(p):
	'parameters -> LPAR RPAR'
	return []

def sem_parameters_2(p):
	'parameters -> LPAR varargslist RPAR'
	return p[1]

def sem_varargslist_1(p):
	'varargslist -> varargslist COMMA NAME'
	p[0].append( p[2].value )
	return p[0]

def sem_varargslist_2(p):
	'varargslist -> NAME'
	return [ p[0].value ]

def sem_suite_1(p):
	'suite -> simple_stmt'
	return p[0]

def sem_suite_2(p):
	'suite -> NEWLINE INDENT stmts DEDENT'
	return p[2]

def sem_stmts_1(p):
	'stmts -> stmts stmt'
	p[0].extend(p[1])
	return p[0]

def sem_stmts_2(p):
	'stmts -> stmt'
	return p[0]

def sem_stmt_1(p):
	'stmt -> simple_stmt'
	return p[0]

def sem_stmt_2(p):
	'stmt -> compound_stmt'
	return p[0]

def sem_comparison_1(p):
	'comparison -> expr'
	return p[0]

def sem_comparison_2(p):
	'comparison -> relexpr'
	return p[0]

def sem_expr_1(p):
	'expr -> expr PLUS term'
	return {"op":"PLUS","a":p[0],"b":p[2]}

def sem_expr_2(p):
	'expr -> expr MINUS term'
	return {"op":"MINUS","a":p[0],"b":p[2]}

def sem_expr_3(p):
	'expr -> term'
	return p[0]

def sem_term_1(p):
	'term -> term MULT factor'
	return {"op":"MULT","a":p[0],"b":p[2]}

def sem_term_2(p):
	'term -> term DIV factor'
	return {"op":"DIV","a":p[0],"b":p[2]}

def sem_term_3(p):
	'term -> term MOD factor'
	return {"op":"MOD","a":p[0],"b":p[2]}

def sem_term_4(p):
	'term -> factor'
	return p[0]

def sem_factor_1(p):
	'factor -> PLUS factor'
	raise Exception("not support unary operation")
	return p

def sem_factor_2(p):
	'factor -> MINUS factor'
	raise Exception("not support unary operation")
	return p

def sem_factor_3(p):
	'factor -> power'
	return p[0]

def sem_power_1(p):
	'power -> atom'
	p[0]["trailer"] = None
	return p[0]

def sem_power_2(p):
	'power -> atom trailer'
	p[0]["trailer"] = p[1]
	return p[0]

def sem_atom_1(p):
	'atom -> NAME'
	return {"val": p[0].value ,"op":"NAME"} 

def sem_atom_2(p):
	'atom -> NUMBER'
	return {"val": p[0].value ,"op":"NUM"} 

def sem_atom_3(p):
	'atom -> STRING'
	return {"val": p[0].value ,"op":"STRING"} 

def sem_atom_4(p):
	'atom -> LPAR testlist RPAR'
	return {"val": p[1] ,"op":"PAREN"} 

def sem_trailer_1(p):
	'trailer -> LPAR arglist RPAR'
	return p[1]

def sem_relexpr_1(p):
	'relexpr -> expr LT expr'
	return {"op":"LT","a":p[0],"b":p[2]}

def sem_relexpr_2(p):
	'relexpr -> expr LE expr'
	return {"op":"LE","a":p[0],"b":p[2]}

def sem_relexpr_3(p):
	'relexpr -> expr GT expr'
	return {"op":"GT","a":p[0],"b":p[2]}

def sem_relexpr_4(p):
	'relexpr -> expr GE expr'
	return {"op":"GE","a":p[0],"b":p[2]}

def sem_relexpr_5(p):
	'relexpr -> expr EQ expr'
	return {"op":"EQ","a":p[0],"b":p[2]}

def sem_relexpr_6(p):
	'relexpr -> expr NE expr'
	return {"op":"NE","a":p[0],"b":p[2]}

def sem_testlist_1(p):
	'testlist -> testlist_multi COMMA'
	return p[0]

def sem_testlist_2(p):
	'testlist -> testlist_multi'
	return p[0]

def sem_testlist_multi_1(p):
	'testlist_multi -> testlist_multi COMMA test'
	p[0].append(p[2])
	return p[0]

def sem_testlist_multi_2(p):
	'testlist_multi -> test'
	return [ p[0] ]

def sem_test_1(p):
	'test -> comparison'
	return p[0]

def sem_arglist_1(p):
	'arglist -> arglist COMMA argument'
	p[0].append(p[2])
	return p[0]

def sem_arglist_2(p):
	'arglist -> argument'
	return [p[0]]

def sem_argument_1(p):
	'argument -> test'
	return p[0]

def sem_tests_1(p):
	'tests -> tests COMMA test'
	p[0].append(p[2])
	return p[0]

def sem_tests_2(p):
	'tests -> test'
	return [p[0]]


import sys,os
from noom.Noom import Noom


class PYTHON:
	def __init__(self):
		self.variable = {}
		self.loop = []
		self.function = {}

	def eval_expr(self,p):
		if p["op"] == "PLUS":
			a = self.eval_expr(p["a"])
			b = self.eval_expr(p["b"])
			return a+b
		elif p["op"] == "MINUS":
			a = self.eval_expr(p["a"])
			b = self.eval_expr(p["b"])
			return a-b
		elif p["op"] == "MULT":
			a = self.eval_expr(p["a"])
			b = self.eval_expr(p["b"])
			return a*b
		elif p["op"] == "MOD":
			a = self.eval_expr(p["a"])
			b = self.eval_expr(p["b"])
			if b==0:
				raise Exception("ZeroDivisionError: integer division or modulo by zero")
			return a%b
		elif p["op"] == "DIV":
			a = self.eval_expr(p["a"])
			b = self.eval_expr(p["b"])
			if b==0:
				raise Exception("ZeroDivisionError: integer division or modulo by zero")
			return a/b

		elif p["op"] == "PAREN":
			return p["val"]

		elif p["op"] == "NUM":
			return p["val"]

		elif p["op"] == "STRING":
			return p["val"]

		elif p["op"] == "NAME":
			if p["trailer"] is None:

				if p["val"] not in self.variable:
					raise Exception("NameError: name '"+p["val"]+"' is not defined")
				return self.variable[p["val"]]

			else:
				if p["val"] not in self.function:
					raise Exception("NameError: name '"+p["val"]+"' is not defined")

				raise Exception("LazyError: Not Implement yet")

		elif p["op"] == "LT":
			a = self.eval_expr(p["a"])
			b = self.eval_expr(p["b"])
			return a < b
		elif p["op"] == "LE":
			a = self.eval_expr(p["a"])
			b = self.eval_expr(p["b"])
			return a <= b
		elif p["op"] == "GT":
			a = self.eval_expr(p["a"])
			b = self.eval_expr(p["b"])
			return a > b
		elif p["op"] == "GE":
			a = self.eval_expr(p["a"])
			b = self.eval_expr(p["b"])
			return a >= b
		elif p["op"] == "EQ":
			a = self.eval_expr(p["a"])
			b = self.eval_expr(p["b"])
			return a == b
		elif p["op"] == "NE":
			a = self.eval_expr(p["a"])
			b = self.eval_expr(p["b"])
			return a != b
		else:
			raise Exception("OperationError: Cannot Operate")

	def run(self,cmd):
		for ins in cmd:
			ret = None
			if ins["type"]=="expr":
				ret = ()
				for expr in ins["a"]:
					ret += (self.eval_expr(expr),)
				if len(ret)==1:
					ret = ret[0]

			elif ins["type"]=="assign":
				if len(ins["a"]) != len(ins["b"]):
					raise Exception("TypeError: doesn't match all value")
				for i in range( len(ins["a"])):
					a = ins["a"][i]
					b = ins["b"][i]
					if a["op"] == "NAME":
						self.variable[ a["val"] ] = self.eval_expr(b)
					else:
						raise Exception("SyntaxError: can't assign to literal")

			elif ins["type"]=="print":
				for p in ins["print"]:
					print self.eval_expr(p),
				print ""

			elif ins["type"]=="if":

				if self.eval_expr( ins["cond"]) :
					ret = self.run( ins["then"] )
				else:
					if ins["else"] is not None:
						ret = self.run( ins["else"] )			

			elif ins["type"]=="while":

				self.loop.append(0)
				while self.eval_expr( ins["cond"]) :
					status = self.run( ins["do"] )

					if status == "break":
						break

				self.loop.pop()

			elif ins["type"]=="flow":

				if ins["mode"] == "return" : 
					raise Exception("LazyError: Not Implement yet")
						
				if len(self.loop) <= 0:
					raise Exception("SyntaxError: '"+ins["mode"]+"' outside loop")

				ret = ins["mode"]
				


			elif ins["type"]=="def":
				self.function[ ins["name"] ] = ins


			if ret == "continue" or ret == "break" or ret=="return" :
				break

			if ret is not None:
				print ret

			

		return ret
			

		

def input_statement():
	statement = raw_input(">>> ")
	while statement=="":
		statement = raw_input(">>> ")

	if len(statement) > 1 and statement[-1] == ":":
		statement +="\n"
		tmp = raw_input("... ")
		while tmp!="":
		 	statement += tmp+"\n"
		 	tmp = raw_input("... ")

	statement +="\n"

	return statement

if __name__ == "__main__":

	lex = "/home/tk/Desktop/Senior/noom/example/python/python.lex"
	E  = Noom(os.path.abspath(__file__),lex)
	E.tokenizer.lexer = E.tokenizer.obj.IndentLexer()

	print "\n** Python subset Interpreter **"
	print "** modify by TK ** "
	print "** credit \"GardenSnake language\" http://ow.ly/KEckv \n"

	python = PYTHON()
	
	statement = input_statement()
	while statement!= "exit":
		cmd = E.run(statement)

		python.run(cmd)
		statement = input_statement()