## **Pág. 29............Um baralho pythônico**
<details>
<summary></📖></summary>

### ***Um barallho como uma sequência de cartas:***
```python
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


#_________EXEMPLOS_________
#from frenchdeck import FrenchDeck, Card

beer_card = Card('7', 'diamonds')
#output: Card(rank='7', suit='diamonds')

deck = FrenchDeck()
len(deck)
#output: 52

deck[:3]
#output: [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]

deck[12::13]
#output:[Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

Card('Q', 'hearts') in deck
#output: True

Card('Z', 'clubs') in deck
#output: False

for card in deck:
    pass
'''
 output:
 Card(rank='2', suit='spades')
 Card(rank='3', suit='spades')
 Card(rank='4', suit='spades')
'''

for card in reversed(deck):
    pass
'''
 output:
 Card(rank='A', suit='hearts')
 Card(rank='K', suit='hearts')
 Card(rank='Q', suit='hearts')
'''

for n, card in enumerate(deck, 1):
    pass
'''
 output:
 1 Card(rank='2', suit='spades')
 2 Card(rank='3', suit='spades')
 3 Card(rank='4', suit='spades')
'''

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

spades_high(Card('2', 'clubs'))
#output: 0

spades_high(Card('A', 'spades'))
#output: 51

for card in sorted(deck, key=spades_high):
    pass
'''
 output:
 Card(rank='2', suit='clubs')
 Card(rank='2', suit='diamonds')
 Card(rank='2', suit='hearts')
 ...
 Card(rank='A', suit='diamonds')
 Card(rank='A', suit='hearts')
 Card(rank='A', suit='spades')
'''

```

</details>
</br>


## **Pág. 33............Como os métodos especiais são usados**
<details>
<summary></📖></summary>
 - Ao implementar os métodos especiais _len__ e _getitem__ nos beneficiamos de recursos especiais da linguagem (neste caso iteração e fatiamento) e da biblioteca padrao(random.choice, reversed e sorted). Graças à composição as implementações de _len__ e _getitem__ podem passar todo o trabalho para os objetos

</details>
</br>


## **Pág. 34............Emulando tipos numéricos**
<details>
<summary></📖></summary>

### ***Uma classe simples de vetor bidimencional:***
```python
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
print("do método especial __bool__:", boll_)

add_ = v + 2
print("do método especial __add__:", add_)

mul_ = v * 6
print("do método especial __mul__:", mul_)

'''output:
do método especial __repr__: Vector(3, 4)
do método especial __abs__: 5.0
do método especial __bool__: True
do método especial __add__: Vector(5, 6)
do método especial __mul__: Vector(18, 24)
'''

```

</details>
</br>


## **Pág. 36............Representação em string**
<details>
<summary></📖></summary>

A representação em string de um objeto é definida pelo método especial __repr__. Esse método é responsável por retornar uma string que representa o objeto de forma legível. É comum usar o __repr__ para fornecer informações sobre o estado interno do objeto, o que facilita a depuração e a compreensão do objeto durante o 

### ***Representação em string de repr:***
```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __repr__(self):
        return f"Pessoa(nome={self.nome}, idade={self.idade})"

p = Pessoa("João", 25)
print(p)  # Saída: Pessoa(nome=João, idade=25)

```

</details>
</br>


## **Pág. 37............Operadores aritméticos**
<details>
<summary></📖></summary>

Os operadores aritméticos podem ser personalizados para um objeto por meio dos métodos especiais __add__ e __mul__. O __add__ permite que um objeto seja somado a outro objeto usando o operador +, enquanto o __mul__ permite multiplicar o objeto por um valor usando o operador *. Esses métodos permitem que você defina o comportamento dos operadores aritméticos para seus objetos personalizados.

### ***Operadores aritméticos com add e mul:***
```python
class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y)
    
    def __mul__(self, escalar):
        return Vetor(self.x * escalar, self.y * escalar)

v1 = Vetor(2, 3)
v2 = Vetor(1, -2)
resultado_soma = v1 + v2
resultado_multiplicacao = v1 * 2
print(resultado_soma.x, resultado_soma.y)  # Saída: 3, 1
print(resultado_multiplicacao.x, resultado_multiplicacao.y)  # Saída: 4, 6

```

