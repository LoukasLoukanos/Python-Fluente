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