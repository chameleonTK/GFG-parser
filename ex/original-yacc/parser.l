%{ 
#include "parser.h"
typedef struct NodeDesc *Node;
typedef struct NodeDesc {
   int kind;
    int val;
	char *varname;
    Node left,right;
 } NodeDesc;

enum { plus,minus,multiply,divide,lparen,rparen,number,var } ;

%} 

%option noyywrap 

%% 
[ \t\r\n]+ 		{ /* ignore */ } 

[0-9]+ 			{
						int i,len=strlen(yytext),val=0;
						for(i=0;i<len;i++){
							val = val*10+(yytext[i]-'0');
						}

						Node tmp =(Node)malloc(sizeof(NodeDesc));
						(tmp)->kind = number;
						(tmp)->val = val;
						yylval.node=tmp;
						//printf(" [[ %d ]]",val);
						return(NUMBER); 
					}
[a-zA-Z0-9]+ 	{ 
						Node tmp =(Node)malloc(sizeof(NodeDesc));
						(tmp)->kind = var;
						(tmp)->val = -1;

						char *a = malloc(strlen(yytext)); 
 						strncpy(a, yytext, strlen(yytext)); 
						(tmp)->varname = a;

						yylval.node=tmp;
						return(IDENTIFIER); 
					}
 
"+"				{ return (ADD);}
"-"				{ return (SUB);}
"*"				{ return (MUL);}
"/"				{ return (DIV);}
"("				{ return (LPAREN);}
")"				{ return (RPAREN);}
%% 
