
from rply import ParserGenerator
from ast_ujap import *


class Parser():
    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMERO', 'PRINT', 'ABRE_PAREN', 'CIERRA_PAREN',
             'PUNTO_COMA', 'SUM', 'SUB', 'STRING', 'ABRE_CORCHETE', 'CIERRA_CORCHETE', 
             'COMA', 'ABRE_LLAVE', 'CIERRA_LLAVE', 'ASIGNACION', 'IDENTIFICADOR', 
             'COMENTARIO', 'MAYOR_QUE', 'MENOR_QUE', 'MAYOR_IGUAL', 'MENOR_IGUAL',
             'IGUAL', 'DIFERENTE', 'AND', 'OR', 'NOT', 'TRUE', 'FALSE']
        )

        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):
        @self.pg.production('program : PRINT ABRE_PAREN expression CIERRA_PAREN PUNTO_COMA')
        def program(p):
            return Print(self.builder, self.module, self.printf, p[2])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression AND expression')
        @self.pg.production('expression : expression OR expression')
        @self.pg.production('expression : NOT expression')
        @self.pg.production('expression : expression IGUAL expression')
        @self.pg.production('expression : expression DIFERENTE expression')
        @self.pg.production('expression : expression MAYOR_QUE expression')
        @self.pg.production('expression : expression MENOR_QUE expression')
        @self.pg.production('expression : expression MAYOR_IGUAL expression')
        @self.pg.production('expression : expression MENOR_IGUAL expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'AND':
                return And(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'OR':
                return Or(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'NOT':
                return Not(self.builder, self.module, left)
            elif operator.gettokentype() == 'IGUAL':
                return Igual(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'DIFERENTE':
                return Diferente(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'MAYOR_QUE':
                return Mayor_que(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'MENOR_QUE':
                return Menor_que(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'MAYOR_IGUAL':
                return Mayor_igual(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'MENOR_IGUAL':
                return Menor_igual(self.builder, self.module, left, right)
            

        @self.pg.production('expression : NUMERO')
        def number(p):
            return Numero(self.builder, self.module, p[0].value)
        
        @self.pg.production('expression : STRING')
        def string(p):
            return String(self.builder, self.module, p[0].value)
        
        @self.pg.production('expression : TRUE')
        def true(p):
            return Boolean(self.builder, self.module, p[0].value)
        
        @self.pg.production('expression : FALSE')
        def false(p):
            return Boolean(self.builder, self.module, p[0].value)
        
        @self.pg.production('expression : IDENTIFICADOR ASIGNACION expression')
        def statement(p):
            # builder = ir.IRBuilder()
            # module = ir.Module()
            return VarAssign(p[0].getstr(), p[2])
            # var_assign.eval(builder, module)


        @self.pg.production('expression : ABRE_PAREN expression CIERRA_PAREN')
        def expression(p):
            return p[1]
        
        @self.pg.production('expression : IDENTIFICADOR')
        def expression(p):
            return VarReference(p[0].getstr())
        
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()