## **Pág. 130 à 135............Falhas de caracteres | O essencial sobre bytes | Structs e memory views | Codificadores/decodificadores básicos**
<details>
<summary></summary>

Mapeame

```python
#___________________________CODIFICAÇÃO (ENCODING) E DECODIFICAÇÃO (DECODING)___________________________
s = 'café' #str café

print("\ntipo s:", type(s), "\nvalor s:", s, "\ntamanho s:", len(s))
'''
    tipo s: <class 'str'> 
    valor s: café
    tamanho s: 4
'''

#CODIFICAÇÃO (de str para bytes) usando a codificação UTF-8
b = s.encode('utf8')

print("\ntipo b:", type(b), "\nvalor b:", b, "\ntamanho b:", len(b))
'''output:
    tipo b: <class 'bytes'>
    valor b: b'caf\xc3\xa9'   →   (literais do tipo bytes começam com um prefixo b)
    tamanho b: 5   →   (o objeto bytes na variável b tem cinco bytes pois o codepoint do caractere "é" é codificado com dois bytes em UTF-8)
'''

#DECODIFICAÇÃO (de bytes para str) usando a codificação UTF-8
b.decode('utf8')


#____________________________________SEQUÊNCIA COMO BYTES E COMO BYTEARRAY____________________________________
#_________SEQUÊNCIA COMO BYTES_________
cafe =  bytes('café', encoding='utf8') #bytes podem ser construído a partir de uma str, dada uma CODIFICAÇÃO
print("\ntipo cafe:", type(cafe), "\nvalor cafe:", cafe, "\ntamanho cafe:", len(cafe), "\n")
'''output:
    tipo cafe: <class 'bytes'>
    valor cafe: b'caf\xc3\xa9'
    tamanho cafe: 5
'''

'''cada item é um inteiro em range(256): 
Por exemplo, a=97, b=98, c=99, d=100, e=101, f=102, ..., \xc3=195, ..., \xa9=169, ...até256.
→ Obs: esses caracteres em utf-8 são representados por "índices", como em Unicode, e alguns até coicidem (a=97 em utf-8 e em Unicode). 
→ Nesse caso (em UTF-8) o par de bytes \xc3=195 + \xa9=169 representa o caractere "é". Já o valor \xc3=195 sozinho não representa um caractere válido.
→ "\xc3"=195 é o mesmo que "0xC3"=195 → '\x' e '0x' representam que está em hexadecimal, e 'C3' é o valor hexadecimal que é igual a 195 em deciaml)'''
print("cafe[0]: ", cafe[0]) #output: 99  → é o "índice" que representa "c" em utf-8 (o mesmo para Unicode)
print("cafe[1]: ", cafe[1]) #output: 97  → é o "índice" que representa "a" em utf-8 (o mesmo para Unicode)
print("cafe[2]: ", cafe[2]) #output: 102 → é o "índice" que representa "f" em utf-8 (o mesmo para Unicode)
print("cafe[3]: ", cafe[3]) #output: 195 → é o "índice" que representa o byte em hexadecimal "\xc3" ("0xC3") em utf-8 (em Unicode seria 'Á')
print("cafe[4]: ", cafe[4]) #output: 169 → é o "índice" que representa o byte em hexadecimal "\xc3" ("0xC3") em utf-8 (em Unicode seria '©')

#fatias de bytes também são bytes — mesmo as fatias com um único byte:
print("cafe[:0]: ", cafe[:0]) #output: b''   →   (literais do tipo bytes começam com um prefixo b)
print("cafe[:1]: ", cafe[:1]) #output: b'c'
print("cafe[:2]: ", cafe[:2]) #output: b'ca'
print("cafe[:3]: ", cafe[:3]) #output: b'caf'
print("cafe[:4]: ", cafe[:4]) #output: b'caf\xc3'
print("cafe[:5]: ", cafe[:5]) #output: b'caf\xc3\xa9'


#_________SEQUÊNCIA COMO BYTEARRAY_________
#não existe uma sintaxe literal para bytearray: eles são mostrados como bytearray(), com um literal bytes como argumento:
cafe_arr = bytearray(cafe)
print("\ntipo cafe_arr:", type(cafe_arr), "\nvalor cafe_arr:", cafe_arr, "\ntamanho cafe_arr:", len(cafe_arr), "\n")
'''output:
    tipo cafe: <class 'bytearray'>
    valor cafe: b'caf\xc3\xa9'
    tamanho cafe: 5
'''

#cada item é um inteiro em range(256):
print("cafe_arr[0]: ", cafe_arr[0]) #output: 99
print("cafe_arr[1]: ", cafe_arr[1]) #output: 97
print("cafe_arr[2]: ", cafe_arr[2]) #output: 102
print("cafe_arr[3]: ", cafe_arr[3]) #output: 195
print("cafe_arr[4]: ", cafe_arr[4]) #output: 169

#fatias de bytearray também são bytearray — mesmo as fatias com um único bytearray:
print("cafe_arr[:0]: ", cafe_arr[:0]) #output: bytearray''   →   (literais do tipo bytes começam com um prefixo bytearray)
print("cafe_arr[:1]: ", cafe_arr[:1]) #output: bytearray'c'
print("cafe_arr[:2]: ", cafe_arr[:2]) #output: bytearray'ca'
print("cafe_arr[:3]: ", cafe_arr[:3]) #output: bytearray'caf'
print("cafe_arr[:4]: ", cafe_arr[:4]) #output: bytearray'caf\xc3'
print("cafe_arr[:5]: ", cafe_arr[:5]) #output: bytearray'caf\xc3\xa9'

print("cafe[-1:]: ", cafe_arr[-1:]) #output: bytearray(b'\xa9')


#____________________________________MÉTODO fromhex PARA SEQUÊNCIAS BINÁRIAS____________________________________

# CODIFICAÇÃO (de hex para bytes) usando o método fromhex que cria uma sequência binária 
# interpretando [pares] de dígitos hexadeximais [opcionalmente separados com espaços]:
f = bytes.fromhex('31 4B CE A9')

print("\ntipo f:", type(f), "\nvalor f:", f, "\ntamanho b:", len(f))
'''output:
    tipo f: <class 'bytes'>
    valor f: b'1K\xce\xa9'
    tamanho b: 4
'''

#DECODIFICAÇÃO (de bytes para str) usando a codificação UTF-8
f = f.decode('utf8')
print("\ntipo f:", type(f), "\nvalor em utf-8:", f, "\ntamanho b:", len(f))
'''output:
    tipo f: <class 'str'>
    valor f: 1KΩ
    tamanho b: 3
'''

```

