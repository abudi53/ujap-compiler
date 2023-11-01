
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

Se generara codigo LLVM a partir de un codigo fuente escrito en un lenguaje de programacion creado por nosotros, el cual sera un lenguaje imperativo, con variables, funciones, ciclos, condicionales, etc.

Luego se generara un ejecutable a partir del codigo LLVM generado.

---

La biblioteca RPLY se utiliza en el lexer para crear un analizador léxico personalizado que puede reconocer y clasificar tokens dentro de un código fuente.

# Uso del compilador:

1. Instalar las dependencias: llvmlite, rply.
2. Añadir una expresion en la variable input del archivo main.py.
3. Ejecutar el archivo main.py.
4. Se compila el archivo obtenido en el terminal con:
```
$ llc -filetype=obj output.ll 
$ gcc -no-pie output.o -o output
```
5. Se ejecuta el archivo compilado:
```
$ ./output
```

## Archivo lexer.py:

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
- 'STRING': representa una cadena de caracteres.
- 'ABRE_CORCHETE': representa el símbolo "[".
- 'CIERRA_CORCHETE': representa el símbolo "]".
- 'COMA': representa el símbolo ",".
- 'ABRE_LLAVE': representa el símbolo "{".
- 'CIERRA_LLAVE': representa el símbolo "}".
- 'ASIGNACION': representa el operador de asignación "=".
- 'IDENTIFICADOR': representa un identificador.
- 'COMENTARIO': representa un comentario.
- 'OPERADORES LOGICOS': Mayor que, menor que, mayor o igual que, menor o igual que, igual que, diferente que, and &&, or || , not !.
- 'BOOLEANOS': true, false.

Además, se utiliza `self.lexer.ignore` para ignorar los espacios en blanco en el código fuente.

14. Método `get_lexer`:
```python
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
```
Este método llama al método privado `_add_tokens` para agregar los tokens al analizador léxico y luego devuelve el analizador léxico construido utilizando `self.lexer.build()`.


## Archivo parser_ujap.py: 

Importación de Módulos:

```python
from rply import ParserGenerator
from ast_ujap import *
```
En estas líneas, se importa la clase ParserGenerator de la biblioteca RPLY y algunas clases (como Print, Sum, Sub, etc.) del módulo ast_ujap. Estas clases se utilizan para construir el AST.>

```
__init__(self, module, builder, printf)
```
Este es el constructor de la clase. Toma tres argumentos: module, builder, y printf. Estos argumentos son necesarios para la generación de código LLVM. module representa el módulo LLVM en el que se generará el código, builder es el generador de código LLVM y printf es una función que permite imprimir valores en la salida estándar.

```
parse(self)
```
Este método se encarga de definir las reglas gramaticales del lenguaje y las producciones del analizador sintáctico. Se utilizan decoradores para definir las reglas gramaticales en términos de producciones. Cada producción especifica cómo se debe construir el AST para una estructura particular del lenguaje.

```
get_parser(self)
```
Este método devuelve el analizador sintáctico construido a partir de las reglas definidas. El analizador sintáctico es necesario para analizar el código fuente y generar el AST.

#### Producciones:
Las producciones se definen utilizando decoradores y siguen la notación BNF (Forma Normal de Backus-Naur). Cada producción define cómo se debe construir una parte específica del AST. Algunos ejemplos de producciones incluyen:

```
@self.pg.production('program : PRINT ABRE_PAREN expression CIERRA_PAREN PUNTO_COMA')
```
Esta producción define cómo se debe construir un nodo Print en el AST cuando se encuentra una declaración de impresión en el código fuente.

```
@self.pg.production('expression : expression SUM expression')
```
Esta producción define cómo se debe construir un nodo Sum en el AST cuando se encuentra una expresión de suma.

```
@self.pg.production('expression : NUMERO')
```
Esta producción define cómo se debe construir un nodo Numero en el AST cuando se encuentra un número en el código fuente.

```
@self.pg.production('expression : IDENTIFICADOR ASIGNACION expression')
```
Esta producción define cómo se debe construir un nodo VarAssign en el AST cuando se encuentra una asignación de variable.

Cada producción especifica cómo se deben combinar los elementos del lenguaje para construir un nodo en el AST.

#### Manejo de Errores:
En caso de encontrar un token inesperado que no coincide con ninguna de las producciones definidas, se lanza una excepción de tipo ValueError. Esto se hace en el método error_handle.

## Archivo ast_ujap.py:


Este código define una serie de clases y una tabla de símbolos utilizadas para la generación de código LLVM a partir del árbol de sintaxis abstracta (AST) creado por el analizador sintáctico. El código está diseñado para procesar expresiones y declaraciones de un lenguaje de programación personalizado. A continuación, se explican las partes más importantes del código:

### Clase Numero:

Esta clase representa un nodo en el AST que almacena un valor numérico.
El constructor (__init__) toma tres argumentos: builder, module y value. builder y module son objetos de LLVM que se utilizan para generar código LLVM. value es el valor numérico.
El método eval genera un valor entero LLVM constante a partir del valor numérico y lo devuelve.
### Clase String:

Esta clase representa un nodo en el AST que almacena una cadena de caracteres.
El constructor toma tres argumentos al igual que la clase Numero.
El método eval convierte la cadena de caracteres en una representación LLVM y la devuelve.
### Clase Boolean:

