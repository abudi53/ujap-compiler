from lexer import Lexer

input = """
print(4 + 4 - 2);
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(input)

for token in tokens:
    print(token)