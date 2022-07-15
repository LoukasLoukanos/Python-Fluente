'''
Módulo bisect oferece duas funções — bisect e insort— que usam algoritmo 
de busca binária para pesquisar e inserir itens em [sequências ordenadas].
sintaxe:
    este_indice = bisect.bisect(sequencia_ordenada, valor) → valor é inserido no índice correto da sequencia_ordenada. É retornado o valor desse índice o qual foi atribuido à este_indice
obs:
    bisect.bisect() é um alias para bisect.bisect_rigth(), que insere à direita do índice procurado; → bisect.bisect_left() insere à esquerda do índice.
'''
import bisect
import sys
# Demonstração de uso do módulo bisect____________________________________
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
        bisect_fn = bisect.bisect_left #bisect.bisect_left() insere à esquerda do índice procurado
    else:
        bisect_fn = bisect.bisect #bisect.bisect() é um alias para bisect.bisect_rigth(), que insere à direita do índice

    print('DEMO:', bisect_fn.__name__)  # exibe um cabeçalho com o nome da função selecionada
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

'''
output:
DEMO: bisect_right
haystack ->  1  4  5  6  8 12 15 20 21 23 23 26 29 30..........# sequência ordenada antes das inserções feitas pela função bisect
31 @ 14      |  |  |  |  |  |  |  |  |  |  |  |  |  |31........# ( 31 @ 14 ) → valor 31 inserido na posição de índice 14°, a coluna |31| representa a célula do índice.
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


# Exemplo de uso do módulo bisect em pesquisa de valores numéricos em tabelas:____________________________________
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'): #notas escolares A, B, C, D e F e parâmetros para cada 60,70,80,90
    i = bisect.bisect(breakpoints, score) # bisect.bisect() é um alias para bisect.bisect_rigth(), que insere à direita do índice procurado. É retornado o valor desse índice o qual é atribuido à i
    print('\n', score, "inserido no índice", i) # cada inserção considera os índices de breakpoits inalterável, ou seja, [60,70,80,90]
    print("nota", grades[i], "obtida para a nota", score)
    return grades[i]

print('\nTodas as notas:', [grade(score) for score in [33, 99, 77, 70 ,89, 90, 100]])

'''output:
 33 inserido no índice 0
nota F obtida para a nota 33

 99 inserido no índice 4
nota A obtida para a nota 99

 77 inserido no índice 2
nota C obtida para a nota 77

 70 inserido no índice 2
nota C obtida para a nota 70

 89 inserido no índice 3
nota B obtida para a nota 89

 90 inserido no índice 4
nota A obtida para a nota 90

 100 inserido no índice 4
nota A obtida para a nota 100

Todas as notas: ['F', 'A', 'C', 'C', 'B', 'A', 'A']
'''