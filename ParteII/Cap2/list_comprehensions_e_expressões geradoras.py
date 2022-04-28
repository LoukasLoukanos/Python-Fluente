'''

 List comprehensions(listcomps): 
    para o tipo de sequência embutida list.

 Expressões geradoras(genexps): 
    para todos os demais tipos de sequências embutidas.

'''

#________________________________________
# Sem usar list comprehension(listcomps):
from array import array
from msilib.schema import ODBCAttribute

symbols = '$)!@|' # códigos Unicode(codepoints)
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print("Sem usar list comprehension:", codes)

#______________________________________
# Usando list comprehension(listcomps):
symbols2 = '$)!@|' # códigos Unicode(codepoints)
codes2 = [ord(symbol2) for symbol2 in symbols2] # list comprehension
print("Usando list comprehension:  ", codes2)

#___________________________________
# Usando expressão geradora(genexp):
symbols = '$)!@|'
t = tuple(ord(symbol) for symbol in symbols) # com um argumento não é necessário suplicar parênteses para a expressão geradora
import array
a = array.array('I', (ord(symbol) for symbol in symbols)) # com mais de um argumento é necessário usar parênteses nas expressões geradoras
print("Usando expressão geradora duplicando parênteses", t, " Sem duplicar parênteses", a)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes): # genexp 
    print("Usando expressão geradora em laço for", tshirt) # graças à expressão geradora é gerado uma saída que não precisa ser armazenada na memória, isso evitou o custo de criar uma lista de itens somente para alimentar o laço for.

#_________________________________________________________________________________________
# Em python 3 as list comprehensions e as epressões geradoras têm seu próprio escopo local,
x = 'ABC'
dummy = [ord(x) for x in x] # list comprehension possui escopo local,
print("Valor da variável preservada fora do escopo", x) # por isso, o valor de x foi preservado,
print("Valor da variável modificada apenas dentro do escopo", dummy) # e a list comprehension gera a lista esperada.
