def sem_root_1(p):
	'root -> exp'
	print "cal >",p[0]
	return p

def sem_exp_1(p):
	'exp -> exp PLUS term'
	return p[0]+p[2]

def sem_exp_2(p):
	'exp -> exp MINUS term'
	return p[0]-p[2]

def sem_exp_3(p):
	'exp -> term'
	return p[0]

def sem_term_1(p):
	'term -> term TIMES pre'
	return p[0]*p[2]

def sem_term_2(p):
	'term -> term DIVIDE pre'
	return p[0]//p[2]

def sem_term_3(p):
	'term -> pre'
	return p[0]

def sem_pre_1(p):
	'pre -> PLUS state'
	return p[1]

def sem_pre_2(p):
	'pre -> MINUS state'
	return p[1]

def sem_pre_3(p):
	'pre -> state'
	return p[0]

def sem_state_1(p):
	'state -> NUMBER'
	return int(p[0].value)

def sem_state_2(p):
	'state -> LPAREN exp RPAREN'
	return p[1]


import sys,os
from noom.Noom import Noom


if __name__ == "__main__":

	E  = Noom(os.path.abspath(__file__),"/home/tk/Desktop/Senior/noom/example/expression/expression.lex")
	while True:
		E.run(raw_input("cal > "))
