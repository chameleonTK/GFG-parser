# List of token names.   This is always required
tokens = (
   'VERB',
   'DET',
   'NOUN',
   'ADJ',
   'PREP',
   'ADV',
)

t_VERB    = r'eat'
t_DET    = r'a'
t_NOUN    = r'man'
t_ADJ   = r'cute'
t_PREP   = r'with'
t_ADV   = r'quickly'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \n\t'

# Error handling rule
def t_error(t):
    "lexicon error"    
    raise Exception("Illegal character '%s'" % t.value[0])     
    t.lexer.skip(1)
