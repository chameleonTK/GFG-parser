def sem_root_1(p):
	'root -> exp'
	print "cal >",p[0]
	return p

def sem_exp_1(p):
	'exp -> LPAREN exp PLUS exp RPAREN'
	return p[1]+p[3]

def sem_exp_2(p):
	'exp -> LPAREN exp MINUS exp RPAREN'
	return p[1]-p[3]

def sem_exp_3(p):
	'exp -> NUMBER'
	return int(p[0].value)


import sys
from lib.Earley import Earley


if __name__ == "__main__":

	E  = Earley("cmp-expression.py","../example/expression/expression.lex")
	print "#### THIS GRAMMAR MUST HAVE PARENs IN EVERY OPERATION ####"
	while True:
		try:
			E.run(raw_input("cal > "))
		except:
			print ""
			break
		

