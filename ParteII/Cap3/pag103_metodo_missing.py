'''____________________pag97_metodos_de_mapeamentos______________________________________________________________________________
 • O diferencial do tipo de mapeamento defaultdict é que ele é capaz de devolver valores predefinidos quando chaves são ausentes:
     (O método especial __missing__ é o mecanismo que faz defaultdict funcionar(chamando default_factory) para essa finalidade.)
'''
class StrKeyDict0(dict):  # <1>

    def __missing__(self, key):
        if isinstance(key, str):  # <2>
            raise KeyError(key)
        return self[str(key)]  # <3>

    def get(self, key, default=None):
        try:
            return self[key]  # <4>
        except KeyError:
            return default  # <5>

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()  # <6>


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
