# adapted from Alex Martelli's example in "Re-learning Python"
# http://www.aleax.it/Python/accu04_Relearn_Python_alex.pdf
# (slide 41) Ex: lines-by-word file index

# BEGIN INDEX0
"""Build an index mapping word -> list of occurrences"""

import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}

with open(sys.argv[1], encoding='utf-8') as fp: #with↓; as→alias(apelido)
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)

            occurrences = index.get(word, [])  # O btêm a lista de ocorrências para word, ou [] se essa palavra não for encontrada
            occurrences.append(location)       # Concatena a nova posição para ocurrences 
            index[word] = occurrences          # Coloca occurrences alterado no dicionário index; isso implica uma segunda busca em index
'''
with é usado para garantir finalização de recursos adquiridos
No exemplo citado deve ficar algo parecido com isto internamente:
try:
    __enter__()
    open(sys.argv[1], encoding='utf-8') as fp:
        #bloco de códigos
finally:
    __exit__()
'''

# print in alphabetical order
for word in sorted(index, key=str.upper):  # No argumento key= de sorted, não é chamando str.upper; mas apenas passado uma referência a esse método para que a função sorted possa usá-lo a fim de normalizar as palavras para a ordenação.
    print(word, index[word])
# END INDEX0
