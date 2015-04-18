#!/bin/bash
for i in `seq 0 99`;
do
        ../Noom.py ../example/expression/expression.lex ../example/expression/expression_full.gram -b exp/exp$i.in >> exp.out
        echo $i
done


