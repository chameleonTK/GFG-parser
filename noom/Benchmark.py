from noom.Noom import Noom

import os,sys
import argparse
from ContextFree import ContextFree
import resource
import timeit,time as timelib
import subprocess,psutil

from Tokenizer import Tokenizer


class Benchmark:
	def __init__(self,grammar, lexicon, prefix, count,nocyk=True):

		if nocyk:
			self.algorithms = ["Keshav","Earley"]
		else:
			self.algorithms = ["Keshav","Earley","CYK"]
			
		self.output_file = os.path.abspath(".")+"/compiler.py"
		self.lexicon = lexicon
		self.prefix = prefix
		self.count = count

		productions = ContextFree.get_production_grammar_file(grammar)
		Noom.set_semantic_file(productions,self.output_file)
		self.create_bench_file()

		self.times = 10
		self.setup()

	def create_bench_file(self):

		f = open(self.output_file,"a")
		s = ""
		s += '\nimport sys,os,time\n'
		s += "from noom.Noom import Noom\n\n\n"
		s += 'if __name__ == "__main__":\n\n'
		s += '\tE  = Noom(os.path.abspath(__file__),"'+self.lexicon+'",mode=sys.argv[1])\n'
	
		s += "\tf = open(sys.argv[2])\n"
		s += "\tE.benchmark(f.read())\n"
		s += "\tf.close()\n"
		s += "\ttime.sleep(1)\n"
		f.write(s)	

	def setup(self):
		self.NoomObj = []
		for alg in self.algorithms:
			E = Noom(self.output_file,self.lexicon,mode=alg)
			self.NoomObj.append(E)

	def read(self,n):
		path = self.prefix+str(n)+".in"
		f=open(path)
		data = f.read().strip()
		f.close()
		return data

	def time(self):

		for i in range(self.count):
			code = self.read(i)
		
			for alg in self.algorithms:
				setup_statement = "from noom.Noom import Noom;"+'E = Noom("'+self.output_file+'","'+self.lexicon+'",mode="'+alg+'")'
				t = timeit.timeit("E.benchmark('"+code+"')",setup=setup_statement,number= self.times)

				#print "Algorithm : " , alg  ," : ",t," s"
				print t," : ",
			print ""

	def memory(self):
		for i in range(self.count):
			for alg in self.algorithms:
				process = subprocess.Popen(['python',self.output_file,alg, self.prefix+str(i)+".in" ])
				#ppp = meminfo(p.pid)
		
				info = psutil.Process(process.pid)
				last = None
				while process.poll() == None:
		  			last = info.get_memory_info()
		  			timelib.sleep(0.1)
				print last[0]/float(2 ** 20)," : ",
			print ""
		

		        



if __name__ == "__main__":
    
	parser = argparse.ArgumentParser()

	parser.add_argument("lexicon", type=str,help="Path to lexicon file")
	parser.add_argument("grammar", type=str,help="Path to grammar file")
	parser.add_argument("input", type=str,help="Prefix of input file [input*.in]")
	parser.add_argument("count", type=int,help="Number of input file")

	parser.add_argument("-n","--no-head", help="Show detail of benchmark ",action="store_true")
	parser.add_argument("--no-cyk", help="Skip CYK ",action="store_true")
	parser.add_argument("--time", help="Measure execution time",action="store_true")
	parser.add_argument("--memory", help="Measure memory usage ",action="store_true")

	args = parser.parse_args()
	args.lexicon = os.path.abspath(args.lexicon)

	bench = Benchmark(args.grammar, args.lexicon , args.input , args.count,nocyk=args.no_cyk)

	if not args.no_head:

		print "*************************"
		print bench.times," times to recognize"

		for N in bench.NoomObj:
			print N.mode ," GRAMMAR SIZE ", str(N.getSize())
		print ""

		print "*************************"

	if args.memory:
		print "==== Memory usage (kb)===="
		bench.memory()

	if args.time:
		print "==== Time usage (s)===="
		bench.time()

	
		
		



