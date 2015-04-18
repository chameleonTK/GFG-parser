#!/bin/bash
for i in `seq 0 99`;
do
		../Noom.py ../example/nlp/word.lex ../example/nlp/eng.gram -b nlp/eng$i.in >> nlp.out
        echo $i
done


