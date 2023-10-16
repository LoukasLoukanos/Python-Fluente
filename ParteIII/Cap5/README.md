## **Pág. 177 à 179............Tratando uma função como um objeto | Funções de ordem superior | Substitutos modernos para map, filter e reduce**
<details>
<summary></summary>

```python
''' Funções de ordem superior (higher-order function) do paradigma da programação funcional
→ Uma função que aceita uma função como argumento ou que devolve uma funcão como resultado

Algumas das funções de ordem superior mais conhecidas são map, filter, reduce e apply. ("ABSOLETAS↓")
List comprehensions(list comp) e expressões geradoras (genexp) fazem o trabalho conjunto de map e filter, porém são mais legíveis:
'''
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

fact = factorial

list(map, range(6)) #→ "ABSOLETO"
#output: [1, 1, 2, 6, 24, 120] 

[fact(n) for n in range(6)] #→ "LISTCOMP"
#output: [1, 1, 2, 6, 24, 120]


'''
A ideia comum de sum e reduce é aplicar alguma operação a itens sucessivos em uma sequência, acumulando 
resultados anteriores e, desse modo, reduzindo uma sequência de valores a um único valor: '''

#→"ABSOLETO":
from functools import reduce
from operator import add 
reduce(add, range(100))
output: 4950

#→"PREFERÍVEL":
sum(range(100))
output: 4950

'''
Outras funções embutidas para redução são all e any:

all(lterable):
Devolve True se todos os elementos de iterable forem verdadeiros; all([]) devole True.

any(Iterable)
Devolve True se algum elemento de iterable for verdadeiro; all([]) devolve False
'''

```

</details>
</br>


## **Pág. 180 à 182............Funções anônimas | As sete variações de objetos invocáveis | Tipos invocáveis definidos pelo usuário**
<details>
<summary></summary>

```python
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

```

</details>
</br>


## **Pág. 183 à 185............Introspecção de função**
<details>
<summary></summary>

```python
# Assim como as instâncias de uma classe comum definida pelo usuário, uma função usa o atributo_dict_para armazenar os atributos de usuário atribuídos a ela.

class C: pass # Cria uma classe vazia definida pelo usuário. 

obj = C() # Cria uma instância dessa classe. 

def func(): pass # Cria uma função vazia. 


# Gera uma lista ordenada de atributos existentes em uma função vazia:
sorted(set(dir(func)))
# output: ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


# Gera uma lista ordenada de atributos existentes em uma instância de uma classe vazia:
sorted(set(dir(obj)))
# output: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']


# Usando a diferença entre conjuntos, gera uma lista ordenada de atributos existentes em uma função, mas não em uma instância de uma classe vazia:
sorted(set(dir(func)) - set(dir(obj)))
# output: ['__annotations__', '__builtins__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']

```

</details>
</br>


## **Pág. 186 e 187............De parâmetros posicionais a parâmetros exclusivamente nomeados**
<details>
<summary></summary>

```python

'''
♦ PARÂMETROS POSICIONAIS → são argumentos de uma função que são passados na ordem em que foram definidos na assinatura da função. Esses argumentos são obrigatórios.
♦ OPERADOR * → Permite que argumentos adicionais sejam passados para uma função como PARÂMETROS POSICIONAIS. É usado para coletar um número variável de argumentos em uma tupla.

♦ PARÂMETROS NOMEADOS → são argumentos de uma função que são passados explicitamente pelo nome →"agr=nome". Esses argumentos são opcionais e podem ser omitidos.
♦ OPERADOR ** → Permite que argumentos adicionais sejam passados para uma função como PARÂMETROS NOMEADOS. É usado para coletar um número variável de argumentos em um dicionário.
'''

def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)
    

# Um único argumento posicional produz uma tag vazia com esse nome:
tag('br')  # PARÂMETRO POSICIONAL
#output: '<br />'

# Qualquer quantidade de argumentos após o primeiro é capturada por *content como uma tuple:
tag('p', 'hello') # OPERADOR * em *content para PARÂMETRO POSICIONAL
#output: '<p>hello</p>'

tag('p', 'hello', 'world') # OPERADOR * em *content para PARÂMETROS POSICIONAIS
'''output: <p>hello</p>
           <p>world</p>
'''

# Argumentos nomeados não explicitamente nomeados na assinatura de tag são capturados por **attrs como um dict:
tag('p', 'hello', id=33)  # OPERADOR * em **attrs para PARÂMETRO NOMEADO
#output: '<p id="33">hello</p>'

# O parámetro cls pode ser passado somente como um argumento nomeado:
tag('p', 'hello', 'world', cls='sidebar') # PARÂMETROS POSICIONAIS e PARÂMETRO NOMEADO
'''output: <p class="sidebar">hello</p>
           <p class="sidebar">world</p>
'''

# Mesmo o primeiro argumento posicional pode ser passado como um argumento nomeado quando tag é chamada.
tag(content='testing', name="img")  # PARÂMETROS POSICIONAIS (ao passar o PARÂMETRO NOMEADO 'name' como segundo argumento, devemos passa-lo como NOMEADO)
#output: '<img content="testing" />'

# Passar um dict como argumento com ** faz todos os seus itens serem passados como argumentos separados, que são então associados aos PARÂMETROS NOMEADOS, com o restante capturado por **attrs:
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
tag(**my_tag) 
#output: '<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'

```