</details>
</br>


## **Pág. 136 à 143............Entendendo os problemas de codificação/decodificação | Lidando com UnicodeEncodeError | Lidando com UnicodeDecodeError | SyntaxError ao carregar módulos com codificação inesperada | Como descobrir a codificação de uma sequência de bytes | BOM: um gremlin útil**
<details>
<summary></summary>

```python
city = 'São Paulo'

city.encode('utf_8') # a codificação não acarreta em erro
city.encode('utf_16') # a codificação não acarreta em erro
city.encode('iso8859_1') # a codificação não acarreta em erro

city.encode('cp437')
'''a codificação acarreta em erro no caractere 'ã':
output:
    ...line 12, in encode return codecs.charmap_encode(input,errors,encoding_map) UnicodeEncodeError: 
    'charmap' codec can't encode character '\xe3' in position 1: character maps to <undefined>...
'''

#tratando erros_________________________________________
city.encode('cp437', errors='ignore') # errors='ignore' → ignora os erros ('ã', nesse caso)
# output: b'So Paulo'

city.encode('cp437', errors='replace') # errors='replace' → substitui os erros por '?'
# output: b'S?o Paulo'

city.encode('cp437', errors='xmlcharrefreplace') # errors='xmlcharrefreplace' → substitui os erros por entidades xml correspondentes
# output: b'S&#227;o Paulo'

```

</details>
</br>


