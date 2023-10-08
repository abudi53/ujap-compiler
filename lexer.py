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
        # Strings
        self.lexer.add('STRING', r'\".*?\"')
        # Corchetes
        self.lexer.add('ABRE_CORCHETE', r'\[')
        self.lexer.add('CIERRA_CORCHETE', r'\]')
        # Coma
        self.lexer.add('COMA', r'\,')
        # Llaves
        self.lexer.add('ABRE_LLAVE', r'\{')
        self.lexer.add('CIERRA_LLAVE', r'\}')
        # Asignacion
        self.lexer.add('ASIGNACION', r'\=')
        # Identificador
        self.lexer.add('IDENTIFICADOR', r'[a-zA-Z_][a-zA-Z0-9_]*')
        # Comentario
        self.lexer.add('COMENTARIO', r'\#.*')
        # Operadores logicos
        self.lexer.add('MAYOR_QUE', r'\>')
        self.lexer.add('MENOR_QUE', r'\<')
        self.lexer.add('MAYOR_IGUAL', r'\>\=')
        self.lexer.add('MENOR_IGUAL', r'\<\=')
        self.lexer.add('IGUAL', r'\=\=')
        self.lexer.add('DIFERENTE', r'\!\=')
        self.lexer.add('AND', r'\&\&')
        self.lexer.add('OR', r'\|\|')
        self.lexer.add('NOT', r'\!')
        # Booleanos
        self.lexer.add('TRUE', r'true')
        self.lexer.add('FALSE', r'false')
        # Ignorar espacios
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()