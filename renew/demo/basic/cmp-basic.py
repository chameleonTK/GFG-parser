import sys

def sem_root_1(p):
	'root -> program'
	return p[0]

def sem_program_1(p):
	'program -> program statement'
	p[0].append(p[1])
	return p[0]

def sem_program_2(p):
	'program -> statement'
	return [p[0]]

def sem_statement_1(p):
	'statement -> INTEGER command NEWLINE'
	return {"line":int(p[0].value),"cmd":p[1]}

def sem_statement_2(p):
	'statement -> RUN NEWLINE'
	raise Exception("not support [statement -> RUN NEWLINE]")
	return RUN

def sem_statement_3(p):
	'statement -> LIST NEWLINE'
	raise Exception("not support [statement -> LIST NEWLINE]")
	return p

def sem_statement_4(p):
	'statement -> NEW NEWLINE'
	raise Exception("not support [statement -> NEW NEWLINE]")
	return p

def sem_statement_5(p):
	'statement -> INTEGER NEWLINE'
	return {"line":int(p[0].value),"cmd":None}

def sem_statement_6(p):
	'statement -> NEWLINE'
	return {"line":None,"cmd":None}

def sem_command_1(p):
	'command -> LET variable EQUALS expr'
	return {"type":"LET","var":p[1],"val":p[3]}

def sem_command_2(p):
	'command -> READ varlist'
	return {"type":"READ","varlist":p[1]}

def sem_command_3(p):
	'command -> DATA numlist'
	return {"type":"DATA","numlist":p[1]}

def sem_command_4(p):
	'command -> PRINT plist optend'
	return {"type":"PRINT","plist":p[1] , "opt":p[2]}

def sem_command_5(p):
	'command -> PRINT plist'
	return {"type":"PRINT","plist":p[1] , "opt": None}

def sem_optend_1(p):
	'optend -> COMMA'
	return "COMMA"

def sem_optend_2(p):
	'optend -> SEMI'
	return "SEMI"

def sem_command_6(p):
	'command -> PRINT'
	return {"type":"PRINT","plist":[]}

def sem_command_7(p):
	'command -> GOTO INTEGER'
	return {"type":"GOTO","tar":int(p[1].value)}

def sem_command_8(p):
	'command -> IF relexpr THEN INTEGER'
	return {"type":"IF","cond":p[1],"then":int(p[3].value)}

def sem_command_9(p):
	'command -> FOR ID EQUALS expr TO expr'
	return {"type":"FOR","var":p[1].value,"init":p[3],"to":p[5],"step": None}

def sem_command_10(p):
	'command -> FOR ID EQUALS expr TO expr STEP expr'
	return {"type":"FOR","var":p[1].value,"init":p[3],"to":p[5],"step":p[7]}

def sem_command_11(p):
	'command -> NEXT ID'
	return {"type":"NEXT","var":p[1].value}

def sem_command_12(p):
	'command -> END'
	return {"type":"END"}

def sem_command_13(p):
	'command -> REM'
	return {"type":"REM"}

def sem_command_14(p):
	'command -> STOP'
	return {"type":"STOP"}

def sem_command_15(p):
	'command -> DEF ID LPAREN ID RPAREN EQUALS expr'
	raise Exception("not support [command -> DEF ID LPAREN ID RPAREN EQUALS expr]")
	return p

def sem_command_16(p):
	'command -> GOSUB INTEGER'
	raise Exception("not support [command -> GOSUB INTEGER]")
	return p

def sem_command_17(p):
	'command -> RETURN'
	raise Exception("not support [command -> RETURN]")
	return p

def sem_command_18(p):
	'command -> DIM dimlist'
	raise Exception("not support [command -> DIM dimlist]")
	return p

def sem_dimlist_1(p):
	'dimlist -> dimlist COMMA dimitem'
	return p

def sem_dimlist_2(p):
	'dimlist -> dimitem'
	return p

def sem_dimitem_1(p):
	'dimitem -> ID LPAREN INTEGER RPAREN'
	return p