## **Pág. 144 à 150............Lidando com arquivos-texto | Defaults de codificação: um hospício | Normalizando Unicode para comparações mais seguras**
<details>
<summary></summary>

```python
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

```

</details>
</br>


## **Pág. 151 à 158............Case folding | Funções utilitárias para comparações normalizadas | “Normalização” extrema: removendo acentos**
<details>
<summary></summary>

```python
#Normalizando Unicode: comparações mais seguras_______________________________________________________________________________________________________________________________________

from unicodedata import normalize
'''
 O primeiro argumento de normalize suporta quatro trings: 
    'NFC' → compõe de modo equivalente... Gera a menor string equivalente aos códigos Unicode
    'NFD' → decompõe de modo equivalente... Expande os caracteres compostos em caracteres básicos, separando os caracteres combinados
    'NFKC' → compõe de modo compatível ... A letra k representa 'compatibility' (compatibilidade), portanto não promete equivalência
    'NFKD' → decompõe de modo compatível... A letra k representa 'compatibility' (compatibilidade), portanto não promete equivalência
 obs: normalize não formata (NORMALIZA), portanto NFKC e NFKD podem distorcer informações.
'''

# exemplos________________________________________________________________________________________________

# Usando (NFC) → "Compõe de modo equivalente":
cof = 'cafe\u0301'
cof = normalize('NFC', cof)
    # output: café

# Usando (NFD) → "Decompõe de modo equivalente":
cof = normalize('NFD', cof)
    # output: cafe\u0301


# Usando (NFKC) → "Compõe de modo compatível"
half = '⅛'
half = normalize('NFKC', half)
    #output: 1/2 → a função normalize não sabe nada sobre formatação, por isso essa saída

# Usando (NFKD) → "Decompõe de modo compatível"
half = normalize('NFKD', half)
    #output: ⅛ → a função normalize não sabe nada sobre formatação, por isso essa saída



# exemplos com funções______________________________________________________________________________________
def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)

def fold_equal(str1, str2):
    # casefold() faz a conversão do texto em letras minúsculas, com algumas transformações adicionais.
    return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold())


# Usando (NFC) → "Compõe":_________________________________
s1 = 'café'
s2 = 'cafe\u0301'
s1 == s2 #output: False

nfc_equal(s1, s2) #output: True → (pois (s1=café) == (s2 composto por NFC))

nfc_equal('A', 'a') #output: False → (não há o que gerar de nova string equivalente, pois 'a' não é a composição de 'A', ou vice-versa, em Unicode)


# Usando (NFC) → "Compõe":_________________________________
s3 = 'Straße'
s4 = 'strasse'
s3 == s4 #output: False

nfc_equal(s3, s4) #output: False → (não há o que gerar de nova string equivalente, pois 'ß' não é a composição de 'ss(minúsculo)', ou vice-versa, em Unicode)

fold_equal(s3, s4) #output: True → (pois casefold() faz a conversão do texto em letras minúsculas, com algumas transformações adicionais – nesse caso 'ß' virou 'ss' –)

fold_equal(s1, s2) #output: True 

fold_equal('A', 'a') #output: True → (pois casefold() converteu 'A' em 'a')




#Normalização Extrema: removendo acentos_______________________________________________________________________________________________________________________________________
import unicodedata
import string

#_________________________________________________________________________________
#FUNÇÃO PARA REMOVER TODAS AS MARCAS COMBINADAS
def shave_marks(txt):
    """Remove todas as marcas de diacríticos(acentos, cedolhas, etc)"""
    norm_txt = unicodedata.normalize('NFD', txt)  # Usando (NFD) → "Decompõe de modo equivalente"
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))  # filtra todas as marcas combinadas
    return unicodedata.normalize('NFC', shaved)  # Usando (NFC) → "Compõe de modo equivalente"
#_________________________________________________________________________________



#_________________________________________________________________________________
#FUNÇÃO PARA REMOVER MARCAS COMBINADAS DE CARACTERES LATINOS
def shave_marks_latin(txt):
    """Remove todas as marcas de diacríticos(acentos, cedolhas, etc) dos caracteres-base latinos"""
    norm_txt = unicodedata.normalize('NFD', txt)  # Usando (NFD) → "Decompõe de modo equivalente"
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base: # pula as marcas combinadas quando o caractere for latino
            continue  # ignora diacríticos(acentos, cedolhas, etc) em caracteres-base latinos
        keepers.append(c) # caso contrário mantém o caractere atual
        # se não é um caractere combinado, é um novo caractere base
        if not unicodedata.combining(c): # declara o novo caractere-base e determina se é latino
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved) # recompõe todos os caracteres
#_________________________________________________________________________________



#_________________________________________________________________________________
#FUNÇÃO PARA TRANSFORMAR ALGUNS SÍMBOLOS TIPOGRÁFICOS OCIDENTAIS EM ASCII 
single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""",  # Cria tabela de mapeamento para substituição de caractere para caractere.
                           """'f"*^<''""---~>""")

multi_map = str.maketrans({  # Cria tabela de mapeamento para substituição de caractere para string
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})

multi_map.update(single_map)  # Combina as tabelas de mapeamento.


def dewinize(txt):
    """Replace Win1252 symbols with ASCII chars or sequences"""
    return txt.translate(multi_map)  # dewinize não afeta texto ASCII ou latin1, somente os acréscimos da Microsoft ao latini em cp1252.


def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))     # Aplica dewintze e remove marcas de diacríticos. 
    no_marks = no_marks.replace('ß', 'ss')          # Substitui Eszett por "ss" (não estamos usando case fold nesse caso, pois queremos preservar a diferença entre letras maiúsculas e minúsculas).
    return unicodedata.normalize('NFKC', no_marks)  # Aplica a normalização NFKC para compor caracteres com seus códigos de compatibilidade Unicode.
#_________________________________________________________________________________



# Exemplos: Manipulando uma string com simbolos em `cp1252`:________________________
order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'

shave_marks(order)
#output: '“Herr Voß: • ½ cup of Œtker™ caffe latte • bowl of acai.”'

shave_marks_latin(order)
#output: '“Herr Voß: • ½ cup of Œtker™ caffe latte • bowl of acai.”'

dewinize(order)
#output: '"Herr Voß: - ½ cup of OEtker(TM) caffè latte - bowl of açaí."'

asciize(order)
#output: '"Herr Voss: - 1⁄2 cup of OEtker(TM) caffe latte - bowl of acai."'



# Exemplos: Manipulando uma string com caracteres acentuados gregos e latinos:_________
greek = 'Ζέφυρος, Zéfiro'

shave_marks(greek)
#output: 'Ζεφυρος, Zefiro'

shave_marks_latin(greek)
#output: 'Ζέφυρος, Zefiro'

dewinize(greek)
#output: 'Ζέφυρος, Zéfiro'

asciize(greek)
#output: 'Ζέφυρος, Zefiro'

```

