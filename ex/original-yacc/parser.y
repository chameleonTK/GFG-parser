%{ 
#include <stdio.h> 
#include <stdlib.h>
#define KYEL  "\x1B[33m"
#define KRED  "\x1B[31m"
#define KWHT  "\x1B[37m"

enum { add,sub,mul,divd,lparen,rparen,number,var};
typedef struct NodeDesc *Node;
typedef struct NodeDesc {
	int kind;
	int val;
	char *varname;
	Node left,right;
} NodeDesc;

void printtree(Node root,int level);
 
%}
 
%union{
	struct NodeDesc *node;
}

%token <node> IDENTIFIER 
%token <node> NUMBER
%token LPAREN
%token RPAREN

%start Input
%left ADD SUB
%left MUL DIV

%% 

Input:
 Expr							{ 
									$<node>$ = $<node>1;
									printf(" \n tree :: \n\n");
									printtree($<node>$,1);
								}
 ;

Expr:
 IDENTIFIER  				{ 	$<node>$ = $<node>1; }
 | NUMBER					{ 	$<node>$ = $<node>1; }	
 | Expr ADD Expr        {  
   								Node result= (Node) malloc (sizeof(NodeDesc));
								   result->kind= add;
								   result->val = -1;
								   result->right = $<node>1;
								   result->left = $<node>3;
									$<node>$ = result;
								}
 | Expr SUB Expr        {  
   								Node result= (Node) malloc (sizeof(NodeDesc));
								   result->kind= sub;
								   result->val = -1;
								   result->right = $<node>1;
								   result->left = $<node>3;
									$<node>$ = result;
								
								}
 | Expr MUL Expr        {
   								Node result= (Node) malloc (sizeof(NodeDesc));
								   result->kind= mul;
								   result->val = -1;
								   result->right = $<node>1;
								   result->left = $<node>3;
									$<node>$ = result;
								
								}
 | Expr DIV Expr        {  
   								Node result= (Node) malloc (sizeof(NodeDesc));
								   result->kind= divd;
								   result->val = -1;
								   result->right = $<node>1;
								   result->left = $<node>3;
									$<node>$ = result;
								}
								
 | LPAREN Expr RPAREN   {  $<node>$ = $<node>2; }
 ;

%% 

void printtree(Node root,int level){
	register int i;
	if(root!=NULL){
		printtree(root->right,level+1);
		for(i=0 ; i<level ; i++) printf("   ");
		switch(root->kind){
			case add 		: printf("(+)\n"); break;
			case sub 		: printf("(-)\n"); break;
			case mul 	: printf("(*)\n"); break;
			case divd	 	: printf("(/)\n"); break;
			case var	 		: printf("%s(%s)%s\n",KRED,root->varname,KWHT); break;
			case number	 	: printf("%s(%d)%s\n",KYEL,root->val,KWHT); break;
		}
		printtree(root->left,level+1);
	}
}

int yyerror(char *s) { 
 printf("yyerror : %s\n",s); 
} 

int main(void) { 
  yyparse(); 
} 
