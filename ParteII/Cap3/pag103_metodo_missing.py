'''—————Implementação de __missing_———————————————————————————————————————————————————————————————————————————————————————————————
 
 • pag97_metodos_de_mapeamentos:
    O diferencial do tipo de mapeamento defaultdict é que ele é capaz de devolver valores predefinidos quando chaves são ausentes:
    (O método especial __missing__ é o mecanismo que faz defaultdict funcionar(chamando default_factory) para essa finalidade.)
'''
class StrKeyDict0(dict):  # StrKeyDict0 herda de dict

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


'''____________________testes para StrKeyDict0()____________________

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
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
