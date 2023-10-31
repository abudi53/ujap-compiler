class Numero():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)

class String():
    def __init__(self, value):
        self.value = value
    
    def eval(self):
        return self.value[1:-1]
    
class Boolean():
    def __init__(self, value):
        self.value = value
    
    def eval(self):
        if self.value == 'true':
            return True
        else:
            return False

class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class And(BinaryOp):
    def eval(self):
        return self.left.eval() and self.right.eval()
    
class Or(BinaryOp):
    def eval(self):
        return self.left.eval() or self.right.eval()

class Not(BinaryOp):
    def eval(self):
        return not self.left.eval()

class Igual(BinaryOp):
    def eval(self):
        return self.left.eval() == self.right.eval()

class Diferente(BinaryOp):
    def eval(self):
        return self.left.eval() != self.right.eval()

class Mayor_que(BinaryOp):
    def eval(self):
        return self.left.eval() > self.right.eval()

class Menor_que(BinaryOp):
    def eval(self):
        return self.left.eval() < self.right.eval()

class Mayor_igual(BinaryOp):
    def eval(self):
        return self.left.eval() >= self.right.eval()

class Menor_igual(BinaryOp):
    def eval(self):
        return self.left.eval() <= self.right.eval()


class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())

class SymbolTable:
    def __init__(self):
        self.symbol_table = {}

    def set(self, name, value):
        self.symbol_table[name] = value

    def get(self, name):
        return self.symbol_table.get(name, None)

symbol_table = SymbolTable()

class VarAssign():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def eval(self):
        value = self.value.eval()
        symbol_table.set(self.name, value)
        return value
        

class VarReference():
    def __init__(self, name):
        self.name = name

    def eval(self):
        value = symbol_table.get(self.name)
        if value is None:
            raise Exception(f"Variable {self.name} is not defined")
        return value