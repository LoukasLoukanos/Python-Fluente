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