</details>
</br>


## **Pág. 188 à 190............Obtendo informações sobre parâmetros**
<details>
<summary></summary>

```python
'''
ACESSO À INFORMAÇÕES DE OBJETOS E PARÂMETROS DE FUNÇÕES (INTROSPECÇÃO)

Introspecção é a capacidade de uma linguagem como Python de examinar seu próprio código e as informações associadas a ele em tempo de execução.
O módulo ♦inspect, nativo do Python, é útil para depurar código e obter informações sobre como os objetos Python estão sendo usados em tempo de 
execução, pois permite obter informações detalhadas sobre um objeto Python, como suas propriedades, métodos e docstrings, podendo ser útil para 
obter a lista de métodos e atributos de uma classe ou, até mesmo, para verificar se uma função é assíncrona. Ou seja, o módulo ♦inspect é uma 
ferramenta poderosíssima e avançada de Introspecção, nativa do python e para o python.
O modelo de dados de Python, com a ajuda do módulo ♦inspect, expõe o mesmo mecanismo usado pelo interpretador para associar argumentos a parâmetros 
formais em chamadas de função. Frameworks e ferramentas como IDEs podem usar essas informações para validar códigos. Outro recurso de Python 3, as 
anotações de função, expandem os possíveis usos disso.

Alguns dos métodos disponíveis no módulo ♦inspect (existem muitos outros métodos úteis de inspect para realizar operações de introspecção em objetos Python):
•getmembers(obj[, predicate]): retorna uma lista de tuplas que representam os membros de um objeto, incluindo métodos, atributos e outros membros.
•signature(obj): retorna a assinatura de uma função, método ou callable como um objeto Signature.
•isfunction(obj): retorna True se o objeto passado for uma função, ou False caso contrário.
•ismethod(obj): retorna True se o objeto passado for um método, ou False caso contrário.
•isclass(obj): retorna True se o objeto passado for uma classe, ou False caso contrário.
•isgenerator(obj): retorna True se o objeto passado for um generator, ou False caso contrário.
•isasyncgen(obj): retorna True se o objeto passado for um async generator, ou False caso contrário.
•isroutine(obj): retorna True se o objeto passado for uma função, método ou callable, ou False caso contrário.
•getsource(obj): retorna o código-fonte de um objeto, como uma string.
•getfile(obj): retorna o nome do arquivo em que um objeto foi definido.
•getmodule(obj[, _filename]): retorna o módulo em que um objeto foi definido.
•getmembers(module[, predicate]): retorna uma lista de tuplas que representam os membros de um módulo, incluindo funções, classes e outros membros.
•getdoc(obj): retorna a documentação de um objeto, como uma string.
'''


# _________________________________________________________________________________
def clip(text, max_len=80):
    '''
    Exempo de função para ser usada com o módulo ♦inspect:
    Encurta um texto para um comprimento máximo especificado. Se o texto fornecido for mais longo do que o comprimento máximo 
    especificado, a função encontra o último espaço antes ou depois da posição máxima permitida e encurta o texto até esse ponto. 
    Se não houver espaços no texto, a função simplesmente encurta o texto para o comprimento máximo permitido.
    '''
    end = None # Inicializa a variável 'end' como 'None'
    
    if len(text) > max_len: # Verifica se o comprimento do texto é maior do que o comprimento máximo permitido
        space_before = text.rfind(' ', 0, max_len) # Procura a posição do último espaço no texto antes da posição máxima permitida
        if space_before >= 0: # Se a posição do último espaço antes da posição máxima permitida for encontrada, atribui essa posição à variável 'end'
            end = space_before
        else: # Caso contrário, procura a posição do último espaço após a posição máxima permitida
            space_after = text.rfind(' ', max_len)
            if space_after >= 0: # Se a posição do último espaço após a posição máxima permitida for encontrada, atribui essa posição à variável 'end'
                end = space_after
    if end is None: # Se a variável 'end' não foi atribuída uma posição, significa que não há espaços no texto para encurtar
        end = len(text) # Define a posição final como o comprimento total do texto
    return text[:end].rstrip() # Retorna o texto encurtado até a posição final e remove quaisquer espaços em branco adicionais do final da string
   
   
# Exemplos de uso apenas da função:
clip('banana ', 6)
#output: 'banana'

clip('banana ', 7)
#output: 'banana'

clip('banana ', 5)
#output: 'banana'

clip('banana split', 6)
#output: 'banana'

clip('banana split', 7)
#output: 'banana'

clip('banana split', 10)
#output: 'banana'

clip('banana split', 11)
#output: 'banana'

clip('banana split', 12)
#output: 'banana split'


# _________________________________________________________________________________
# ACESSANDO INFORMAÇÕES DA FUNÇÃO clip() (INTROSPECÇÃO), MAS SEM O USO DE ♦inspect:

# 'clip.defaults' retorna uma tupla que contém os valores padrão dos parâmetros da função 'clip'. Nesse caso, o valor padrão para o parâmetro 'max_len' é 80.
clip.__defaults__
#output: (80,)

# 'clip.code' retorna um objeto de código que contém várias informações sobre a função 'clip', incluindo seu bytecode (a sequência de instruções em Python que implementam a função) e outras informações sobre como a função foi definida.
clip.__code__  # doctest: +ELLIPSIS
#output: <code object clip at 0x...>

#'clip.code.co_varnames' retorna uma tupla contendo os nomes de todas as variáveis locais e argumentos posicionais na função 'clip'.
clip.__code__.co_varnames
#output: ('text', 'max_len', 'end', 'space_before', 'space_after')

#'clip.code.co_argcount' retorna o número total de argumentos que a função 'clip' aceita. Nesse caso, a função aceita dois argumentos: 'text' e 'max_len'.
clip.__code__.co_argcount
#output: 2


# _________________________________________________________________________________________________________
# ACESSANDO INFORMAÇÕES DA FUNÇÃO clip() (INTROSPECÇÃO), COM O USO DA FUNÇÃO •signature do MÓDULO ♦inspect:
'''
Algumas das funções que podem ser usadas com o objeto Signature:
→ parameters: retorna uma lista com os objetos Parameter do objeto Signature, que contêm informações sobre cada um dos parâmetros da função.
→ bind: permite ligar os argumentos passados para a função aos parâmetros da assinatura da função. Essa função pode levantar exceções se houver erros de ligação.
→ bind_partial: semelhante à função bind(), mas permite ligar apenas alguns dos argumentos da função aos parâmetros da assinatura. Os argumentos não passados serão substituídos pelos seus valores padrão.
→ return_annotation: retorna a anotação de retorno da função, se houver.
'''
from inspect import signature

# 'sig = signature(clip)' cria um objeto Signature que representa a assinatura da função 'clip', incluindo o número e o nome de seus parâmetros.
sig = signature(clip)

# 'sig' imprime a assinatura da função 'clip', que mostra o nome da função, seus parâmetros e seus valores padrão, se houver.
sig
#output: <inspect.Signature object at 0x...>

# 'str(sig)' retorna a representação em forma de string da assinatura da função 'clip'.
str(sig)
#output: '(text, max_len=80)'

# O loop 'for name, param in sig.parameters.items():' itera através dos parâmetros da função 'clip' e extrai informações sobre cada um deles.
for name, param in sig.parameters.items():
    #imprime o tipo de cada parâmetro (posicional ou com palavra-chave), seu nome e seu valor padrão, se houver.
    print(param.kind, ':', name, '=', param.default)
    """output:
    POSITIONAL_OR_KEYWORD : text = <class 'inspect._empty'>
    POSITIONAL_OR_KEYWORD : max_len = 80
    """

    
# ______________________________________________________________________________________________________________________________________________________
# ACESSANDO INFORMAÇÕES DA FUNÇÃO tag() (INTROSPECÇÃO) do módulo pag186e187_ArgsPosicionaisNomeados, COM O USO DA FUNÇÃO •signature do MÓDULO ♦inspect:
import pag186e187_ArgsPosicionaisNomeados
import inspect

sig = inspect.signature(pag186e187_ArgsPosicionaisNomeados.tag) # Obtém a assinatura da função tag do exemplo

my_tag = {'name': 'ing', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'Framed'}
bound_args = sig.bind(**my_tag) # Passa um dict com os argumentos para .bind()

bound_args # Um objeto inspect.BoundArguments é produzido ↓
#output: <inspect.BoundArguments object at 0x..>

# Faz uma iteração pelos itens em bound_args.arguments, que é um OrderedDict, para exibir os nomes e os valores dos argumentos ↓ 
for name, value in bound_args.arguments.items():
    print(name, '=', value)
    '''output:
    name = img
    cls = framed
    attrs = {'title': 'Sunset Boulevard', 'src': 'sunset.jpg"}
    '''

del my_tag['name'] # Remove o argumento obrigatório name de my_tag.

bound_args = sig.bind(**my_tag) # Chamar sig.bind(**my_tag) gera um TypeError que reclama do parâmetro name ausente.
'''output:
Traceback (most recent call last):
TypeError: 'name' paraneter lacking default value
'''

```