</details>
</br>


## **Pág. 159 à 161............Ordenação de texto Unicode | Ordenação com o Unicode Collation Algorithm | Base de dados Unicode**
<details>
<summary></summary>

```python
'''
A maneira-padrão de ordenar textos que não sejam ASCII em Python é por meio da função locale.strxfrm, que, de acordo com a documentação do módulo locale, "transforma uma string em outra para ser usada em comparações que levem em conta a localidade (locale)".
'''

import locale #locale deve estar instalado no sistema operacional; se não estiver, setlocale levantará uma exceção locale.Error: unsupported locale setting

# É necessário chamar setlocale(LC_COLLATE, "sua localidade") antes de usar locale.strxfrm como chave ao ordenar:
locale.setlocale(locale.LC_COLLATE, 'pt BR.UTF-8') #habilita locale.strxfrm definindo uma localidade adequada para a sua aplicação

#Em GNU/Linux (Ubuntu 14.04), com a localidade pt_BR, a sequência de comandos funciona:
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']

sorted_fruits = sorted(fruits, key=locale.strxfrm)

sorted_fruits 
#output: ['açaí', 'acerola', 'atemoia', 'cajá', 'caju'] 
```

</details>
</br>


## **Pág. 162 e 163............APIs de modo dual para str e bytes | str versus bytes em expressões regulares**
<details>
<summary></summary>

