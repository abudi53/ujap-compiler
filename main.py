from lexer import Lexer
from parser_ujap import Parser

input = """
print(4 + 4 - 2)
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()