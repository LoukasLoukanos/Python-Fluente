## **Pág. 94 à 96............Tipos genéricos de mapeamento | dict comprehensions**
<details>
<summary></summary>

Mapeamento ou Dicionário (dict) ou hash[key]=value é uma coleção de objetos armazenados por uma chave e valor, ao contrário de sequências que armazenam pela posição dos itens.

```python
# Uma sequência de itens ou lista de pares
DIAL_CODES = [(86, 'China'), (91, 'India'), (1, 'United States'), (62, 'Indonesia'), (55, 'Brazil'), (92, 'Pakistan'), (880, 'Bangladesh'), (234, 'Nigeria'), (7, 'Russia'), (81, 'Japan'),]   

# Criando um Mapeamento (dicionário ou hash[key]=value) com o método dict()__________________________________________________________________
metodo_dict = dict(DIAL_CODES) #método dict()
print('Chaves e valores:', metodo_dict) #output: Chaves e valores: {86: 'China', 91: 'India', 1: 'United States', 62: 'Indonesia', 55: 'Brazil', 92: 'Pakistan', 880: 'Bangladesh', 234: 'Nigeria', 7: 'Russia', 81: 'Japan'}
print('Chaves:', metodo_dict.keys()) #output: Chaves: dict_keys([86, 91, 1, 62, 55, 92, 880, 234, 7, 81])
print('Valores:', metodo_dict.values()) #output: Valores: dict_values(['China', 'India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Bangladesh', 'Nigeria', 'Russia', 'Japan'])

# Criando um Mapeamento (dicionário ou hash[key]=value) com dict comprehensions______________________________________________________________
dict_comprehensions = {key: value for key, value in DIAL_CODES} #dict comprehensionsa
print('Chaves e valores:', dict_comprehensions) #output: Chaves e valores: {86: 'China', 91: 'India', 1: 'United States', 62: 'Indonesia', 55: 'Brazil', 92: 'Pakistan', 880: 'Bangladesh', 234: 'Nigeria', 7: 'Russia', 81: 'Japan'}
print('Chaves:', dict_comprehensions.keys()) #output: Chaves: dict_keys([86, 91, 1, 62, 55, 92, 880, 234, 7, 81])
print('Valores:', dict_comprehensions.values()) #output: Valores: dict_values(['China', 'India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Bangladesh', 'Nigeria', 'Russia', 'Japan'])

dict_comprehensions_2 = {key: value.upper() for key, value in dict_comprehensions.items() if key<66} #dict comprehensions
print(dict_comprehensions_2) #output: {1: 'UNITED STATES', 62: 'INDONESIA', 55: 'BRAZIL', 7: 'RUSSIA'}
```

</details>
</br>


## **Pág. 98............Tratando chaves ausentes com setdefault**
<details>
<summary></summary>

Mapeamento ou Dicionário ("dict") ou hash[key]=value é uma coleção de objetos armazenados por uma chave e um valor, ao contrário de sequências que armazenam pela posição dos itens.

### ***MÉTODOS DE DICT DEFAULTDICT E ORDEREDDICT:***

♦ O diferencial do tipo de mapeamento defaultdict é que ele é capaz de devolver valores predefinidos quando chaves são ausentes:</br>
    (O método especial __missing__ é o mecanismo que faz defaultdict funcionar(chamando default_factory) para essa finalidade.)</br>
→ Nota:
 - @a: default_factory não é um método, mas um atributo de instância invocável (callable) definido pelo usuário final quando defaultdict é instanciada.
 - @b: OrderedDict.popitem() remove o primeiro item inserido (FIFO); um argumento last opcional, se definido com True, remove o último item (LIFO).

