enum { plus,minus,multiply,divide,lparen,rparen,number,var};

typedef struct NodeDesc *Node;
typedef struct NodeDesc {
	int kind;
	int val;
	Node left,right;
} NodeDesc;


