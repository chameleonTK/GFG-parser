#!/bin/bash
for i in `seq 0 4999`;
do
        ../Noom.py ../example/expression/expression.lex ../example/expression/expression_full.gram -b exp/exp$i.in >> earley.out
        echo $i
done


