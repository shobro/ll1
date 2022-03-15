default:
	flex lex.l
	gcc -lfl lex.yy.c -o lexer