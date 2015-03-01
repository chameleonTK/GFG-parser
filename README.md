# Compiler-compiler #

We implement this parser generator based on "Parsing with Picture" , Keshav Pingali and Gianfranco Bilardi
[[ ref ]](http://apps.cs.utexas.edu/tech_reports/reports/tr/TR-2102.pdf)

It's modify of the Earley's algorithm that easier to understand. we use Grammar Flow Graph (GFG) as a representation of Context Free Grammar (CFG) to parse code.

GFG is tool that can reformulated parsing problem to the problem of finding certain kinds of path in graph.


# TODO #
* debug mode
* not support epsilon production
* EBNF format
* testing 
* cannot parser multiple tree

# Installation #
* Clone our project
> git clone https://kramatk@bitbucket.org/kramatk/earleyparser.git

* Link our lib to your `$PYTHONPATH`
> sudo ln -s noom /usr/lib/python2.7/noom

* Set your `$PATH`
> export PATH=$PATH:/your/absolute/path/

* Make our project execuable
>cd noom
>chmod +x Noom.py

# Usage #
* create your Grammar 

``````````````````
root -> exp
exp -> LPAREN exp PLUS exp RPAREN | LPAREN exp MINUS exp RPAREN
exp -> NUMBER

``````````````````
* create your Lexicon base on [PLY tools](http://www.dabeaz.com/ply/ply.html)

``````````````````
# List of token names.   This is always required
tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    "lexicon error"    
    raise Exception("Illegal character '%s'" % t.value[0])     
    t.lexer.skip(1)

``````````````````
* create your compiler
> Noom.py [lexicon] [grammar] -o [compiler/name].py


* modify your compiler 
