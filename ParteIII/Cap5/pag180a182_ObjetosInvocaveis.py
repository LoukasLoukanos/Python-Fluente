import random

class BingoCage:

    def __init__(self, items):
        self._items = list(items)  # __init__ aceita qualquer iterável; criar uma cópia legal evita efeitos colaterais inesperados em qualquer list passada como argumento.
        random.shuffle(self._items)  # é certo que shuffle funcionará porque self._items é uma list.

    def pick(self):  # O método principal.
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')  # levanta uma exceção com uma mensagem personalizada se self._items estiver vazio.

    '''Implementar __call__ é uma maneira fácil de criar objetos do tipo função ou similar com algum estado 
       interno que deva ser mantido entre chamadas, por exemplo, os itens restantes em BingoCage.'''
    def __call__(self):  # Atalho para bing.pick(): bingo()
        return self.pick()


bingo = BingoCage(range(3))

bingo.pick() 
#output: 1

bingo() # a instância bingo, de BingoCage, pode ser chamada como função, graças ao método __call__
#output: 0

callable(bingo) # a instância bingo, de BingoCage, é reconhecida pela função embutida callable() como um objeto invocável
#output: True
