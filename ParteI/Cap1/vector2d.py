from audioop import add, mul
from ctypes.wintypes import PINT
from math import hypot
from pickle import TRUE

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%s, %s)' % (self.x, self.y)

    #método abs para calcular a magnitude("hipotenusa") de um vetor bidimencional (x, y)
    def __abs__(self):
        return hypot(self.x, self.y) #>>> hypot(3.0, 4.0) → hp=5.0

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v = Vector(3, 4)
repr_ = repr(v)
print("__repr__:", repr_)

abs_ = abs(v)
print("__abs__:", abs_)

boll_ = bool(v)
print("__boll__:", boll_)

add_ = add(v, 5)
print("__add__:", add_)#TypeError: add expected 3 arguments, got 2 ???????????????

mul_ = mul(v, 5)
print("__mul__:", mul_)#TypeError: add expected 3 arguments, got 2 ???????????????