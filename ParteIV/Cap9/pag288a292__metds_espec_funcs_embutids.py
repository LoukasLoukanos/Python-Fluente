from array import array
import math


class Vector2d:
    typecode = 'd'  # atributo de classe para converter instâncias da classe para de bytes em __bytes__

    def __init__(self, x, y): # converte os argumentos para float ao serem passados como argumentos inválidos (int nesse caso), previnindo erros...
        self.x = float(x)
        self.y = float(y)

    def __iter__(self): # torna a classe um iterável, ou seja, um vetor (iterável → possibilita o desempacotamento, ex: x, y = my_obj
        return (i for i in (self.x, self.y))  

    def __repr__(self): # Devolve uma string que representa o objeto como o DESENVOLVEDOR quer vê-lo
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)  # cria uma string para o DESENVOLVEDOR interpolando os componentes com {!r} para obter sua repr; como a classe é iterável (graças a __iter__), *self alimenta format com os componentes x e y

    def __str__(self): # Devolve uma string que representa o objeto como o USUÁRIO quer vê-lo
        return str(tuple(self))  # a partir da classe iterável (graças a __iter__), cria uma tupla a ser exibida como um par ordenado para o USUÁRIO

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +  # para gerar bytes, convertemos o bytecode para bytes e concatenamos
                bytes(array(self.typecode, self)))  # bytes convertidos a partir de um array criado por iteração na instância

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)  # magnitude = hipotenusa do triângulo formado pelos componentes-catetos x e y

    def __bool__(self):
        return bool(abs(self))  # usa abs para retornar se há magnitude; 0.0 é False, valores diferentes de zero é True

# emprego de __init__
v1 = Vector2d(3, 4) # cria o objeto v1 iterável, ou seja, o vetor v1 (iterável → possibilita o desempacotamento, ex: x, y = my_obj)
print(v1.x, v1.y)  # os componentes do vetor podem ser acessados diretamente como atributos, sem chamadas à metodos getter
#output: 3.0 4.0

# emprego de __iter__
x, y = v1  # o objeto vetor v1 é herdou da classe a implementação para ser iterável (iterável → possibilita o desempacotamento, ex: x, y = my_obj)
x, y
#output: (3.0, 4.0)

# emprego de __repr__
v1  # __repr__ Devolve uma string que representa o objeto como o DESENVOLVEDOR quer vê-lo
#output:Vector2d(3.0, 4.0)

# emprego de __str__
print(v1)  #__str__ Devolve uma string que representa o objeto como o USUÁRIO quer vê-lo
#output:(3.0, 4.0)

# emprego de __bytes__
octets = bytes(v1)  # a função embutida bytes, usa o método especial __bytes__ para gerar uma representação binária
#return →  b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'

# emprego de __eq__
v1_clone = eval(repr(v1))  # a cópia v1_clone, de v1, mostra que repr é uma representação fiel da chamada ao seu construtor↓
v1 == v1_clone 
#return →  True

# emprego de __abs__
abs(v1)  # a função embutida abs, usa o método especial __abs__ para devolver a magnitude do vetor (magnitude = hipotenusa do triângulo formado pelos componentes-catetos x e y)
#return →  5.0

# emprego de __bool__
bool(v1), bool(Vector2d(0, 0))  # a função embutida bool, usa o método especial __bool__ para devolver False para vetores de magnitude zero ou True, caso contrário
#return →  (True, False)
