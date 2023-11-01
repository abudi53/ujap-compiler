from lexer import Lexer
from parser_ujap import Parser
from codegen import CodeGen

input = """
print(4 + 4 - 2);
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(input)

codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf


pg = Parser(module, builder, printf)
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

codegen.create_ir()
codegen.save_ir("output.ll")