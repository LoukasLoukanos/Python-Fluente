# adapted from Alex Martelli's example in "Re-learning Python"
# http://www.aleax.it/Python/accu04_Relearn_Python_alex.pdf
# (slide 41) Ex: lines-by-word file index


'''
Explicação de with:
with é usado para garantir finalização de recursos adquiridos
No exemplo citado deve ficar algo parecido com isto internamente:
try:
    __enter__()
    open(sys.argv[1], encoding='utf-8') as fp:
        #bloco de códigos
finally:
    __exit__()
'''

import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}

'''
♦ OBJETIVO:________________________________________________________________________
Demonstrar um código que satisfaça o exemplo abaixo, [FAZENDO APENAS UMA BUSCA].
    if key not in my_dict:           → 1°BUSCA
        my_dict[key] = []
    my_dict[key].append(new_value)   → 2°BUSCA
'''

#MANEIRA 1[DUAS BUSCAS]:
with open(sys.argv[1], encoding='utf-8') as fp: # with↓; as→alias(apelido)
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)

            # MANEIRA 1: → com .get(word, [])
            occurrences = index.get(word, [])  # Obtêm a lista de ocorrências para word, ou [] se essa palavra não for encontrada
            occurrences.append(location)       # Concatena a nova posição para ocurrences 
            index[word] = occurrences          # Coloca occurrences alterado no dicionário index; isso [IMPLICA UMA SEGUNDA BUSCA] em index

# MANEIRA 2[UMA BUSCA]:
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            
            # MANEIRA 2: → com .setdefault
            index.setdefault(word, []).append(location)  # Obtêm a lista de ocorrências para word, ou [] se essa palavra não for encontrada; setdefault devolve o valor, portanto poderá ser atualizada [SEM EXIGIR UMA SEGUNDA BUSCA]).


'''
♦ CONCLUSÃO:________________________________________________________________________
A MANEIRA 2:
    my_dict.setdefault(key, []).append(new_value)   → UMA ÚNICA BUSCA

É EQUIVALENTE À:
    if key not in my_dict:           → 1°BUSCA
        my_dict[key] = []
    my_dict[key].append(new_value)   → 2°BUSCA

COM EXCEÇÃO DE QUE .setdefault FAZ TUDO COM [UMA ÚNICA BUSCA]
'''


# print in alphabetical order
for word in sorted(index, key=str.upper):  # No argumento key= de sorted, não é chamando str.upper; mas apenas passado uma referência a esse método para que a função sorted possa usá-lo a fim de normalizar as palavras para a ordenação.
    print(word, index[word])
# END INDEX0