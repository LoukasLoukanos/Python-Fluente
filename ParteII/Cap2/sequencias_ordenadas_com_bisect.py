# Módulo bisect oferece duas funções — bisect e insort— que usam algoritmo 
# de busca binária para pesquisar e inserir itens em sequências ordenadas.
#
# Demonstração de uso do módulo bisect____________________________________
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # usa a função bisec escolhida para obter o ponto de inserção
        offset = position * '  |'  # cria padrão de barras verticais proporcionais a offset
        print(ROW_FMT.format(needle, position, offset)) # exibe as linhas formatadas mostrando o valor de needle e o ponto de inserção 

if __name__ == '__main__':

    if sys.argv[-1] == 'left':    # escolhe a função bisect a ser usada de acordo com o último argumento da linha de comando
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)  # exibe um cabeçalho com o nome da função selecionada
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

''' output:
DEMO: bisect_right
haystack ->  1  4  5  6  8 12 15 20 21 23 23 26 29 30
31 @ 14      |  |  |  |  |  |  |  |  |  |  |  |  |  |31
30 @ 14      |  |  |  |  |  |  |  |  |  |  |  |  |  |30
29 @ 13      |  |  |  |  |  |  |  |  |  |  |  |  |29
23 @ 11      |  |  |  |  |  |  |  |  |  |  |23
22 @  9      |  |  |  |  |  |  |  |  |22
10 @  5      |  |  |  |  |10
 8 @  5      |  |  |  |  |8
 5 @  3      |  |  |5
 2 @  1      |2
 1 @  1      |1
 0 @  0    0
'''