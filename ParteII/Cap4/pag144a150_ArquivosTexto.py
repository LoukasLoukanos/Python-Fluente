import os

# arquivo 'cafe.txt' com uma linha contendo a palavra 'café' escrita
print(os.stat('cafe.txt').st_size) # os.stat devolve a informação de que o arquivo contém 5 bytes;
#output: 5
#obs: → UTF-8 codifica 'é' com 2 bytes: \xc3\xa9 é 'c3' e 'a9' em hexadecimal para os caracteres 'e' e '´'

#_________Escrevendo no arquivo aberto com a codificação em utf-8 (arquivo 'cafe.txt' com uma linha contendo a palavra 'café' escrita)_________
fp = open('cafe.txt', 'w', encoding='utf-8') # Por padrão, open opera em modo texto e devolve um objeto TextIOkrapper.
print(fp)
#output: <_io.TextIOWrapper name='cafe.txt' mode='w' encoding='utf-8'> 

print(fp.write('café')) # O método write em um TextI0Wrapper devolve o número de caracteres Unicode escritos
#output: 4

fp.close()


#_________Lendo o arquivo aberto sem especificar a codificação (arquivo 'cafe.txt' com uma linha contendo a palavra 'café' escrita)_________
fp2 = open('cafe.txt') # Abrir um arquivo-texto sem uma codificação explícita devolve um TextIOHrapper com a codificação definida com um default conforme a localidade.
print(fp2)
#output: <to.TextIOwrapper name='cafe.txt' node='r' encoding='cp1252'>

print(fp2.encoding) # Um objeto TextIOWrapper tem um atributo de codificação que você pode inspecionar: cp1252 nesse caso.
#output: 'cp1252'

print(fp2.read()) # Na codificação cp1252 do Windows, o byte 0xc3 é um "Ã" (A com til) e Oxa9 é o símbolo de copyright.
#output: 'cafÃ©

fp2.close()


#_________Lendo o arquivo aberto com a codificação em utf-8 (arquivo 'cafe.txt' com uma linha contendo a palavra 'café' escrita)_________
fp3 = open('cafe.txt', encoding='utf-8') # Abre o mesmo arquivo com a codificação correta.
print(fp3)
#output: <to.TextIOWrapper name='cafe.txt' node='r' encoding="utf-8">

print(fp3.read()) # O resultado esperado: os mesmos quatro caracteres Unicode para 'café'.
#output: 'café'

fp3.close()


#_________Lendo o arquivo aberto em modo binário (arquivo 'cafe.txt' com uma linha contendo a palavra 'café' escrita)_________
fp4 = open('cafe.txt', 'rb') # A flag 'rb' abre um arquivo para leitura em modo binário.
print(fp4)
#output: <to.BufferedReader name='cafe.txt'>   → (O objeto devolvido é um BufferedReader, e não um TextIOWrapper.)

print(fp4.read()) # Leitura que retorna bytes, conforme esperado.
#output: b'caf\xc3\xa9'
#obs: → \xc3\xa9 é 'c3' e 'a9' em hexadecimal para os caracteres 'e' e '´' que formam 'é'
fp4.close()





'''————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
Várias configurações do SO afetam a codigicação default para I/O: Em GNU/Linux e em OSX, todas as codificações abaixo são definidas 
como UTF-8 por padrão, portanto o I/O trata todos os caracteres Unicode; em Windows, codificações diferentes são usadas no mesmo 
sistema, portanto existe muito mais chances de ocorrer erros de codificação.
'''

import sys, locale

my_file = open('dummy', 'w') # encoding omitido → o default será dado por locale.getpreferredencoding()

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
'''explicação da variável 'expressions':
locale.getpreferredencoding().......→ Retorna a codificação preferida do sistema operacional.
type(my_file).......................→ Retorna o tipo de objeto de 'my_file'.
my_file.encoding....................→ Obtém a codificação do objeto my_file.
sys.stdout.isatty().................→ Verifica se a saída padrão (sys.stdout) está associada a um terminal (TTY). Retorna True ou False se a saída estiver ou não conectada a um terminal.
sys.stdout.encoding.................→ Obtém a codificação da saída padrão (sys.stdout). Retorna a codificação usada para codificar a saída que é enviada para o terminal.
sys.stdin.isatty()..................→ Verifica se a entrada padrão (sys.stdin) está associada a um terminal (TTY). Retorna True ou False se a entrada estiver ou não vinda de um terminal.
sys.stdin.encoding..................→ Obtém a codificação da entrada padrão (sys.stdin). Retorna a codificação usada para decodificar a entrada provenientes do terminal.
sys.stderr.isatty().................→ Verifica se a saída de erro padrão (sys.stderr) está associada a um terminal (TTY). Retorna True ou False se a saída de erro estiver ou não conectada a um terminal.
sys.stderr.encoding.................→ Obtém a codificação da saída de erro padrão (sys.stderr). Retorna a codificação usada para codificar a saída de erro que é enviada para o terminal.
sys.getdefaultencoding()............→ Retorna a codificação padrão do sistema.
sys.getfilesystemencoding().........→ Retorna a codificação usada para interpretar nomes de arquivos no sistema de arquivos do sistema operacional.
'''

for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))

