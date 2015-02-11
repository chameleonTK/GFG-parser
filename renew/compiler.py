from lib import Earley
from Tokenizer import Tokenizer

T = Tokenizer("example/lexicon")
E  = Earley.Earley("example/grammar",T)

print "Enter your code : ",
st = raw_input()
print E.run(st)