| MÉTODOS | dict | defaultdict | OrderedDict |  |
|:-:|:-:|:-:|:-:|:-:|
| d.clear() | ● | ● | ● | Remove todos os itens |
| d.contains(k) | ● | ● | ● | k in d |
| d.copy() | ● | ● | ● | Cópia rasa |
| d._copy_() |  | ● |  | Suporte para copy.copy |
| d.default_factory |  | ● |  | Função a ser chamada por __missing__ para gerar valores ausentes [ver nota @a] |
| d__deliten__(k) | ● | ● | ● | del d[k] – remove item com a chave k |
| d.fronkeys(it, [initial]) | ● | ● | ● | Novo mapeamento a partir das chaves do iterável, com valor inicial opcional (default é None) |
| d.get(k, [default]) | ● | ● | ● | Obtém item com a chave k; devolve default ou None se estiver ausente |
| d.__getiten__(k) | ● | ● | ● | d[k]-obtém item com a chave k |
| d.items() | ● | ● | ● | Obtém view sobre itens - pares (key, value) |
| d.__iter__() | ● | ● | ● | Obtém um iterador para chaves |
| d.keys() | ● | ● | ● | Obtém view para chaves |
| d.__len__() | ● | ● |●  | len(s)-número de itens |
| d.__missing__(k) |  | ● |  | Chamado quando __gettten__ não encontra a chave |
| d.move_to_end(k, [Last]) |  |  | ● | Move k para a primeira ou para a última posição (last é True por default) |
| d.pop(k, [default]) | ● | ● | ● | Remove e devolve o valor em k, ou default ou None se estiver ausente |
| d.popitem() | ● | ● | ● | Remove e devolve um item (key, value) arbitrário [ver nota @b] |
| d.__reversed__() |  |  | ● | Obtém um iterador para chaves do último para o primeiro inserido |
| d.setdefault(k, [default]) | ● | ● | ● | Se k in d, devolve d[k]; caso contrário, define d[k] default e devolve esse valor |
| d.__setitem__(k, v) | ● | ● | ● | d[k] = v – coloca v em k |
| d.update(m, [**kargs]) | ● | ● | ● | Atualiza d com itens do mapeamento ou do iterável de pares (key, value) |
| d.values() | ● | ● | ● | Obtém view dos valores |

</details>
</br>


## **Pág. 97............Visão geral dos métodos comuns a mapeamentos**
<details>
<summary></summary>

adapted from Alex Martelli's example in "Re-learning Python"
http://www.aleax.it/Python/accu04_Relearn_Python_alex.pdf
(slide 41) Ex: lines-by-word file index


#### **Explicação de with:**
with é usado para garantir finalização de recursos adquiridos.</br>
No exemplo citado deve ficar algo parecido com isto internamente:</br>

```python
try:
    __enter__()
    open(sys.argv[1], encoding='utf-8') as fp:
        #bloco de códigos
finally:
    __exit__()
```

```python
import sys
import re
import collections #para collections.defaultdict()

WORD_RE = re.compile(r'\w+')

index = {}

'''
♦ OBJETIVO:__________________________________________________________________________________________
Demonstrar um código que satisfaça o exemplo do uso do mapeamento abaixo, [FAZENDO APENAS UMA BUSCA].
    if key not in my_dict:           → 1°BUSCA
        my_dict[key] = []
    my_dict[key].append(new_value)   → 2°BUSCA
'''

#MANEIRA 1[DUAS BUSCAS]:
with open(sys.argv[1], encoding='utf-8') as fp: # with↓; as→alias(apelido)
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)

            # MANEIRA 1: com my_dict.get(k, [default])   →   Obtém item com a chave k; devolve default ou None se estiver ausente (pag97_metodos_de_mapeamento.py).
            occurrences = index.get(word, [])  # 1°BUSCA: Obtêm a lista de ocorrências para word, ou [] se essa palavra não for encontrada
            occurrences.append(location)       # Concatena a nova posição para ocurrences 
            index[word] = occurrences          # 2°BUSCA: Coloca occurrences alterado no dicionário index; isso [IMPLICA UMA SEGUNDA BUSCA] em index

#ou MANEIRA 2[UMA BUSCA]:
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            
            # MANEIRA 2: → com my_dict.setdefault(k, [default])   →   Se k in my_dict, devolve my_dict[k]; caso contrário, define my_dict[k] = default e devolve esse valor (pag97_metodos_de_mapeamento.py).
            index.setdefault(word, []).append(location)  # Obtêm a lista de ocorrências para word, ou [] se essa palavra não for encontrada; setdefault devolve o valor, portanto poderá ser atualizada [SEM EXIGIR UMA SEGUNDA BUSCA]).


'''
♦ CONCLUSÃO:__________________________________________________________________________________________
A MANEIRA 2:
    my_dict.setdefault(key, []).append(new_value)   → UMA ÚNICA BUSCA

É EQUIVALENTE À:
    if key not in my_dict:           → +1 BUSCA
        my_dict[key] = []         → +1 (ou não)
    my_dict[key].append(new_value)   → +1 BUSCA

COM EXCEÇÃO DE QUE .setdefault FAZ TUDO COM [UMA ÚNICA BUSCA]
'''

# print in alphabetical order
for word in sorted(index, key=str.upper):  # No argumento key= de sorted, não é chamando str.upper; mas apenas passado uma referência a esse método para que a função sorted possa usá-lo a fim de normalizar as palavras para a ordenação.
    print(word, index[word])
# END INDEX0


'''
____________________________________________________________________________________________________________________________________________
→ o mapeamento defaultdict devolve valores predefinidos quando chaves são ausentes, pode ser usado no lugar do método setdefault.
dado um defaultdict vazio criado como dd = defaultdict(list), se 'new-key' não estiver em dd, a expressão dd['new-key'] executará os passos:
    •Chama list() para criar uma nova lista.
    •Insere a lista em dd usando 'new-key' como chave.
    •Devolve uma referência a essa lista.
'''
WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)     # Cria um defaultdict com o construtor list como default_factory
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location)  # Se word não estiver inicialmente em index, default_factory será chamado para gerar o valor
                                          # ausente, que, neste caso, é uma list vazia; ela será então atribuida a index[word] e
                                          # devolvida, de modo que a operação .append(location) sempre será bem-sucedida.

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])
# END INDEX0
```