</details>
</br>


## **Pág. 191 e 192............Anotações de função**
<details>
<summary></summary>

```python
''' ANOTAÇÕES DE FUNÇÃO: 
  As anotações de função em Python são utilizadas para especificar o tipo de dado esperado para cada parâmetro da função, bem como 
  o tipo de dado que é retornado pela função. Ou seja, anotações ajudam a documentar o tipo de entrada e saída esperado pela função 
  de maneira semelhante à assinatura de métodos em Java. As anotações de função em Python são opcionais e não afetam o comportamento 
  da função em si, a única coisa que python faz com as anotações, é armazená-las no atributo __annotations__, que é um dict.

As anotações de função são especificadas colocando o nome do parâmetro seguido de dois pontos e, em seguida, o tipo esperado. 
Por exemplo, uma função que recebe dois números inteiros e retorna outro número inteiro pode ser escrita da seguinte forma:
'''
def soma(a: int, b: int) -> int:
    # → anotação a: int indica que o primeiro parâmetro da função soma deve ser um inteiro
    # → anotação b: int indica que o segundo parâmetro também deve ser um inteiro
    # → anotação -> int indica que a função retorna um inteiro.
    return a + b

print(soma.__annotations__)
# output: {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}



def clip(text:str, max_len:'int > 0'=80) -> str:  # Função clip do exemplo pag188a190_InformacoesDeParametros.py declarada com anotações
   
    # Encurta um texto para um comprimento máximo especificado...
    
    end = None

    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()

print(clip.__annotations__)
# output: {'text': <class 'str'>, 'max_len': 'int > 0', 'return': <class 'str'>}

# podemos usar signature para inspecionar melhor
from inspect import signature
sig = signature(clip)
print(sig.return_annotation) # return_annotation é um atributo do objeto Signature 'sig' que mostra o tipo da anotação de retorno
#output: <class 'str'>

for param in sig.parameters.values(): # parameters é um dicionario do objeto Signature 'sig'
    note = repr(param.annotation).ljust(13)
    print(note, ':', param.name, '=', param.default)
    '''output:    
    <class 'str'> : text = <class 'inspect._empty'>
    'int > 0'     : max_len = 80
    '''

```

