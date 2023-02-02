'''
A maneira-padrão de ordenar textos que não sejam ASCII em Python é por meio da função locale.strxfrm, que, de acordo com a documentação do módulo locale, "transforma uma string em outra para ser usada em comparações que levem em conta a localidade (locale)".
'''

import locale

# É necessário chamar setlocale(LC_COLLATE, "sua localidade") antes de usar locale.strxfrm como chave ao ordenar:
locale.setlocale(locale.LC_COLLATE, 'pt BR.UTF-8') #habilita locale.strxfrm definindo uma localidade adequada para a sua aplicação

#Em GNU/Linux (Ubuntu 14.04), com a localidade pt_BR, a sequência de comandos funciona:
fruits = ['caju', 'atenota', 'caja', 'açat', 'acerola']

sorted_fruits = sorted(fruits, key=locale.strxfrm)

sorted_fruits 
#output: ['açat', 'acerola', 'atenota', 'cajá', 'caju']