```python
# BEGIN NUMERICS_DEMO
import unicodedata #O módulo unicodedata do Python fornece acesso a informações sobre caracteres Unicode, incluindo seu nome, número, propriedades e classificação. 
import re

'''
Abaixo uma descrição de quatro métodos úteis ao trabalhar com caracteres Unicode, especialmente quando se lida com scripts e idiomas que possuem representações diferentes de números ou símbolos.

Métodos disponíveis no módulo unicodedata:
→ unicodedata.numeric(chr): retorna o valor numérico associado ao caractere chr no formato de uma string. Se o caractere não tiver um valor numérico associado, a função retorna None.
→ unicodedata.name(chr): retorna o nome formal do caractere chr segundo o padrão Unicode.

Métodos disponíveis no objeto de string e não no módulo unicodedata:
→ .isdigit(): retorna True se o caractere for uma cifra decimal, False caso contrário.
→ .isnumeric(): retorna True se o caractere for um símbolo numérico (como um número romano), False caso contrário.
'''

re_digit = re.compile(r'\d')

sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

for char in sample:
    print('U+%04x' % ord(char),                       # Código Unicode no formato U+0000.
          char.center(6),                             # Caractere centralizado em uma str de tamanho 6.
          're_dig' if re_digit.match(char) else '-',  # Mostra re_dig se o caractere corresponde à regex r'\d'.
          'isdig' if char.isdigit() else '-',         # Mostra isdig se char.isdigit() for True.
          'isnum' if char.isnumeric() else '-',       # Mostra isnum se char.isnumeric() for True.
          format(unicodedata.numeric(char), '5.2f'),  # Valor numérico formatado com largura 5 e duas casas decimais.
          unicodedata.name(char),                     # Nome do caractere Unicode.
          sep='\t')


'''
output: (obs: U+00bc é o número Unicode do hexadeximal \xbc...)

U+0031    1     re_dig  isdig   isnum    1.00   DIGIT ONE
U+00bc    ¼     -       -       isnum    0.25   VULGAR FRACTION ONE QUARTER
U+00b2    ²     -       isdig   isnum    2.00   SUPERSCRIPT TWO
U+0969    ३     re_dig  isdig   isnum    3.00   DEVANAGARI DIGIT THREE
U+136b    ፫     -       isdig   isnum    3.00   ETHIOPIC DIGIT THREE
U+216b    Ⅻ     -       -       isnum   12.00   ROMAN NUMERAL TWELVE
U+2466    ⑦     -       isdig   isnum    7.00   CIRCLED DIGIT SEVEN
U+2480    ⒀     -       -       isnum   13.00   PARENTHESIZED NUMBER THIRTEEN
U+3285    ㊅    -       -       isnum    6.00   CIRCLED IDEOGRAPH SIX

'''

```

</details>
</br>


## **Pág. 164 à 167............str versus bytes em funções de os**
<details>
<summary></summary>

