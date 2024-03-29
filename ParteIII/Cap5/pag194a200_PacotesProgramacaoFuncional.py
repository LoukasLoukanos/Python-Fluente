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
