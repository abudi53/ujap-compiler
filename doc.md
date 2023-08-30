
### Tokens

#### Identificadores: 
Nombres de las variables, clases, funciones, métodos, etc.

#### Palabras clave: 
Palabra exacta que indíca el comienzo de una definición (`class`, `def`), un modificador (`public`, `private`, `static`, `final`, etc), o estructuras de control de flujo (`while`, `for`, `if`, `else`)

#### Literales: 
Valores definídos por el usuario: `"Hola Mundo"`, `123`, `true`.

#### Separadores y delímitadores:
`:`, `;`, `,`, `()`, `[]`, 

#### Espacios:
Espacios, Tabs, lineas nuevas, etc

#### Comentarios:
En python es `# Este es un comentario`, en Javascipt es `// Este es un comentario`

---
## Documentación de programa

La biblioteca RPLY es una herramienta de análisis léxico y sintáctico escrita en Python. Proporciona una forma sencilla de crear analizadores léxicos y sintácticos para procesar lenguajes formales, como gramáticas y expresiones regulares.

La funcionalidad principal de RPLY se divide en dos partes: el analizador léxico (lexer) y el analizador sintáctico (parser).

El analizador léxico se encarga de dividir el código fuente en elementos más pequeños llamados "tokens". Estos tokens representan unidades léxicas, como palabras clave, identificadores, literales numéricos, operadores, etc. El lexer de RPLY permite definir reglas para reconocer y clasificar estos tokens en base a expresiones regulares.

El analizador sintáctico, también conocido como parser, toma los tokens generados por el lexer y los organiza en una estructura jerárquica que representa la estructura gramatical del código fuente. RPLY soporta diferentes tipos de análisis sintáctico, incluyendo análisis descendente (top-down) y análisis ascendente (bottom-up). Además, permite definir gramáticas utilizando notación de expresiones regulares y gramáticas libres de contexto.

---

La biblioteca RPLY se utiliza en el lexer para crear un analizador léxico personalizado que puede reconocer y clasificar tokens dentro de un código fuente.

Archivo lexer.py:

1. Importación de la biblioteca RPLY:
```python
from rply import LexerGenerator
```
En esta línea, se importa la clase `LexerGenerator` de la biblioteca RPLY. Esta clase se utiliza para generar un analizador léxico.

3. Definición de la clase Lexer:
```python
class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()
```
La clase `Lexer` se define con un método `__init__` que inicializa el objeto `Lexer` y crea una instancia de `LexerGenerator` llamada `lexer`.

6. Método privado `_add_tokens`:
```python
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
```
Este método se encarga de agregar los tokens al analizador léxico. Cada llamada a `self.lexer.add` define un nuevo token con un nombre y una expresión regular que lo representa. Los tokens definidos en este código incluyen:
- 'PRINT': representa la palabra clave "print".
- 'ABRE_PAREN': representa el símbolo "(".
- 'CIERRA_PAREN': representa el símbolo ")".
- 'PUNTO_COMA': representa el símbolo ";".
- 'SUM': representa el operador de suma "+".
- 'SUB': representa el operador de resta "-".
- 'NUMERO': representa un número entero.
Además, se utiliza `self.lexer.ignore` para ignorar los espacios en blanco en el código fuente.

14. Método `get_lexer`:
```python
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
```
Este método llama al método privado `_add_tokens` para agregar los tokens al analizador léxico y luego devuelve el analizador léxico construido utilizando `self.lexer.build()`.

Archivo main.py:

1. Importación del módulo Lexer:
```python
from lexer import Lexer
```
Se importa la clase `Lexer` del archivo lexer.py para utilizarla en el código principal.

4-8. Definición de una cadena de entrada:
```python
input = """
print(4 + 4 - 2);
"""
```
Se define una cadena de entrada que contiene un código fuente de ejemplo.

10. Creación del analizador léxico:
```python
lexer = Lexer().get_lexer()
```
Se crea una instancia de la clase `Lexer` y se llama al método `get_lexer` para obtener el analizador léxico creado.

12. Análisis léxico del código fuente:
```python
tokens = lexer.lex(input)
```
Se utiliza el objeto `lexer` para ejecutar el análisis léxico en la cadena de entrada.

14-16. Iteración sobre los tokens obtenidos:
```python
for token in tokens:
    print(token)
```
Se itera sobre los tokens generados por el analizador léxico y se imprime cada token.


