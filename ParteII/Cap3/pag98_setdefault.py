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
import collections #para collections.defaultdict()

WORD_RE = re.compile(r'\w+')

index = {}

'''
♦ OBJETIVO:__________________________________________________________________________________________
Demonstrar um código que satisfaça o exemplo do uso do mapeamento abaixo, [FAZENDO APENAS UMA BUSCA].
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

            # MANEIRA 1: com my_dict.get(k, [default])   →   Obtém item com a chave k; devolve default ou None se estiver ausente (pag97_metodos_de_mapeamento.py).
            occurrences = index.get(word, [])  # 1°BUSCA: Obtêm a lista de ocorrências para word, ou [] se essa palavra não for encontrada
            occurrences.append(location)       # Concatena a nova posição para ocurrences 
            index[word] = occurrences          # 2°BUSCA: Coloca occurrences alterado no dicionário index; isso [IMPLICA UMA SEGUNDA BUSCA] em index

#ou MANEIRA 2[UMA BUSCA]:
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            
            # MANEIRA 2: → com my_dict.setdefault(k, [default])   →   Se k in my_dict, devolve my_dict[k]; caso contrário, define my_dict[k] = default e devolve esse valor (pag97_metodos_de_mapeamento.py).
            index.setdefault(word, []).append(location)  # Obtêm a lista de ocorrências para word, ou [] se essa palavra não for encontrada; setdefault devolve o valor, portanto poderá ser atualizada [SEM EXIGIR UMA SEGUNDA BUSCA]).


'''
♦ CONCLUSÃO:__________________________________________________________________________________________
A MANEIRA 2:
    my_dict.setdefault(key, []).append(new_value)   → UMA ÚNICA BUSCA

É EQUIVALENTE À:
    if key not in my_dict:           → +1 BUSCA
        my_dict[key] = []         → +1 (ou não)
    my_dict[key].append(new_value)   → +1 BUSCA

COM EXCEÇÃO DE QUE .setdefault FAZ TUDO COM [UMA ÚNICA BUSCA]
'''

# print in alphabetical order
for word in sorted(index, key=str.upper):  # No argumento key= de sorted, não é chamando str.upper; mas apenas passado uma referência a esse método para que a função sorted possa usá-lo a fim de normalizar as palavras para a ordenação.
    print(word, index[word])
# END INDEX0


'''
____________________________________________________________________________________________________________________________________________
→ o mapeamento defaultdict devolve valores predefinidos quando chaves são ausentes, pode ser usado no lugar do método setdefault.
dado um defaultdict vazio criado como dd = defaultdict(list), se 'new-key' não estiver em dd, a expressão dd['new-key'] executará os passos:
    •Chama list() para criar uma nova lista.
    •Insere a lista em dd usando 'new-key' como chave.
    •Devolve uma referência a essa lista.
'''
WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)     # Cria um defaultdict com o construtor list como default_factory
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location)  # Se word não estiver inicialmente em index, default_factory será chamado para gerar o valor
                                          # ausente, que, neste caso, é uma list vazia; ela será então atribuida a index[word] e
                                          # devolvida, de modo que a operação .append(location) sempre será bem-sucedida.

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])
# END INDEX0