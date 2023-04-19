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

# reduce _________________________________________________
#Fatorial Implementado com reduce e uma função anônima
from functools import reduce 
def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))


# reduce e mul _________________________________________________
# Para evitar o trabalho de escrever funções anónimas triviais como acima↑, o módulo 
# operator oferece equivalentes de funções para dezenas de operadores artiméticos.

# Fatorial implementado com reduce e operator.mul
from functools import reduce 
from operator import mul
def fact(n):
    return reduce(mul, range(1, n+1))


# itemgetter _________________________________________________
# Demo de itemgetter para ordenar uma lista de tuplas
metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.288889)), ('Mexico City', 'X', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 29.104, (40.888611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
from operator import itemgetter
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
