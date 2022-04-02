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

'''
 Ao implementar os métodos especiais __len__ e __getitem__ nos
 beneficiamos de recursos especiais da linguagem(neste caso
 iteração e fatiamento) e da biblioteca padrao(random.choice, 
 reversed e sorted). Graças à composição as implementações de
 __len__ e __getitem__ podem passar todo o trabalho para os objetos 
'''

#EXEMPLO:

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
