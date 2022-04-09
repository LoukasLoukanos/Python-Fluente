from audioop import add, mul
from ctypes.wintypes import PINT
from math import hypot
from pickle import TRUE

class Vector:

    #método inicializador(construtor em Java)...
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #método especial __repr__ é chamado pela função embutida repr para obtermos a representação em string do objeto para inspeção.
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)#string → Vector(x, y)

    #método especial __abs__ é chamado pela função embutida abs para calcular a magnitude("hipotenusa") de um vetor bidimencional (x, y).
    def __abs__(self):
        return hypot(self.x, self.y) #>>> hypot(3.0, 4.0) → hp=5.0

    #método especial __bool__ é chamado pela função embutida bool e implementa bool para retornar o cálculo da magnitude, 
    #implementado pela função embutida abs, e por padrão bool retorna False se a magnitude do vetor for zero e True, caso contrário.
    #A magnitude implementada lepo método especial __abs__ foi convertida em um valor booleano pela função embutida bool.
    def __bool__(self):#o parâmetro deve ser um vetor com dois valores
        return bool(abs(self))

    #novos objetos são criados e os operandos (self e other) não são alterados.
    def __add__(self, other):
        return Vector(self.x + other, self.y + other)

    #novos objetos são criados e os operandos (self e scalar) não são alterados.
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v = Vector(3, 4)
repr_ = repr(v)
print("do método especial __repr__:", repr_)

abs_ = abs(v)
print("do método especial __abs__:", abs_)

boll_ = bool(v)
print("do método especial __boll__:", boll_)

add_ = add(v, 2)
print("do método especial __add__:", add_)#TypeError: add expected 3 arguments, got 2 ???????????????

mul_ = mul(v, 6)
print("do método especial __mul__:", mul_)#TypeError: add expected 3 arguments, got 2 ???????????????