def sem_dimitem_2(p):
	'dimitem -> ID LPAREN INTEGER COMMA INTEGER RPAREN'
	return p

def sem_expr_1(p):
	'expr -> expr PLUS term'
	return {"op":"PLUS","a":p[0],"b":p[2]}

def sem_expr_2(p):
	'expr -> expr MINUS term'
	return {"op":"MINUS","a":p[0],"b":p[2]}

def sem_expr_3(p):
	'expr -> term'
	return {"op":"NONE","a":p[0]}

def sem_term_1(p):
	'term -> term TIMES expo'
	return {"op":"TIMES","a":p[0],"b":p[2]}

def sem_term_2(p):
	'term -> term DIVIDE expo'
	return {"op":"DIVIDE","a":p[0],"b":p[2]}

def sem_term_2(p):
	'term -> term MOD expo'
	return {"op":"MOD","a":p[0],"b":p[2]}

def sem_term_3(p):
	'term -> expo'
	return {"op":"NONE","a":p[0]}

def sem_expo_1(p):
	'expo -> base POWER expo'
	return {"op":"POWER","a":p[0],"b":p[2]}

def sem_expo_2(p):
	'expo -> base'
	return {"op":"NONE","a":p[0]}

def sem_base_1(p):
	'base -> number'
	return {"op":"NUM","a":p[0]}

def sem_base_2(p):
	'base -> LPAREN expr RPAREN'
	return {"op":"NONE","a":p[1]}

def sem_base_3(p):
	'base -> variable'
	return {"op":"VAR","a":p[0]}

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
	'relexpr -> expr EQUALS expr'
	return {"op":"EQ","a":p[0],"b":p[2]}

def sem_relexpr_6(p):
	'relexpr -> expr NE expr'
	return {"op":"NE","a":p[0],"b":p[2]}

def sem_variable_1(p):
	'variable -> ID'
	return {"var":p[0].value}

def sem_variable_2(p):
	'variable -> ID LPAREN expr RPAREN'
	raise Exception("not support [variable -> ID LPAREN expr RPAREN]")
	#list
	return p

def sem_variable_3(p):
	'variable -> ID LPAREN expr COMMA expr RPAREN'
	raise Exception("not support [variable -> ID LPAREN expr COMMA expr RPAREN]")
	#table
	return p

def sem_varlist_1(p):
	'varlist -> varlist COMMA variable'
	p[0].append(p[2])
	return p[0]

def sem_varlist_2(p):
	'varlist -> variable'
	return [p[0]]

def sem_numlist_1(p):
	'numlist -> numlist COMMA number'
	p[0].append(p[2])
	return p[0]

def sem_numlist_2(p):
	'numlist -> number'
	return [p[0]]

def sem_number_1(p):
	'number -> INTEGER'
	return int(p[0].value)

def sem_number_2(p):
	'number -> FLOAT'
	return float(p[0].value)

def sem_number_3(p):
	'number -> MINUS INTEGER'
	return int(p[1].value)*(-1)

def sem_number_4(p):
	'number -> MINUS FLOAT'
	return float(p[1].value)*(-1)

def sem_plist_1(p):
	'plist -> plist COMMA pitem'
	p[0].append(p[2])
	return p[0]

def sem_plist_2(p):
	'plist -> pitem'
	return [p[0]]

def sem_pitem_1(p):
	'pitem -> STRING'
	return {"label":p[0].value,"val":None} 

def sem_pitem_2(p):
	'pitem -> STRING expr'
	return {"label":p[0].value,"val":p[1]} 

def sem_pitem_3(p):
	'pitem -> expr'
	return {"label":None,"val":p[0]} 


import sys
from lib.Earley import Earley


class Data:
	def __init__(self):
		self.index = -1
		self._value = []

	def get(self):
		if self.index >= 0 and self.index < len(self._value):
			self.index+=1
			return self._value[self.index-1]
		return False

	def add(self, val):
		if self.index == -1:
			self.index = 0 
		self._value.append(val)


