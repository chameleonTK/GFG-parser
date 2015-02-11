#!/bin/bash
bison -d parser.y
flex parser.l
mv parser.tab.h parser.h
gcc -o parser *.c
