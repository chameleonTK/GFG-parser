5  REM HELLO WORLD PROGAM
10 PRINT "HELLO WORLD",1+2
11 READ A1,A2,A3,A4
12 LET D = A1*A4 - A4*A2
13 IF D = 0 THEN 65
30 READ B1,B2
32 LET X1 = (B1*A4 - B2*A2)/D
33 LET X2 = (A1*B2 - A3*B1)/D
34 PRINT X1,X2
35 GOTO 30
65 PRINT "NO UNIQUE SOLUTION"
66 DATA 1,2,4
67 DATA 2,-7,5
68 DATA 1,3,4,-7
99 END
