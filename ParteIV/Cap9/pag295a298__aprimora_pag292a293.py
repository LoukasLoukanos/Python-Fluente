"""
Versão aprimorada da classe Vector2d(pág292a293): INCLUSÃO DO MÉTODO ESPECIAL __format__(linha40) + EXEMPLO DE USO(linha112)
"""

from array import array
import math


class Vector2d: # aprimoramento do Vector2d da pag292à293 (→ o qual foi aprimorado de pag288a292)
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

    def __abs__(self): # ♦coordenadas retângulares (será usado em else em __format__ ↓)
        return math.hypot(self.x, self.y)  # magnitude = hipotenusa do triângulo formado pelos componentes-catetos x e y

    def __bool__(self):
        return bool(abs(self))  # usa abs para retornar se há magnitude; 0.0 é False, valores diferentes de zero é True
    

    #begin:↓=======INCLUSÃO DO MÉTODO ESPECIAL __format__=================================================
    def angle(self): # ♦coordenadas polares (será usado em if em __format__ ↓)
        return math.atan2(self.y, self.x) # ângulo da magnitude (= hipotenusa, em __abs__↑)

    def __format__(self, fmt_spec=''): #sintaxe: format(obj, especificadorDeFormatação)   →ou→   'str {field_name:especificadorDeFormatação} str'.format(field_name=obj)
        # caso a formatação terminar com 'p': use ♦coordenadas polares (angle):
        if fmt_spec.endswith('p'): 
            fmt_spec = fmt_spec[:-1] # remove o sufixo 'p' de fmt_spec
            coords = (abs(self), self.angle()) # cria tuple de coordenadas polares: (magnitude, angle)
            outer_fmt = '<{}, {}>' # configura a formatação exterma delimitada por sinais de menor e de maior
        
        # caso a formatação não terminar com 'p': use ♦coordenadas retângulares (__abs__):
        else:
            coords = self # usa componentes de x, y de self para coordenadas retangulares
            outer_fmt = '({}, {})' # configura a formatação externa com parênteses
        
        components = (format(c, fmt_spec) for c in coords) # gera iterável com componentes como srings formatadas
        return outer_fmt.format(*components) # insere strings formatadas na formatação externa
    
    #begin:↑=======INCLUSÃO DO MÉTODO ESPECIAL __format__=================================================

    
    """O decorador @classmethod indica que esse método é um método de classe, e não um método de instância. Isso significa que o método será associado à classe 
    em vez de ser associado a instâncias individuais da classe. Isso permite que o método acesse e manipule dados da classe, em vez de dados de instância específicos."""
    @classmethod # o decorador classmethod define que o método frozembytes será um método de classe
    def frombytes(cls, octets):  # não há argumento self, em vez disso a própria classe é passada como cls
        typecode = chr(octets[0])  # lê o typecode no primeiro byte
        memv = memoryview(octets[1:]).cast(typecode)  # cria uma memoryview a partir da sequência binária octets e usa o typecode para fazer o cast dos dados →obs: sobre "Memory Views", ver pág.78...
        return cls(*memv)  # desempacota a memoryview resultante do cast, produzindo o par de argumentos necessário ao construtor.


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

v1_clone = Vector2d.frombytes(bytes(v1))

# emprego de __repr__
v1_clone  # __repr__ Devolve uma string que representa o objeto como o DESENVOLVEDOR quer vê-lo
#output:Vector2d(3.0, 4.0)

# emprego de __eq__
v1 == v1_clone 
#return →  True

# emprego de __abs__
abs(v1)  # a função embutida abs, usa o método especial __abs__ para devolver a magnitude do vetor (magnitude = hipotenusa do triângulo formado pelos componentes-catetos x e y)
#return →  5.0

# emprego de __bool__
bool(v1), bool(Vector2d(0, 0))  # a função embutida bool, usa o método especial __bool__ para devolver False para vetores de magnitude zero ou True, caso contrário
#return →  (True, False)


#begin:↓=======EXEMPLO DE USO DO MÉTODO ESPECIAL __format__=====================

#Teste da função embutida format() com ♦coordenadas cartesianas:
format(v1) # a formatação é default: format(v1, fmt_spec=''), portanto não termina com 'p': → entra em else de __format__
#return →  '(3.0, 4.0)'
format(v1, '.2f') # a formatação não termina com 'p': → entra em else de __format__
#return →  '(3.00, 4.00)'
format(v1, '.3e') # a formatação não termina com 'p': → entra em else de __format__
#return →  '(3.000e+00, 4.000e+00)'


#Teste do método angle():
Vector2d(0, 0).angle()
#return →  0.0
Vector2d(1, 0).angle()
#return →  0.0
epsilon = 10**-8
abs(Vector2d(0, 1).angle() - math.pi/2) < epsilon
#return →  True
abs(Vector2d(1, 1).angle() - math.pi/4) < epsilon
#return →  True


#Teste da função embutida format() com ♦coordenadas polares:
format(Vector2d(1, 1), 'p')  # a formatação termina com 'p': → entra em if de __format__
#return →  '<1.414213..., 0.785398...>'
format(Vector2d(1, 1), '.3ep') # a formatação termina com 'p': → entra em if de __format__
#return →  '<1.414e+00, 7.854e-01>'
format(Vector2d(1, 1), '0.5fp') # a formatação termina com 'p': → entra em if de __format__
#return →  '<1.41421, 0.78540>'

#begin:↑=======EXEMPLO DE USO DO MÉTODO ESPECIAL __format__=====================