Esta clase representa un nodo en el AST que almacena un valor booleano (true o false).
El constructor toma tres argumentos al igual que las clases anteriores.
El método eval verifica el valor y genera una constante LLVM entera (1 para true y 0 para false) y la devuelve.
### Clases para Operaciones Binarias:

Estas clases (Sum, Sub, And, Or, Not, Igual, Diferente, Mayor_que, Menor_que, Mayor_igual y Menor_igual) representan operaciones binarias en el AST. Cada una de estas clases hereda de BinaryOp y tiene un método eval que aplica la operación correspondiente a los valores izquierdo y derecho y devuelve el resultado.
### Clase Print:

Esta clase representa un nodo en el AST que imprime un valor en la salida estándar.
El constructor toma cuatro argumentos: builder, module, printf y value. builder y module son objetos de LLVM utilizados para generar código, printf es una función que permite imprimir valores, y value es el valor que se imprimirá.
El método eval genera el código necesario para imprimir el valor utilizando la función printf.
### Clase SymbolTable:

Esta clase se utiliza para mantener un seguimiento de las variables definidas en el código y sus valores en LLVM.
El método set agrega una variable y su valor a la tabla de símbolos.
El método get recupera el valor de una variable de la tabla de símbolos.
### Clase VarAssign:

Esta clase representa una asignación de variable en el AST.
El constructor toma dos argumentos: name (el nombre de la variable) y value (el valor que se le asigna).
El método eval genera código LLVM para el valor y lo almacena en la tabla de símbolos con el nombre especificado.
### Clase VarReference:

Esta clase representa una referencia a una variable en el AST.
El constructor toma un argumento: name (el nombre de la variable).
El método eval recupera el valor de la variable desde la tabla de símbolos.

## Archivo codegen.py:

Este programa se encarga de generar código LLVM y compilarlo utilizando la biblioteca llvmlite. A continuación, se describen las partes clave de este código:

### Clase CodeGen:

Esta clase se utiliza para generar y compilar código LLVM.
### Método __init__:

El constructor de la clase inicializa varias configuraciones de LLVM, crea un motor de ejecución (execution engine), declara la función printf y configura el módulo LLVM.
### Método _config_llvm:

Este método configura LLVM y crea un módulo vacío con una función base llamada "main". La función base no toma argumentos y no devuelve ningún valor.
### Método _create_execution_engine:

Este método crea un motor de ejecución adecuado para la generación de código JIT (Just-In-Time) en la CPU del host. El motor es reutilizable para un número arbitrario de módulos.
Se crea una instancia de la clase Target y se utiliza para crear una máquina de destino (target machine).
Luego se crea un motor de ejecución (execution engine) con un módulo LLVM vacío y la máquina de destino.
### Método _declare_print_function:

Este método declara la función printf, que se utiliza para imprimir valores en la salida estándar.
Se define el tipo de la función printf y se declara en el módulo.
### Método _compile_ir:

Este método compila el código LLVM generado. Primero, genera una representación en cadena del módulo LLVM. Luego, crea un objeto de módulo LLVM a partir de la representación en cadena.
Se verifican las propiedades del módulo y se agrega al motor de ejecución (execution engine).
Finalmente, se ejecutan los constructores estáticos y se devuelve el módulo compilado.
### Método create_ir:

Este método llama al método _compile_ir para compilar el código LLVM. Sin embargo, no se almacena el módulo compilado ni se realiza ninguna acción adicional.
### Método save_ir:

Este método toma un nombre de archivo como argumento y guarda el código LLVM generado en ese archivo en formato de texto.

## Archivo main.py:

1. Se importan las clases Lexer, Parser y CodeGen de sus respectivos módulos.

2. Se define una cadena llamada input que contiene el código fuente a analizar y compilar. En este caso, el código fuente es un ejemplo que imprime una expresión matemática.

3. Se crea una instancia del analizador léxico (Lexer) llamada lexer.

4. Se utiliza el analizador léxico para analizar la cadena de entrada input y obtener una secuencia de tokens. Los tokens se almacenan en la variable tokens.

5. Se crea una instancia de la clase CodeGen llamada codegen. Esto inicializa y configura el entorno de generación de código LLVM.

6. Se obtienen referencias al módulo LLVM, el generador de código (builder) y la función printf desde el objeto codegen.

7. Se crea una instancia del analizador sintáctico (Parser) llamada pg. Se le pasan el módulo, el generador de código y printf como argumentos.

8. Se llama al método parse en el objeto pg, que define las reglas de análisis sintáctico.

9. Se obtiene el parser creado llamando al método get_parser en el objeto pg.

10. Se llama al método parse en el parser creado, pasando la secuencia de tokens (tokens). Este paso inicia el proceso de análisis sintáctico y construcción del árbol de sintaxis abstracta (AST).

11. Una vez que se ha analizado y construido el AST, se llama al método eval en el resultado del análisis sintáctico. Esto inicia la generación de código LLVM a partir del AST.

12. Se llama al método create_ir en el objeto codegen para compilar el código LLVM generado.

13. Finalmente, se llama al método save_ir en el objeto codegen para guardar el código LLVM compilado en un archivo llamado "output.ll".