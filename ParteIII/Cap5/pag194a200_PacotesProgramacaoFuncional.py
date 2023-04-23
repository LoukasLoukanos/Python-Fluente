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
# •reduce de ♦functools: reduce é uma função do módulo functools em Python que permite reduzir uma sequência de valores a um único valor aplicando uma função cumulativa que combina cada elemento da sequência com o resultado anterior.

# Fatorial Implementado com reduce e uma função anônima
from functools import reduce 
def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

#_________________________________________________________________________________
# •mul de ♦operator: mul é uma função do módulo operator em Python que retorna o produto de dois valores. Essa função é frequentemente usada em conjunto com a função reduce do módulo functools para calcular o produto de uma sequência de valores.

# Para evitar o trabalho de escrever funções anónimas triviais como acima↑, o módulo 
# operator oferece equivalentes de funções para dezenas de operadores artiméticos.

# Fatorial implementado com reduce e operator.mul
from functools import reduce 
from operator import mul
def fact(n):
    return reduce(mul, range(1, n+1))

#_________________________________________________________________________________
# •itemgetter de ♦operator: itemgetter é uma função do módulo operator em Python que retorna uma função que pode ser usada para recuperar um determinado item de uma sequência ou de um objeto. Essa função é especialmente útil quando se trabalha com objetos que têm muitos atributos e se deseja acessar apenas um ou alguns deles.

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