</details>
</br>


## **Pág. 101 a 102............Mapeamentos com consulta de chave flexível | defaultdict: outra abordagem para chaves ausentes | Método _ausente__**
<details>
<summary></summary>

#### **Implementação de __missing_**
 - pag97_metodos_de_mapeamentos:
   - O diferencial do tipo de mapeamento defaultdict é que ele é capaz de devolver valores predefinidos quando chaves são ausentes:
     - (O método especial __missing__ é o mecanismo que faz defaultdict funcionar(chamando default_factory) para essa finalidade.)

```python
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
```

</details>
</br>


## **Pág. 105 a 113............Variações de dict | Criando subclasses de UserDict | Mapeamentos imutáveis | Teoria dos conjuntos | Literais de set | Set comprehensions | Operações de conjuntos**
<details>
<summary></summary>

### ***Operações matemáticas de set: esses métodos geram um novo conjunto ou atualizam o conjunto-alvo in-place se ele for mutável:***

| SIMB MAT | OPER PYTHON | MÉTODO | DESCRIÇÃO |
|:-:|:-:|:-:|:-:|
| S∩Z. | s & z | s.__and__(z) | Intersecção entre s e z |
|  | z & s | s__rand__(z) | Operador & reverso |
|  |  | s.intersection(it, ...) | Intersecção entre s e todos os conjuntos criados a partir dos iteráveis it etc |
|  | s &= z | s.__iand__(z) | s atualizado com a intersecção entre s e z |
|  |  | s.intersection_update(it, ...) | s atualizado com a intersecção entre s e todos os conjuntos criados a partir dos iteráveis it etc |
| SUZ | s | z | s.__or__(z) | União de s e z |
|  | z | s | s.__ror__(z) | Operador | reverso |
|  |  | s.union(it, ...) | União de s e todos os conjuntos criados a partir dos iteráveis it etc |
|  | s |= z | s.__ior__(z) | s atualizado com a união de s e z |
|  |  | s.update(it, ...) | s atualizado com a união de s e todos os conjuntos criados a partir dos iteráveis it etc |
| S\Z | s - z | s.__sub__(z) | Complemento relativo ou diferença entre s e z |
|  | z - s | s.__rsub__(z) | Operador - reverso |
|  |  | s.difference(it, ...) | Diferença entre s e todos os conjuntos criados a partir dos iteráveis it etc |
|  | s -= z | s.__isub__(z) | s atualizado com a diferença entre s e z |
|  |  | s.difference_update(it, ...) | s atualizado com a diferença entre s e todos os conjuntos criados a partir dos iteráveis it etc |
|  |  | s.symmetric_difference(it) | Complemento de s & set(it) |
| SΔZ | s ^ z | s.__xor__(z) | Diferença simétrica (complemento da intersecção s & z) |
|  | z ^ s | s.__rxor__(z). | Operador ^ reverso |
|  |  | s.symmetric_difference_update(it, ...) | s atualizado com a diferença simétrica entre s e todos os conjuntos criados a partir dos iteráveis it etc |
|  | s ^= z | s.__ixor__(z) | s atualizado com a diferença simétrica de s e z |