</details>
</br>


## **Pág. 194 à 200............Pacotes para programação funcional | Módulo operator | Congelando argumentos com functools.partia**
<details>
<summary></summary>

```python
'''A programação funcional em Python é um paradigma de programação que se concentra na avaliação de funções matemáticas e evita mudanças de 
estado e dados mutáveis. Em outras palavras, o foco principal é escrever funções puras que não têm efeitos colaterais e que retornam sempre 
o mesmo resultado para as mesmas entradas.

Em Python, a programação funcional pode ser alcançada usando funções lambda, funções de ordem superior, compreensão de lista e geradores. A 
programação funcional também é comumente usada em combinação com a programação orientada a objetos para criar código mais legível e fácil de 
manter.

Alguns benefícios da programação funcional incluem a redução de efeitos colaterais, que podem levar a bugs difíceis de depurar, e a 
simplificação da lógica do programa. Além disso, a programação funcional permite a criação de código mais modular e reutilizável, o 
que pode acelerar o processo de desenvolvimento e melhorar a qualidade do software.
'''

# Alguns dos ♦pacotes mais utilizados em programação funcional em Python:
#_________________________________________________________________________________
# ♦NumPy: uma biblioteca para computação científica que inclui suporte para matrizes multidimensionais e funções matemáticas.
import numpy as np

# Criando uma matriz 3x3 de números aleatórios
matriz_aleatoria = np.random.rand(3,3)

# Multiplicando cada elemento da matriz por 2
matriz_dobrada = matriz_aleatoria * 2

# Calculando a média dos elementos da matriz
media_matriz = np.mean(matriz_aleatoria)

#_________________________________________________________________________________
# ♦Pandas: uma biblioteca para análise de dados que fornece estruturas de dados flexíveis e eficientes, além de ferramentas para manipulação e análise de dados.
import pandas as pd

# Criando um dataframe a partir de um arquivo CSV
df = pd.read_csv('dados.csv')

# Selecionando as linhas do dataframe onde a coluna 'idade' é maior que 30
df_mais_velhos = df[df['idade'] > 30]

# Calculando a média da coluna 'salário'
media_salario = df['salário'].mean()

#_________________________________________________________________________________
# ♦functools: um módulo que fornece ferramentas para trabalhar com funções e objetos relacionados a funções, incluindo decorators, redução de sequências e memorização.
import functools

# Criando uma função que multiplica seus dois argumentos
def multiplicar(x, y):
    return x * y

# Criando uma nova função que sempre multiplica seu primeiro argumento por 2
multiplicar_por_2 = functools.partial(multiplicar, 2)

# Aplicando a nova função com um segundo argumento
resultado = multiplicar_por_2(5)  # Retorna 10

#_________________________________________________________________________________
# ♦itertools: um módulo que fornece ferramentas para trabalhar com iteradores e geradores, incluindo combinações, permutações e produtos cartesianos.
import itertools

# Criando um iterador que gera todas as combinações de duas letras a partir de uma lista
letras = ['a', 'b', 'c']
combinacoes = itertools.combinations(letras, 2)

# Imprimindo as combinações geradas
for combinacao in combinacoes:
    print(combinacao)
# Output: ('a', 'b'), ('a', 'c'), ('b', 'c')

#_________________________________________________________________________________
# ♦operator: um módulo que fornece funções que replicam os operadores internos do Python, como adição, subtração e multiplicação, como funções normais.
import operator

# Criando uma lista de números inteiros
numeros = [1, 2, 3, 4, 5]

# Somando todos os números da lista usando a função reduce do functools e o operador '+'
soma = functools.reduce(operator.add, numeros)

# Verificando se o número 3 está na lista usando o operador 'in'
esta_na_lista = operator.contains(numeros, 3)

#_________________________________________________________________________________
# •reduce de ♦functools: reduce é uma função do módulo functools em Python que permite reduzir uma sequência de valores a um único valor aplicando uma 
# função cumulativa que combina cada elemento da sequência com o resultado anterior.

# Fatorial Implementado com reduce e uma função anônima
from functools import reduce 
def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

#_________________________________________________________________________________
# •mul de ♦operator: mul é uma função do módulo operator em Python que retorna o produto de dois valores. Essa função é frequentemente usada em conjunto 
# com a função reduce do módulo functools para calcular o produto de uma sequência de valores.

# Para evitar o trabalho de escrever funções anónimas triviais como acima↑, o módulo 
# operator oferece equivalentes de funções para dezenas de operadores artiméticos.

# Fatorial implementado com reduce e operator.mul
from functools import reduce 
from operator import mul
def fact(n):
    return reduce(mul, range(1, n+1))

#_________________________________________________________________________________
# •itemgetter de ♦operator: itemgetter é uma função do módulo operator em Python que retorna uma função que pode ser usada para recuperar um determinado 
# item de uma sequência ou de um objeto. Essa função é especialmente útil quando se trabalha com objetos que têm muitos atributos e se deseja acessar 
# apenas um ou alguns deles.

# Demo de itemgetter para ordenar uma lista de tuplas
from operator import itemgetter
metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.288889)), ('Mexico City', 'X', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 29.104, (40.888611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
for city in sorted (metro_data, key=itemgetter(1)):
    print(city)
    '''output:
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.288889))
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)) 
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)) 
        ('New York-Newark', 'US', 20.164, (48.808611, -74.020386))
    '''
# Devolvendo tuplas com valores extraídos:
cc_name = itemgetter (1, 0)
for city in metro_data: 
    print(cc_name(city))
    '''output:
        ('JP', 'Tokyo')
        ("IN", "Delhi NCR')
        ('x', 'Mexico City')
        ('US', 'New York-Newark')
        ('BR', 'Sao Paulo')
    '''

#_________________________________________________________________________________
# •attrgetter de ♦operator: attrgetter é uma função da biblioteca operator do Python que retorna uma função que pode ser usada para obter um determinado
#  atributo de um objeto. A função attrgetter pode ser usada em conjunto com outras funções como sorted, min, max, entre outras, para ordenar ou processar 
#  objetos com base em um determinado atributo.
from collections import namedtuple

LatLong = namedtuple('LatLong', 'lat long') # Usa namedtuple para definir LatLong.

Metropolis = namedtuple('Metropolis', 'nane cc pop coord') # Também define Metropolis.

metro_areas = [Metropolis (name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data] # Cria a lista retro areas com instâncias de Metropolis; observe o desempacotamento da tupla aninhada para extrair (lat, long) e usar esses valores para criar o Latlong para o atributo coord de Metropolis.

print(metro_areas[0])
#output: Metropolis (name='Tokyo', cc='JP', pop-36.933, coord=LatLong(lat-35.689722, long-139.691667))

print(metro_areas[0].coord.lat) # Acessa o elemento netro_areas[0] internamente para obter sua latitude
#output: 35.689722

from operator import attrgetter

name_lat = attrgetter('name', 'coord.lat') # Define um attrgetter para obter name e o atributo aninhado coord.lat

for city in sorted(metro_areas, key=attrgetter('coord.lat')): # Usa attrgetter novamente para ordenar a lista de cidades de acordo com a latitude.
    print(name_lat(city)) # Usa o attrgetter definido em 157 para mostrar somente o nome da cidade e a latitude.
    '''output:
    ('Sao Paulo', -23.547778)
    ('Mexico City', 19.433333)
    ('Delhi NCR, 28.613889) 
    ('Tokyo', 35.689722)
    ('New York-Newark', 49.888611)
    '''

#_________________________________________________________________________________
from operator import methodcaller
s = 'The tine has cone!'
upcase = methodcaller('upper')
print(upcase(s))
#output: THE TIME HAS COME 

hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s))
#output: 'The-tine-has-cone'

print(str.upper(s))
#output: 'THE TIME HAS COME'


#_________________________________________________________________________________
'''Congelando argumentos com functools partial
O módulo functools reúne uma porção de funções de ordem superior. A mais conhecida delas provavelmente é reduce.
Entre as funções restantes em functools, as mais úteis são partial e a sua variante partialmethod.'''

from operator import mul
from functools import partial 
triple = partial (mul, 3) # Cria uma nova função triple a partir de rul, associando o primeiro argumenta posicional a 3.
print(triple(7)) # Testa. 
#output: 21

list(map(triple, range(1, 10))) # Usa triple com map; mul não funcionaria com map nesse exemplo.
#output: [3, 6, 9, 12, 15, 18, 21, 24, 27]

#_________________________________________________________________________________
# Criando uma função conveniente para normalização de Unicode com parcial

import unicodedata, functools

nfc = functools.partial (unicodedata.normalize, 'NFC')
s1 = 'café' 
s2 = 'cafe\u0301'
print(s1, s2)
#output: ('café', 'café')

print(s1 == s2)
#output: False

print(nfc(s1) == nfc(s2))
#output: True

#_________________________________________________________________________________
# Demo de parcial aplicado à função tag do exemplo pag186e187_ArgsPosicionaisNomeados.py

from pag186e187_ArgsPosicionaisNomeados import tag
print(tag) # ↑ Importa tag e mostra o seu ID ↓
#output: <function tag at 6x10206d1e0> 

from functools import partial

# Cria a função picture a partir de tag fixando o primeiro argumentos com 'img' e o argumento nomeado cls com 'pic-frame' ↓
picture = partial(tag, 'img', cls='pic-frame')
print(picture(src="wumpus.jpeg")) # O picture funciona conforme esperado ↓
#output: '<img class="pic-frame" src="wumpus.jpeg" />'

print(picture) # partial() devolve um objeto functools.partial ↓
#output: functools.partial(<function tag at 0x10206d1e0>, 'img', cls'pic-frame')

print(picture.func) # Um objeto functools, partial tem atributos que possibilitam ter acesso à função original e aos argumentos fixos ↓
#output: <function tag at 0x10206d1e0>

print(picture.args)
#output: ('img',)

print(picture.keywords)
#output: ('cls': 'pic-frame')

```

</details>
</br>
