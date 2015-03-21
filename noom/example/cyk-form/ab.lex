# List of token names.   This is always required
tokens = (
   'A',
   'B',
)

t_A    = r'a'
t_B   = r'b'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \n\t'

# Error handling rule
def t_error(t):
    "lexicon error"    
    raise Exception("Illegal character '%s'" % t.value[0])     
    t.lexer.skip(1)
