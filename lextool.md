To install flex on Linux, you can use the following command:

```
sudo apt-get install flex
```

For the content of the lex file (let's call it `lex.l`), here it is:

```lex
%{  
int n = 0 ;   
%}  

%%  

"while"|"if"|"else" {n++;printf("\t keywords : %s", yytext);}   
"int"|"float" {n++;printf("\t DataType : %s", yytext);}    
[a-zA-Z_][a-zA-Z0-9_]* {n++;printf("\t identifier : %s", yytext);}  
"<="|"=="|"="|"++"|"-"|"*"|"+" {n++;printf("\t operator : %s", yytext);}
[(){}|, ;] {n++;printf("\t separator : %s", yytext);}  
[0-9]*"."[0-9]+ {n++;printf("\t float : %s", yytext);}   
[0-9]+ {n++;printf("\t integer : %s", yytext);}         
"*TOKEN*"  {printf("\n total no. of token = %d\n", n);}          	 

[\t\n\r ]+ ;

%%  

int main()  
{  
    yylex();  
}  

int yywrap()  
{  
    return 0;  
}
```

To compile and run the lexer, follow these instructions:

1. Compile the lex file using:
   ```
   lex lex.l
   ```
2. Compile the generated `lex.yy.c` file using:
   ```
   gcc lex.yy.c
   ```
3. Finally, run the lexer:
   ```
   ./a.out
   ```
