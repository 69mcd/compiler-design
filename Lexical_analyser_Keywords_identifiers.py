import re

class LexicalAnalyzer:
    def __init__(self):
        self.keywords = {
            'if', 'else', 'while', 'for', 'int', 'float', 'return'  # Add more keywords as needed
        }

    def analyze(self, input_text):
        tokens = []
        lines = input_text.split('\n')
        for line_number, line in enumerate(lines, start=1):
            line = line.strip()
            if not line:
                continue
            current_token = ''
            for char in line:
                if char.isalnum() or char == '_':
                    current_token += char
                else:
                    if current_token:
                        if current_token in self.keywords:
                            tokens.append(('keyword', current_token, line_number))
                        else:
                            tokens.append(('identifier', current_token, line_number))
                        current_token = ''
                    if char != ' ':
                        tokens.append(('symbol', char, line_number))
            if current_token:
                if current_token in self.keywords:
                    tokens.append(('keyword', current_token, line_number))
                else:
                    tokens.append(('identifier', current_token, line_number))
        return tokens

# Example usage
lexer = LexicalAnalyzer()
input_text = """
int main() {
    int x = 10;
    if (x > 5) {
        return 1;
    } else {
        return 0;
    }
}
"""
tokens = lexer.analyze(input_text)
for token_type, token_value, line_number in tokens:
    print(f"Token type: {token_type}, Token value: {token_value}, Line number: {line_number}")
