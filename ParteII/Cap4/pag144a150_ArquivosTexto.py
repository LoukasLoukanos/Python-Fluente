import os
print(os.stat('cafe.txt').st_size) # os.stat devolve a informação de que o arquivo contém 5 bytes; UTF-8 codifica 'e' com 2 bytes: 0xc3 e Oxa9.
#output: 5



fp = open('cafe.txt', 'w', encoding='utf-8') # Por padrão, open opera em modo texto e devolve um objeto TextIOkrapper.
print(fp)
#output: <_io.TextIOWrapper name='cafe.txt' mode='w' encoding='utf-8'> 

print(fp.write('café')) # O método write em um TextI0Wrapper devolve o número de caracteres Unicode escritos
#output: 4

fp.close()



fp2 = open('cafe.txt') # Abrir um arquivo-texto sem uma codificação explícita devolve um TextIOHrapper com a codificação definida com um default conforme a localidade.
print(fp2)
#output: <to.TextIOwrapper name='cafe.txt' node='r' encoding='cp1252'>

print(fp2.encoding) # Um objeto TextIOWrapper tem um atributo de codificação que você pode inspecionar: cp1252 nesse caso.
#output: 'cp1252'

print(fp2.read()) # Na codificação cp1252 do Windows, o byte 0xc3 é um "A" (A com til) e Oxa9 é o símbolo de copyright.
#output: 'cafÃ©

fp2.close()



fp3 = open('cafe.txt', encoding='utf-8') # Abre o mesmo arquivo com a codificação correta.
print(fp3)
#output: <to.TextIOWrapper name='cafe.txt' node='r' encoding="utf-8">

print(fp3.read()) # O resultado esperado: os mesmos quatro caracteres Unicode para 'café'.
#output: 'café'

fp3.close()



fp4 = open('cafe.txt', 'rb') # A flag 'rb' abre um arquivo para leitura em modo binário.
print(fp4)
#output: <to.BufferedReader name='cafe.txt'>   → (O objeto devolvido é um BufferedReader, e não um TextIOWrapper.)

print(fp4.read()) # Leitura que retorna bytes, conforme esperado.
#output: b'caf\xc3\xa9'
 
fp4.close()





#———————————————————————————————————————————————————————————————————————————————————————————————————
#Várias configurações do SO afetam a codigicação default para I/O em Python:

import sys, locale

expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """

my_file = open('dummy', 'w')

for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))

'''
output em GNULinux (Ubuntu 14.040) e em  OSX (Mavericks 10.9):
 locale.getpreferredencoding() -> 'utf-8'
                 type(my_file) -> <class '_io.TextIOWrapper'>
              my_file.encoding -> 'utf-8'
           sys.stdout.isatty() -> True
           sys.stdout.encoding -> 'utf-8'
            sys.stdin.isatty() -> True
            sys.stdin.encoding -> 'utf-8'
           sys.stderr.isatty() -> True
           sys.stderr.encoding -> 'utf-8'
      sys.getdefaultencoding() -> 'utf-8'
   sys.getfilesystemencoding() -> 'utf-8' 


output no Windows 7:
 locale.getpreferredencoding() -> 'cp1252'........................(é a configuração mais importante)
                 type(my_file) -> <class '_io.TextIOWrapper'>
              my_file.encoding -> 'cp1252'........................(arquivos de texto usam getpreferredencoding() por padrão)
           sys.stdout.isatty() -> True............................(a saídad está sendo enviada para o console)
           sys.stdout.encoding -> 'cp850'.........................(igual a configuração do console)
            sys.stdin.isatty() -> True
            sys.stdin.encoding -> 'cp850'
           sys.stderr.isatty() -> True
           sys.stderr.encoding -> 'cp850'
      sys.getdefaultencoding() -> 'utf-8'
   sys.getfilesystemencoding() -> 'mbcs' 


output no Windows 11:
 locale.getpreferredencoding() -> 'cp1252'
                 type(my_file) -> <class '_io.TextIOWrapper'>
              my_file.encoding -> 'cp1252'
           sys.stdout.isatty() -> True
           sys.stdout.encoding -> 'utf-8'
            sys.stdin.isatty() -> True
            sys.stdin.encoding -> 'utf-8'
           sys.stderr.isatty() -> True
           sys.stderr.encoding -> 'utf-8'
      sys.getdefaultencoding() -> 'utf-8'
   sys.getfilesystemencoding() -> 'utf-8' 
'''