</details>
</br>


## **Pág. 37............Valor booleano de um tipo definido pelo usuário**
<details>
<summary></📖></summary>

O método especial __bool__ permite definir o valor booleano de um objeto definido pelo usuário. Ao implementar esse método, você pode especificar quando um objeto deve ser considerado verdadeiro (True) ou falso (False). Isso é útil em situações em que você deseja que um objeto personalizado seja avaliado em uma expressão booleana, como em um if ou em um contexto de condicional.

### ***Valor booleano de um tipo definido pelo usuário com bool:***
```python
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def __bool__(self):
        return self.titulo != ""
    
livro_valido = Livro("Aventuras Fantásticas", "João Silva")
livro_invalido = Livro("", "Maria Souza")
print(bool(livro_valido))  # Saída: True
print(bool(livro_invalido))  # Saída: False

```

</details>
</br>


## **Pág. 39............Visão geral dos métodos especiais**
<details>
<summary></📖></summary>

### ***Nomes dos métodos especiais (não inclui operadores)***
| Categoria | Nomes dos métodos |
|:-:|:-:|
| Representação em string/bytes | __ repr __ , __ str __ , __ format __ , __ bytes __ |
| Conversão para número | __ abs __ , __ bool __ , __ complex __ , __ int __ , __ float , __ hash __ , __ index __ |
| Emulação de coleções | __ len __ , __ getiten __ , __ setiten __ , __ deliten __ , __ contains __ |
| Iteração | __ iter __ , __ reversed __ , __ next __ |
| Emulação de invocáveis | __ call __ |
| Gerenciamento de contexto | __ enter __ , __ exit __ |
| Criação e destruição de instâncias | __ new __ , __ init __ , __ del __ |
| Gerenciamento de atributos | __ getattr __ , __ getattribute __ , __ setattr __ , __ delattr __ , __ dir __ |
| Descritores de atributos | __ get __ , __ set __ , __ delete __ |
| Serviços de classes | __ prepare __ , __ instancecheck __ , __ subclasscheck __ |

### ***Nomes dos métodos especiais para operadores***
| Categoria | Nomes dos métodos e operadores relacionados |
|:-:|:-:|
| Operadores numéricos unários | __ ne __ - , __ pos __ + , __ abs __ abs() |
| Operadores de comparação rica | __ lt __ > , __ le __ <= , __ eq __ == , __ ne __ != , __ gt __ >, __ ge __ >= |
| Operadores aritméticos | __ add __ + , __ sub __ - , __ mul __ * , __ truediv __ / , __ floordiv __ // , __ mod __ % , __ divmod __ divmod() , __ pow __ ** ou pow() , __ round __ round() |
| Operadores aritméticos reversos | __ radd __ , __ rsub __ , __ rmul __ , __ rtruediv __ , __ rfloordiv __ , __ rmod __ , __ rdivmod __ , __ rpow __ |
| Operadores aritméticos de atribuição combinada | __ iadd __ , __ isub __ , __ imul __ , __ itruediv __ , __ ifloordiv __ , __ imod __ , __ ipow __ |
| Operadores bit a bit (bitwise) | __ invert __ ~ , __ lshift __ << , __ rshift __ >> , __ and __ & , __ or __ | , __ xor __ ^ |
| Operadores bit a bit reversos | __ rlshift __ , __ rrshift __ , __ rand __ , __ rxor __ , __ ror __ |
| Operadores bit a bit de atribuição combinada | __ ilshift __ , __ irshift __ , __ iand __ , __ ixor __ , __ ior __  |

</details>
</br>


## **Pág. 39............Por que len não é um método?**
<details>
<summary></📖></summary>

O len não é um método porque é uma função embutida no Python que retorna o tamanho (número de elementos) de um objeto iterável, como uma lista, uma string ou um dicionário. Em vez de ser um método específico de um objeto, o len é usado como uma função geral que pode ser aplicada a diferentes tipos de objetos iteráveis. Portanto, em vez de chamar objeto.len(), você usa len(objeto) para obter o tamanho do objeto.

### ***Por que len não é um método:***
```python
lista = [1, 2, 3, 4, 5]
tamanho = len(lista)
print(tamanho)  # Saída: 5

```

</details>
