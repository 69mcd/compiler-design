import ply.lex as lex

# Define token names
tokens = (
    'NUMBER',
    'KEYWORD',
    'HEADER',
    'IDENTIFIER',
    'SYMBOL'
)

# Define token regular expressions
t_ignore = ' \t'


def t_NUMBER(t):
    r'[0-9]+|[0-9]+\.[0-9]+'
    return t


def t_KEYWORD(t):
    r'auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while'
    return t


def t_HEADER(t):
    r'\#include\s*<([a-zA-Z0-9]+\.[a-zA-Z0-9]+)>'
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z]+[a-zA-Z0-9]*'
    return t


def t_SYMBOL(t):
    r'[+*/=%;-]'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Example usage
lexer.input("""
#include <stdio.h>

int main(int argc, char *argv[]) {
    int val;
    while ((val = yylex()) != 0) { // Check for non-zero return (valid token)
        switch (val) {
            case Number:
                printf("\\n %s: Number", yytext);
                break;
            case Key:
                printf("\\n %s: Keyword", yytext);
                break;
            case Header:
                printf("\\n %s: Header", yytext);
                break;
            case ID:
                printf("\\n %s: Identifier", yytext);
                break;
            case Symbol:
                printf("\\n %s: Symbol", yytext);
                break;
        }
    }
    return 0; // Indicate successful program termination
}
""")

# Print tokens
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
