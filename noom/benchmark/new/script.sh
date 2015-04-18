echo "phase1"
python Benchmark.py example/expression/expression.lex example/expression/expression_full.gram benchmark/exp/exp 100 --time > exp-time.out
echo "phase2"
python Benchmark.py example/expression/expression.lex example/expression/expression_full.gram benchmark/exp/exp 100 --memory > exp-mem.out
echo "phase3"
python Benchmark.py example/expression/expression.lex example/expression/expression_cnf.gram benchmark/exp/exp 100 --time > exp-time-cnf.out
echo "phase4"
python Benchmark.py example/expression/expression.lex example/expression/expression_cnf.gram benchmark/exp/exp 100 --memory > exp-mem-cnf.out

echo "phase5"
python Benchmark.py example/expression/expression.lex example/expression/expression_full.gram benchmark/exp/exp 1000 --time --no-cyk > exp-time-without-cyk.out
echo "phase6"
python Benchmark.py example/expression/expression.lex example/expression/expression_full.gram benchmark/exp/exp 1000 --memory --no-cyk > exp-mem-without-cyk.out
echo "end"

