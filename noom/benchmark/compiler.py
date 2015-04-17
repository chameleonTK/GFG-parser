def sem_root_1(p):
	'root -> exp'
	return p

def sem_exp_1(p):
	'exp -> exp PLUS term'
	return p

def sem_exp_2(p):
	'exp -> exp MINUS term'
	return p

def sem_exp_3(p):
	'exp -> term'
	return p

def sem_term_1(p):
	'term -> term TIMES pre'
	return p

def sem_term_2(p):
	'term -> term DIVIDE pre'
	return p

def sem_term_3(p):
	'term -> pre'
	return p

def sem_pre_1(p):
	'pre -> PLUS state'
	return p

def sem_pre_2(p):
	'pre -> MINUS state'
	return p

def sem_pre_3(p):
	'pre -> state'
	return p

def sem_state_1(p):
	'state -> NUMBER'
	return p

def sem_state_2(p):
	'state -> LPAREN exp RPAREN'
	return p

