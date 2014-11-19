

# Compiler-compiler #

We implement this parser generator based on "Parsing with Picture" , Keshav Pingali and Gianfranco Bilardi
[[ ref ]](http://apps.cs.utexas.edu/tech_reports/reports/tr/TR-2102.pdf)

It's modify of the Earley's algorithm that easier to understand. we use Grammar Flow Graph (GFG) as a representation of Context Free Grammar (CFG) to parse code.

GFG is tool that can reformulated parsing problem to the problem of finding certain kinds of path in graph.


# Update #
* renew , by using GFG
* implement simply original earley recoginzer

* * * 

## Context Free Object ##

### [#] ContextFree( grammar , lexicon) ###

**grammar** is address of file that contain grammar information (string)

**lexicon** is address of file that contain lexicon information (string)

grammar file format
``````````````````
root -> exp
exp -> exp PLUS exp | exp MINUS exp
exp -> NUMBER
``````````````````

lexicon file format
``````````````````
NUMBER -> \d+
PLUS -> \+
MINUS -> -
MUL -> \*
DIV -> /
``````````````````

### [#] self.nonterminal ###
return set() of nonterminal 

### [#] self.terminal ###
return set() of terminal 

### [#] self.production ###
return list of `Production object`

### [#] self.start ###
return "root" if `grammar` file has `root` production

### [#] self.lexicon ###
return dictionary `[key =  terminal symbol]` `[value = Re object]`

### [#] ContextFree.isTerminal( s ) ###
return `True` if s is terminal format ( we defined s is terminal when s is UpperChar )

### [#] ContextFree.isNonTerminal( s ) ###
return `True` if s is non-terminal format 

### [#] ContextFree.isToken( lexicon , s ) ###
return `True` if s is terminal of lexicon


* * *

## Production Object ##

### [#] Production( left , right) ###

**left** is Terminal in left side of production (string).

**right** is String that is right side of production separate each terminal/non-terminal by space  (string)

### [#] self.left ###
return terminal in left side

### [#] self.right ###
return list of terminal in right

### [#] self.isEpsilon() ###
return `True` if self is epsilon production

* * *