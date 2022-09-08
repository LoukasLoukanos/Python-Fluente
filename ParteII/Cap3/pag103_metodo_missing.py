'''—————Implementação de __missing_———————————————————————————————————————————————————————————————————————————————————————————————
 
 • pag97_metodos_de_mapeamentos:
    O diferencial do tipo de mapeamento defaultdict é que ele é capaz de devolver valores predefinidos quando chaves são ausentes:
    (O método especial __missing__ é o mecanismo que faz defaultdict funcionar(chamando default_factory) para essa finalidade.)
'''

# exemplo com uma classe que herda de dict_____________________________________
class ExemploSimples(dict):  # ExemploSimples herda de dict

    def __missing__(self, key):
        if isinstance(key, str):  # Verifica se key já é uma str. Se for e estiver ausente, gera KeyError.
            raise KeyError(key)
        return self[str(key)]  # Cria str a partir de key e refaz a consulta.

    def get(self, key, default=None):
        try:
            return self[key]  # O método get deleta para __getitem__ usando a notação self[key]; isso dá a oportunidade ao nosso __missing__ de agir.
        except KeyError:
            return default  # Se um KeyError for gerado, é sinal de que __missing__ já falhou, portanto devolveremos default.

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()  # Procura a chave não modificada (a instância pode conter chaves que não sejam str) e, em seguida, procura uma str criada a partir da chave.


'''___testes para ExemploSimples()_________

d = ExemploSimples([('2', 'two'), ('4', 'four')])
d['2']
    output: 'two'
d[4]
    output: 'four'
d[1]
    output: 
        Traceback (most recent call last):
          ...
        KeyError: '1'


d.get('2')
    output: 'two'
d.get(4)
    output: 'four'
d.get(1, 'N/A')
    output: 'N/A'


2 in d
    output: True
1 in d
    output: False

'''

import collections
# exemplo com uma classe que herda de UserDict_____________________________________
# Graças a UserDict, a classe ExemploAvancado é menor que ExemploSimples e sempre converte chaves que não são strings para str — na inserção, na atualização e na consulta.
class ExemploAvancado(collections.UserDict):  # A classe ExemploAvancado estende de UserDict

    def __missing__(self, key):  # __missing_ é exatamente como no exemplo anterior
        if isinstance(key, str): # Verifica se key já é uma str. Se for e estiver ausente, gera KeyError.
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data  # __contais__ é mais simples que no exemplo anterior: pode-se supor que todas as chaves armazenadas sejam str e consultar self.data em vez de chamar senf.keys() como fieto em ExemploSimples

    def __setitem__(self, key, item):
        self.data[str(key)] = item   # __setitem__ converte qualquer key para uma str. Esse método é mais fácil de sobrescrever quando podemos delegar ao atributo self.data.


'''___testes para ExemploAvancado()_________

d = ExemploAvancado([(2, 'two'), ('4', 'four')])
sorted(d.keys())
    output: ['2', '4']


d['2']
    output: 'two'
d[4]
    output: 'four'
d[1]
    output:
        Traceback (most recent call last):
          ...
        KeyError: '1'


d.get('2')
    output: 'two'
d.get(4)
    output: 'four'
d.get(1, 'N/A')
    output: 'N/A'


2 in d
    output: True
1 in d
    output: False


d[0] = 'zero'
d['0']
    output: 'zero'


d.update({6:'six', '8':'eight'})
sorted(d.keys())
    output: ['0', '2', '4', '6', '8']
d.update([(10, 'ten'), ('12', 'twelve')])
sorted(d.keys())
    output: ['0', '10', '12', '2', '4', '6', '8']
d.update([1, 3, 5])
    output: 
        Traceback (most recent call last):
          ...
        TypeError: 'int' object is not iterable
'''
