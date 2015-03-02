# -*- Mode: Python -*-

# An Earley Parser.
# J. Earley, "An efficient context-free parsing algorithm",
#  Communications of the Association for Computing Machinery, 13:2:94-102, 1970.

from pprint import pprint as pp
is_a = isinstance

class nonterminal:
    def __init__ (self, name):
        self.name = name
    def __repr__ (self):
        return '<%s>' % (self.name,)

class terminal:
    def __init__ (self, name):
        self.name = name
    def __repr__ (self):
        return '{%s}' % (self.name,)

class token:
    def __init__ (self, kind, val):
        self.kind = kind
        self.val = val
    def __repr__ (self):
        return '{%s:%s}' % (self.kind, self.val)

NT = nonterminal
TERM = terminal
TOK = token
EOF = TERM ('eof')
PHI = NT ('PHI')

class parser:
    def __init__ (self, grammar, root):
        self.grammar = grammar
        self.root = root
        self.states = [
            [(PHI, 0, [root, EOF], EOF, 0, None)] # S0
            ]

    def go (self, toks):
        for i in range (len (toks)):
            tok = toks[i]
            self.step (tok, i)
        if len(self.states[-1]) == 1 and self.states[-1][0][0] is PHI:
            return self.build_parse_tree()
        else:
            raise ValueError ('string not recognized!')
        
    def step (self, tok, i):
        next = []
        states = self.states[-1]
        j = 0
        while j < len(states):
            state = states[j]
            j += 1
            nt, dot, prod, look, start, tok0 = state
            if dot == len (prod):
                # completer
                if tok.kind == look.name:
                    for state0 in self.states[start]:
                        nt0, dot0, prod0, look0, start0, tok0 = state0
                        if prod0[dot0] == nt:
                            maybe_new = (nt0, dot0+1, prod0, look0, start0, tok0)
                            if maybe_new not in states:
                                states.append (maybe_new)
            elif is_a (prod[dot], nonterminal):
                nt0 = prod[dot]
                # predictor
                for prod0 in self.grammar[nt0]:
                    if dot+1 >= len(prod):
                        look0 = look
                    else:
                        look0 = prod[dot+1]
                    maybe_new = (nt0, 0, prod0, look0, i, None)
                    if maybe_new not in states:
                        states.append (maybe_new)
            elif is_a (prod[dot], terminal) and tok.kind == prod[dot].name:
                # scanner
                next.append ((nt, dot+1, prod, look, start, tok))
        self.states.append (next)

    def build_parse_tree (self):
        # this uses the technique described in "Parsing Techniques - A Practical Guide".
        # [http://www.cs.vu.nl/~dick/PTAPG.html] the method described by Earley is
        #  confusing (and wrong in some cases).

        # remove non-completed states
        self.states = all = [
            # i.e.,               dot  == len(prod)
            [st for st in sts if st[1] == len(st[2])] for sts in self.states
            ]

        def walk (nt, end):
            # walk backward through completed set at <end>,
            #   find a completed version of non-terminal <nt>.
            for st in reversed (all[end]):
                if st[0] == nt:
                    # ok, we found a completed rule for this nt.
                    # walk backward through the production, recursing,
                    #   building this node of the parse tree in the process.
                    r = [nt]
                    prod = st[2]
                    for x in reversed (prod):
                        if is_a (x, nonterminal):
                            x, end = walk (x, end)
                            r.insert (1, x)
                        else:
                            r.insert (1, st[-1])
                            end -= 1
                    return r, end
        # maybe just use PHI instead?


        root = all[-1][0][2][0]
        r, end = walk (root, len(all)-2)
        return r



E = NT ('E')
T = NT ('T')
P = NT ('P')
plus = TERM ('+')
mult = TERM ('*')
ident = TERM ('ident')

g = {
    E: [[T,plus,T]],
    T: [[T,mult,P], [P]],
    P: [[ident]],
    }

p = parser (g, E)
s = [TOK('ident', 'a'),
     TOK('*', '*'),
     TOK ('ident', 'b'),
     TOK ('+', '+'),
     TOK ('ident', 'c'),
     TOK ('eof', 'eof')
     ]

#print(p.go(s))
pp(p.go(s))