### ***Operadores e métodos de comparação de conjuntos que devolvem um booleano:***

| SIMB MAT | OPER PYTHON | MÉTODO | DESCRIÇÃO |
|:-:|:-:|:-:|:-:|
|  |  | s.Isdisjoint(z) | sez são disjuntos (não tem nenhum elemento em comum) |
| e∈S | e in s | s.__contain__(e) | O elemento e está presente em s |
| S⊆Z | s <= s | s.__le__(z)  | s é um subconjunto do conjunto z |
|  |  | s.issubset(it) | s é um subconjunto do conjunto criado a partir do iterável it |
| S⊂Z | s < z | s.__lt__(z) | s é um subconjunto próprio do conjunto z |
| S⊇Z | s >= z | s.__ge__(z) | s é um superconjunto do conjunto z |
|  |  | s.issuperset(it) | s é um superconjunto do conjunto criado a partir do iterável it |
| S⊃Z | s > z | s.__gt__(z) | s é um superconjunto próprio do conjunto z |


### ***Métodos adicionais de conjuntos:***

|  | set | frozenset | DESCRIÇÃO |
|:-:|:-:|:-:|:-:|
| s.add(e) | ● |  | Adiciona o elemento e em s |
| s.clear() | ● |  | Remove todos os elementos de s |
| s.copy() | ● | ● | Cópia rasa de s |
| s.discard(e) | ● |  | Remove o elemento e de s se estiver presente |
| s.__iter__() | ● | ● | Obtém um iterador para s |
| s.__len__() | ● | ● | len(s) |
| s.pop() | ● |  | Remove e devolve um elemento de s, gerando KeyError ses estiver vazio |
| s.remove(e) | ● |  | Remove o elemento e de s, gerando KeyError se e not in s |

</details>
</br>


## **Pág. 116 a 125............Por dentro de dict e set | Um experimento para testar o desempenho | Tabelas hash em dicionários | Consequências práticas de como os dicionários funcionam | Como os conjuntos funcionam – consequências práticas**
<details>
<summary></summary>

### ***As chaves dos dict ou dicionários ou hash[key]=value precisam ser objetos hashable:***
**♦ Um objeto é hashable se:**</br>
 - 1. Tiver um valor de hash que nunca mude: i.e., oferecer suporte a função hash por meio de um método __hash__ que sempre devolva o mesmo valor.
 - 2. Puder ser comparado com outros objetos: i.e., possuir suporte à igualdade por meio do método __eq__().

</br>

*→ Se a == b é True, então hash(a) == hash(b) também deve ser True.*

</br>

```python
# Códigos de discagem dos dez países mais populosos
DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]

d1 = dict(DIAL_CODES)  # d1 é criado a partir de tuplas, em ordem decrescente por padrão.

d2 = dict(sorted(DIAL_CODES))  # d2 é criado com tuplas ordenadas de acordo com o código de discagem do país.

d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))  # d3 é cria com tuplas ordenadas de acordo com o nome do país

print('d1:', d1.keys())
print('d2:', d2.keys())
print('d3:', d3.keys())
'''output:
d1: dict_keys([86, 91, 1, 62, 55, 92, 880, 234, 7, 81])
d2: dict_keys([1, 7, 55, 62, 81, 86, 91, 92, 234, 880])
d3: dict_keys([880, 55, 86, 91, 62, 81, 234, 92, 7, 1])
'''
assert d1 == d2 and d2 == d3  # d4 os dicionários são comparados como iguais, pois armazenam as mesmas células/baldes(bucket)/pares key:value.
```

</details>
