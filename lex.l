%{
#include <stdio.h>
%}

%%

[ \t\n]+     { }
[a-zA-Z0-9]+ { printf("%s\n", yytext); }
[+\-()*/]    { printf("%s\n", yytext); }

%%

int main(int argc, char **argv){
    yylex();
    return 0;
}
