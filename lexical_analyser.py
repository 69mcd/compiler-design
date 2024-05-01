import re

# Define token types using regular expressions
TOKEN_TYPES = [
    ('NUMBER', r'\d+'),
    ('PLUS', r'\+'),
    ('MINUS', r'\-'),
    ('TIMES', r'\*'),
    ('DIVIDE', r'\/'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('WHITESPACE', r'\s+')
]


# Lexical analyzer function
def lexer(input_string):
    tokens = []
    pos = 0

    while pos < len(input_string):
        match = None
        for token_type, pattern in TOKEN_TYPES:
            regex = re.compile(pattern)
            match = regex.match(input_string, pos)
            if match:
                value = match.group(0)
                if token_type != 'WHITESPACE':
                    tokens.append((token_type, value))
                break
        if not match:
            raise Exception('Illegal character: %s' % input_string[pos])
        else:
            pos = match.end(0)

    return tokens


# Test the lexer
input_string = "3 + 4 * (5 - 2)"
tokens = lexer(input_string)
for token in tokens:
    print(token)