'''
output em GNULinux (Ubuntu 14.040) e em  OSX (Mavericks 10.9):
 locale.getpreferredencoding() -> 'utf-8'.........................(# a codificação preferida do sistema operacional)
                 type(my_file) -> <class '_io.TextIOWrapper'>.....(o tipo de objeto de 'my_file')
              my_file.encoding -> 'utf-8'.........................(a codificação do objeto my_file)
           sys.stdout.isatty() -> True............................(a saída padrão (sys.stdout) está associada a um terminal (TTY))
           sys.stdout.encoding -> 'utf-8'.........................(a codificação da saída padrão (sys.stdout))
            sys.stdin.isatty() -> True............................(a entrada padrão (sys.stdin) está associada a um terminal (TTY))
            sys.stdin.encoding -> 'utf-8'.........................(a codificação da entrada padrão (sys.stdin))
           sys.stderr.isatty() -> True............................(a saída de erro padrão (sys.stderr) está associada a um terminal (TTY))
           sys.stderr.encoding -> 'utf-8'.........................(a codificação da saída de erro padrão (sys.stderr))
      sys.getdefaultencoding() -> 'utf-8'.........................(a codificação padrão do sistema)
   sys.getfilesystemencoding() -> 'utf-8'.........................(a codificação usada para interpretar nomes de arquivos no sistema de arquivos do sistema operacional)


output no Windows 7:
 locale.getpreferredencoding() -> 'cp1252'........................(a codificação preferida do sistema operacional)
                 type(my_file) -> <class '_io.TextIOWrapper'>.....(o tipo de objeto de 'my_file')
              my_file.encoding -> 'cp1252'........................(a codificação do objeto my_file)
           sys.stdout.isatty() -> True............................(a saída padrão (sys.stdout) está associada a um terminal (TTY))
           sys.stdout.encoding -> 'cp850'.........................(a codificação da saída padrão (sys.stdout))
            sys.stdin.isatty() -> True............................(a entrada padrão (sys.stdin) está associada a um terminal (TTY))
            sys.stdin.encoding -> 'cp850'.........................(a codificação da entrada padrão (sys.stdin))
           sys.stderr.isatty() -> True............................(a saída de erro padrão (sys.stderr) está associada a um terminal (TTY))
           sys.stderr.encoding -> 'cp850'.........................(a codificação da saída de erro padrão (sys.stderr))
      sys.getdefaultencoding() -> 'utf-8'.........................(a codificação padrão do sistema)
   sys.getfilesystemencoding() -> 'mbcs'..........................(a codificação usada para interpretar nomes de arquivos no sistema de arquivos do sistema operacional)


output no Windows 11:
 locale.getpreferredencoding() -> 'cp1252'........................(a codificação preferida do sistema operacional)
                 type(my_file) -> <class '_io.TextIOWrapper'>.....(o tipo de objeto de 'my_file')
              my_file.encoding -> 'cp1252'........................(a codificação do objeto my_file)
           sys.stdout.isatty() -> True............................(a saída padrão (sys.stdout) está associada a um terminal (TTY))
           sys.stdout.encoding -> 'utf-8'.........................(a codificação da saída padrão (sys.stdout))
            sys.stdin.isatty() -> True............................(a entrada padrão (sys.stdin) está associada a um terminal (TTY))
            sys.stdin.encoding -> 'utf-8'.........................(a codificação da entrada padrão (sys.stdin))
           sys.stderr.isatty() -> True............................(a saída de erro padrão (sys.stderr) está associada a um terminal (TTY))
           sys.stderr.encoding -> 'utf-8'.........................(a codificação da saída de erro padrão (sys.stderr))
      sys.getdefaultencoding() -> 'utf-8'.........................(a codificação padrão do sistema)
   sys.getfilesystemencoding() -> 'utf-8'.........................(a codificação usada para interpretar nomes de arquivos no sistema de arquivos do sistema operacional)


_________CONCLUSÃO (texto gerado pela IA ChatGPT):_________
As configurações do sistema operacional podem afetar a codificação padrão para operações de entrada e saída (I/O), e existem diferenças significativas 
entre os sistemas operacionais GNU/Linux, macOS e Windows nesse aspecto. No caso do GNU/Linux e macOS, a maioria das distribuições e configurações padrão 
define a codificação para I/O como UTF-8. O UTF-8 é um formato de codificação que suporta uma ampla gama de caracteres Unicode, o que significa que é capaz 
de lidar com a maioria dos caracteres usados em diferentes idiomas e sistemas de escrita. Portanto, em sistemas GNU/Linux e macOS, é mais provável que as 
operações de I/O tratem corretamente os caracteres Unicode. 

No entanto, em sistemas Windows, a situação é um pouco diferente. O Windows usa diferentes codificações, dependendo das configurações e do contexto. Embora 
a codificação UTF-8 esteja se tornando mais comum e amplamente suportada no Windows, versões mais antigas do sistema operacional (como o Windows 7) e algumas 
configurações específicas podem usar codificações diferentes, como a codificação ANSI ou a codificação baseada na localidade do sistema. Essas codificações 
podem não suportar todos os caracteres Unicode, o que pode resultar em erros de codificação ao lidar com caracteres especiais ou não ASCII.

Portanto, em sistemas Windows, especialmente em versões mais antigas ou com configurações específicas, existe uma maior chance de ocorrerem erros de 
codificação ao realizar operações de I/O, especialmente quando envolve caracteres Unicode fora do conjunto suportado pela codificação padrão.

É importante ressaltar que a codificação padrão pode ser alterada em diferentes sistemas operacionais e depende das configurações e do contexto. 
Portanto, é sempre recomendado que os desenvolvedores lidem explicitamente com a codificação ao realizar operações de I/O, para garantir a correta 
manipulação de caracteres e evitar problemas de codificação.
'''