class BASIC:
	def __init__(self,cmd):
		self.cmd = cmd
		self.data = Data()
		self.variable = {}
		self.loop = {}

	def eval_expr(self,p):
		if p["op"] == "PLUS":
			a = self.eval_expr(p["a"])
			b = self.eval_expr(p["b"])
			return a+b
		elif p["op"] == "MINUS":
			a = self.eval_expr(p["a"])
			b = self.eval_expr(p["b"])
			return a-b
		elif p["op"] == "TIMES":
			a = self.eval_expr(p["a"])
			b = self.eval_expr(p["b"])
			return a*b
		elif p["op"] == "MOD":
			a = self.eval_expr(p["a"])
			b = self.eval_expr(p["b"])
			return a%b
		elif p["op"] == "DIVIDE":
			a = self.eval_expr(p["a"])
			b = self.eval_expr(p["b"])
			if b==0:
				raise Exception("ERROR: divide by zero")
			return a/b
		elif p["op"] == "POWER":
			a = self.eval_expr(p["a"])
			b = self.eval_expr(p["b"])
			return a**b
		elif p["op"] == "NUM":
			return p["a"]
		elif p["op"] == "VAR":
			if p["a"]["var"] not in self.variable:
				raise Exception("ERROR: not declare variable :"+p["a"])
			return self.variable[p["a"]["var"]]
		else:
			return self.eval_expr(p["a"])

	def eval_relexpr(self,p):
		if p["op"] == "LT":
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
			return False

	def run(self):
		code = {}
		PC = self.cmd[0]["line"]
		for c in self.cmd:
			code[c["line"]] = c
			if c["cmd"]["type"] == "DATA":
				for n in c["cmd"]["numlist"]:
					self.data.add(n)
		while True:
			if PC not in code:
				PC +=1
				continue

			ins = code[PC]["cmd"]

			if ins["type"] == "LET":
				self.variable[ins["var"]["var"]] = self.eval_expr( ins["val"])

			elif ins["type"] == "READ":
				for v in ins["varlist"]:
					d = self.data.get()
					if d :					
						self.variable[v["var"]] = d*(1.0)
					else:
						return None

			elif ins["type"] == "PRINT":
				isFirst = True
				for p in ins["plist"]:
					if not isFirst:
						sys.stdout.write("\t")
					else:
						isFirst = False

					if p["label"]:
						sys.stdout.write(p["label"])
					if p["val"]:
						sys.stdout.write(str(self.eval_expr(p["val"])) )

				sys.stdout.write("\n")
			
			elif ins["type"] == "GOTO":
				PC = ins["tar"]
				continue

			elif ins["type"] == "IF":
				
				if self.eval_relexpr(ins["cond"]):
					PC = ins["then"]
					continue

			elif ins["type"] == "FOR":
				self.variable[ins["var"]] = self.eval_expr( ins["init"])
				to = self.eval_expr( ins["to"] )
				step = 1
				if ins["step"]:
					step = self.eval_expr( ins["step"] )

				self.loop[ins["var"]] = { 'to': to ,'step': step , "loop": PC+1 }

			elif ins["type"] == "NEXT":
				if ins["var"] not in self.loop:
					raise Exception("ERROR : Not declare for-loop variable")

				l = self.loop[ins["var"]]
				self.variable[ins["var"]] += l["step"]
				if self.variable[ins["var"]] < l["to"]:
					PC = l["loop"]
					continue
				else:
					self.loop.pop(ins["var"], None)

			elif ins["type"] == "STOP":
				print ins
				break
			elif ins["type"] == "END":
				break
			PC +=1
			#print ins["type"],self.variable
			#raw_input()
			



if __name__ == "__main__":

	E  = Earley("cmp-basic.py","../example/basic/basic.lex")
	if len(sys.argv) == 2 :
		f = open(sys.argv[1])
		cmd = E.run(f.read())

		basic = BASIC(cmd)
		basic.run()

	else:
		print "PLEASE INPUT YOUR CODE!!"
