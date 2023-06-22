## **Um baralho pythônico............Pág. 29**

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
</br>

## **Como os métodos especiais são usados............Pág. 33**
 - Ao implementar os métodos especiais _len__ e _getitem__ nos beneficiamos de recursos especiais da linguagem (neste caso iteração e fatiamento) e da biblioteca padrao(random.choice, reversed e sorted). Graças à composição as implementações de _len__ e _getitem__ podem passar todo o trabalho para os objetos
</br>

## **Emulando tipos numéricos............Pág. 34**

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
</br>

## **Representação em string............Pág. 36**

### ***título do código***
