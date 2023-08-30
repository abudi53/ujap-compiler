from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'print')
        # Parentesis
        self.lexer.add('ABRE_PAREN', r'\(')
        self.lexer.add('CIERRA_PAREN', r'\)')
        # Punto y coma
        self.lexer.add('PUNTO_COMA', r'\;')
        # Operadores
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        # Numeros
        self.lexer.add('NUMERO', r'\d+')
        # Ignorar espacios
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()