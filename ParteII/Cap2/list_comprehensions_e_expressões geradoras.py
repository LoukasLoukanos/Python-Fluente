'''

 List comprehensions(listcomps): 
    para o tipo de sequência embutida list.

 Expressões geradoras(genexps): 
    para todos os demais tipos de sequências embutidas.

'''

#_________________________________________________________________
#lista de códigos Unicode(codepoints) sem usar list comprehension:
symbols = '$)!@|'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print("sem uasr list comprehension:", codes)

#lista de códigos Unicode(codepoints) usando list comprehension:
symbols2 = '$)!@|'
codes2 = [ord(symbol2) for symbol2 in symbols2]#list comprehension

print("usando list comprehension:  ", codes2)

#_________________________________________________________________________________________
#em python 3 as list comprehensions e as epressões geradoras têm seu próprio escopo local,
x = 'ABC'
dummy = [ord(x) for x in x]#list comprehension possui escopo local,
print(x)#por isso, o valor de x foi preservado,
print(dummy)#e a list comprehension gera a lista esperada.
