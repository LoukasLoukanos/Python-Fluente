'''
A classe collections.deque é uma fila dupla thread-safe (segura para threads), criada para disponibilizar 
inserção e remoção rápidas de ambas as extremidades, proporcionando as regras de acesso FIFO e LIFO. 
Ela também é a opção adequada se houver necessidade de manter uma lista dos "últimos itens vistos", 
pois um deque pode ser limitado — ou seja, criado com um tamanho máximo — e, quando estiver cheio os 
itens serão descartados da extermidade oposta quando novos itens forem adicionados.'''
from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)
'''output: deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
→ O argumento maxlen opcional define o número máximo de itens permitido nessa
instância de deque; isso define um atributo de instância maxlen somente para leitura'''

dq.rotate(3)
print(dq)
#output: deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
dq.rotate(-4)
print(dq)
'''output: deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
→ Fazer a rotação (rotate()) com n > 0 retira os itens da extremidade direita e os insere 
na esquerda; quando n < 0, os itens serão retirados da esquerda e concatenados à direita.'''

dq.appendleft(-1)
print(dq)
'''output: deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
→ Concatenar em um deque que esteja cheio (len(d) == d.naxlen) faz com que os itens da outra 
exteremidade sejam descartados; observe na próxima linha que 0 foi descartado.'''

dq.extend([11, 22, 33])
print(dq)
'''output: deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)
→ Adicionar três itens à direita remove os valores -1,1 e 2 mais á esquerda.'''

dq.extendleft([10, 20, 30, 40])
print(dq)
'''output: deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)
→ Observe que extendleft(iter) funciona pela adição sucessiva de cada item do argumento iter 
à esquerda do deque; desse modo, a posição final dos itens estará invertida.'''
