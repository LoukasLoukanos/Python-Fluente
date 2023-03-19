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
