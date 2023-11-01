from llvmlite import ir

class Numero():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        i = ir.Constant(ir.IntType(8), int(self.value))
        return i

class String():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value
    
    def eval(self):
        str_val = bytearray((self.value + '\00').encode('utf8'))
        i = ir.Constant(ir.ArrayType(ir.IntType(8), len(str_val)), str_val)
        return i

    
class Boolean():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value
    
    def eval(self):
        if self.value == 'true':
            return ir.Constant(ir.IntType(1), 1)
        else:
            return ir.Constant(ir.IntType(1), 0)

class BinaryOp():
    def __init__(self, builder, module, left, right):
        self.builder = builder
        self.module = module
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        return self.builder.add(self.left.eval(), self.right.eval())


class Sub(BinaryOp):
    def eval(self):
        return self.builder.sub(self.left.eval(), self.right.eval())

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
    def __init__(self, builder, module, printf, value):
        self.builder = builder
        self.module = module
        self.printf = printf
        self.value = value

    def eval(self):
        value = self.value.eval()

        # Declare argument list
        voidptr_ty = ir.IntType(8).as_pointer()
        fmt = "%i \n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
                            bytearray(fmt.encode("utf8")))
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr")
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)

        # Call Print Function
        self.builder.call(self.printf, [fmt_arg, value])

class SymbolTable:
    def __init__(self):
        self.symbol_table = {}

    def set(self, name, value):
        self.symbol_table[name] = value

    def get(self, name):
        llvm_value = self.symbol_table.get(name, None)
        if llvm_value is None:
            raise Exception(f"Variable {name} is not defined")
        return llvm_value

symbol_table = SymbolTable()

class VarAssign():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def eval(self, builder, module):
        # Generate LLVM code for the value
        value = self.value.eval(builder, module)

        # Store the value in the symbol table
        symbol_table.set(self.name, value)

        return value
        

class VarReference():
    def __init__(self, name):
        self.name = name

    def eval(self, builder, module):
        # Retrieve the value from the symbol table
        value = symbol_table.get(self.name)

        return value