```python
''' 
 ♦ Comparação entre o comportamento de expressões regulares str e bytes simples. ♦

→ Conclusão: Você pode usar expressões em str e em bytes, mas os bytes fora do intervalo ASCII serão tratados 
  como caracteres e não-palavra, já str serão tratados como dígitos ou letras Unicode além dos caracteres ASCII
'''

import re

re_numbers_str = re.compile(r'\d+')     # Expressão regular são do tipo str.
re_words_str = re.compile(r'\w+')       # Expressão regular são do tipo str.
re_numbers_bytes = re.compile(rb'\d+')  # Expressão regular do tipo bytes. → b de "byte"
re_words_bytes = re.compile(rb'\w+')    # Expressão regular do tipo bytes. → b de "byte"

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"  # Texto Unicode a ser pesquisado, contendo os dígitos em tamil para 1729 (a linha lógica continua até o parêntese direito).
            " as 1729 = 1³ + 12³ = 9³ + 10³.")        # Essa string é unida à anterior em tempo de compilação.

text_bytes = text_str.encode('utf_8')  # Uma string bytes é necessária para pesquisar com expressões regulares do tipo bytes. 

print('Text', repr(text_str), sep='\n  ')
print('Numbers')
print('  str  :', re_numbers_str.findall(text_str))      # O padrão str r'\d+' corresponde aos dígitos em tâmil e ASCIL.
print('  bytes:', re_numbers_bytes.findall(text_bytes))  # O padrão bytes rb'\d+' corresponde somente aos bytes ASCII para dígitos.
print('Words')
print('  str  :', re_words_str.findall(text_str))        # O padrão str r'w+' corresponde a letras, sobrescritos, tâmil e digitos ASCII.
print('  bytes:', re_words_bytes.findall(text_bytes))    # O padrão bytes rb'w+' corresponde somente aos bytes ASCII para letras e dígitos.

'''output:
Text
  'Ramanujan saw ௧௭௨௯ as 1729 = 1³ + 12³ = 9³ + 10³.'
Numbers
  str  : ['௧௭௨௯', '1729', '1', '12', '9', '10']
  bytes: [b'1729', b'1', b'12', b'9', b'10']
Words
  str  : ['Ramanujan', 'saw', '௧௭௨௯', 'as', '1729', '1³', '12³', '9³', '10³']
  bytes: [b'Ramanujan', b'saw', b'as', b'1729', b'1', b'12', b'9', b'10']
'''




import os
''' O kernel do GNU/Linux não foi projetado para lidar com Unkasle, portanto, no mundo real, ocê poderá encontrar nomes de arquivo compostos 
    de sequências de hyes que não são válidas em nenhum esquema sensato de codificação e não poderão ser codificadas para str '''

os.listdir('.') # O nome do segundo arquivo é "digits-of-t.txt" (com a letra grega pi).
#output: ['abc.txt', 'digits-of txt') 

os.listdir('.') # Dado um argumento byte, listdir devolve os nomes de arquivo como bytes: b'xcf\x89' é a codificação UTF-8 da letra grega pi).
#output: [b'abc.txt', b'digits-of-xcfx.txt')

''' 
Para ajudar no tratamento manual de sequências str ou bites que sejam nomes ou paths de arquivo, o módulo os oferece funções especiais de codificação e decodificacão:
→ fsencode(filename):
    Codifica filename (pode ser str ou bytes) para bytes usando o codec nomeado por sys.getfilesystemencoding() se 
    filename for do tipo str, caso contrário, devolve o filename do tipo bytes inalterado

fsdecode(filename):
    Decodifica filename (pode ser str ou bytes) para str usando o codec nomeado por sys.getfilesystemencoding() se 
    filename for do tipo bytes; caso contrário, devolve o filename do tipo str inalterado.
'''




''' Lidando com bytes inesperados ou codificações desconhecidas com o handler de erro de codec surrogateescape '''
import os

os.listdir('.') # Lista diretório com um nome de arquivo que não usa ASCII.
#output: ['abc.txt', 'digits-of-\xcf\x80.txt"]

os.ltstdir(b'.') # Vamos fingir que não sabemos qual é a codificação e obter os nomes dos arquivos como bytes.
#output: [b'abc.txt', b'digits-of-\xcf\x80..txt']

pi_name_bytes = os.listdir(b'.')[1] # pi_names_bytes é o nome do arquivo com o caractere pi.

pi_name_str = pi_name_bytes.decode('ascii', 'surrogateescape') # Decodifica-o para str usando o codec 'ascii' com 'surrogateescape'.
#output: 'digits-of-\udccf\udc80.txt'  → Cada byte que não é ASCII é substituído por um código Unicode substituto (surrogate): '\xcf\x80.' torna-se '\udccf\udc80'.

pi_name_str.encode('ascii', 'surrogateescape') # Codifica de volta para bytes ASCII: cada código Unicode substituto é trocado pelo byte que ele substituiu.
#output:  b'digits-of-\xcf\x80.txt" 

```

</details>
</br>