"""
Versão aprimorada da classe Vector2d(pág295a298): inclusão dos atributos x e y privados (__x, __y), decorador @property e método especial __hash__, tornando a classe hashable + Exemplo de uso
"""

from array import array
import math

class Vector2d: # aprimoramento do Vector2d da pag295a298 (→ o qual foi aprimorado de pag292à293, aprimorado de pag288a292)
    typecode = 'd'

    """
    Tornar os atributos x e y privados usando dois underscores (__) é uma prática comum para garantir que eles não sejam acessados 
    diretamente fora da classe. Isso é útil não apenas para controlar o acesso aos dados, mas também para tornar a classe hashable.

    Quando uma classe é usada como chave em um conjunto (set) em Python (set → {key:value} → hash[key]=value), ela precisa ser hashable. 
    Para que uma classe seja considerada hashable, ela deve implementar os métodos __hash__() e __eq__(). Se os atributos da classe 
    forem mutáveis, como listas, conjuntos ou dicionários, a classe não poderá ser hashable.

    Ao tornar os atributos x e y privados e controlar o acesso a eles por meio de métodos getters (@property), você pode garantir 
    que esses atributos não sejam modificados fora da classe de uma maneira que comprometa a hashability da instância da classe.
    """
    def __init__(self, x, y):
        self.__x = float(x) # usando dois underscores __ na frente, deixa o atributo x privado
        self.__y = float(y) # atributo y é privado (atributos privados precisam de método getter para acesso)

    """ 
    o decorador @property a seguir é necessário para expor os atributos x e y privados (__x e __y):
    1.→ Os atributos __x e __y são definidos como privados usando dois underscores (__). Isso significa 
    que eles não podem ser acessados diretamente de fora da classe. Portanto, os métodos getter x e y, marcados 
    com @property, são necessários para permitir o acesso controlado a esses atributos de fora da classe.
    2.→ Ao usar métodos getter para acessar os atributos, você pode adicionar lógica adicional, como 
    validações de entrada ou cálculos, se necessário, antes de retornar os valores. Isso garante 
    que o acesso aos atributos seja feito de maneira segura e consistente.
    3.→ Os métodos getter x e y servem como a interface pública para acessar os atributos __x e __y. Usar o decorador 
    @property os marca como propriedades da classe, tornando sua utilização mais intuitiva para os usuários da classe.
    """
    @property
    def x(self):  # Método getter para acessar o atributo privado x.
        return self.__x  # Retorna o valor do atributo privado x.

    @property
    def y(self):  # Método getter para acessar o atributo privado y.
        return self.__y  # Retorna o valor do atributo privado y.

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

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __abs__(self): # ♦coordenadas retângulares (será usado em else em __format__ ↓)
        return math.hypot(self.x, self.y)  # magnitude = hipotenusa do triângulo formado pelos componentes-catetos x e y

    def __bool__(self):
        return bool(abs(self))  # usa abs para retornar se há magnitude; 0.0 é False, valores diferentes de zero é True

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
    
    """
    O decorador @classmethod abaixo indica que esse método é um método de classe, e não um método de instância. Isso significa que o método será associado à classe 
    em vez de ser associado a instâncias individuais da classe. Isso permite que o método acesse e manipule dados da classe, em vez de dados de instância específicos.
    """
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
#output: Vector2d(3.0, 4.0)


# emprego de __str__
print(v1)  #__str__ Devolve uma string que representa o objeto como o USUÁRIO quer vê-lo
#output: (3.0, 4.0)


# emprego de __bytes__
octets = bytes(v1)  # a função embutida bytes, usa o método especial __bytes__ para gerar uma representação binária
##output: b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'


# teste de frombytes()
v1_clone = Vector2d.frombytes(bytes(v1))


# emprego de __eq__
v1 == v1_clone 
##output: True


#Testes de x e y, somente como leitura:
v1.x, v1.y
#output: (3.0, 4.0)
v1.x = 123
'''output:
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
'''


# emprego de __hash__
v1 = Vector2d(3, 4)
v2 = Vector2d(3.1, 4.2)
hash(v1), hash(v2)
#return →  (7, 384307168202284039)
len(set([v1, v2])) # por ser hashable suporta conjunto (set → {key:value} → hash[key]=value)
#output: 2


# emprego de __abs__
abs(v1)  # a função embutida abs, usa o método especial __abs__ para devolver a magnitude do vetor (magnitude = hipotenusa do triângulo formado pelos componentes-catetos x e y)
#output: 5.0


# emprego de __bool__
bool(v1), bool(Vector2d(0, 0))  # a função embutida bool, usa o método especial __bool__ para devolver False para vetores de magnitude zero ou True, caso contrário
#output: (True, False)


# teste de angle()
Vector2d(0, 0).angle()
#output: 0.0
Vector2d(1, 0).angle()
#output: 0.0
epsilon = 10**-8
abs(Vector2d(0, 1).angle() - math.pi/2) < epsilon
#output: True
abs(Vector2d(1, 1).angle() - math.pi/4) < epsilon
#output: True


# emprego de __format__
#Teste da função embutida format() com ♦coordenadas cartesianas:
format(v1) # a formatação é default: format(v1, fmt_spec=''), portanto não termina com 'p': → entra em else de __format__
#output: '(3.0, 4.0)'
format(v1, '.2f') # a formatação não termina com 'p': → entra em else de __format__
#output: '(3.00, 4.00)'
format(v1, '.3e') # a formatação não termina com 'p': → entra em else de __format__
#output: '(3.000e+00, 4.000e+00)'

#Teste da função embutida format() com ♦coordenadas polares:
format(Vector2d(1, 1), 'p')  # a formatação termina com 'p': → entra em if de __format__
#output: '<1.414213..., 0.785398...>'
format(Vector2d(1, 1), '.3ep') # a formatação termina com 'p': → entra em if de __format__
#output: '<1.414e+00, 7.854e-01>'
format(Vector2d(1, 1), '0.5fp') # a formatação termina com 'p': → entra em if de __format__
#output: '<1.41421, 0.78540>'
