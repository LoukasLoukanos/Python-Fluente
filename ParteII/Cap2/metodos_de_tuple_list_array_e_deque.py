'''
╔═══════════════════════════════════════════════════════╦═════════════════════════════════╦══════════════════════════════════╗
║................SEQUÊNCIAS EMBUTIDAS...................║...MUTÁVEIS(aceitam mudanças)....║.IMUTÁVEIS(não aceitam mudanças)..║
╠═══════════════════════════════════════════════════════╬═════════════════════════════════╬══════════════════════════════════╣
║SIMPLES(armazenam itens de um só tipo).................║..bytearray, array, memoryview...║............str, bytes............║
╠═══════════════════════════════════════════════════════╬═════════════════════════════════╬══════════════════════════════════╣
║CONTAINER(armazenam itens de tipos diferentes).........║...........list, deque...........║..............tuple...............║
╚═══════════════════════════════════════════════════════╩═════════════════════════════════╩══════════════════════════════════╝

SIMPLES:
• Mais compactas, rápidas e fáceis de usar.
• Limitadas ao armazenamento de dados atômicos como números, caracteres e bytes.

CONTAINER:
• Mais flexíveis.
• Não recomendadas para armazenar objetos mutáveis.


Objeto hashable é um ojeto capaz de possuir um hash (um id como sha1 ou MD5)
 ✓ Terá um valor de hash que não muda (possuirá um método __hash__())
 ✓ Será comparável com outros objetos (possuirá um método __eq__())
Condição para um objeto ser hashable:
 → Deve ser IMUTÁVEL — str, bytes e tuple (exceto se conter referências a objetos que não são hashable)—.
Nota: 
 → frozenset é uma função que transforma objetos MUTÁVEIS em IMUTÁVEIS.


Métodos de tuple, list, array e deque:________________________________________________________________________________________________________________________________________
● tuple aceita os métodos de list, com exceção do método __reversed__() e de todos os métodos que acrescentam ou removem itens, pois tuple é IMUTÁVEL.
● array é mais eficiente que list (exceto pela limitância de ser do tipo de sequência SIMPLES) para sequências contendo apenas tipo de valores numéricos.
● deque permite as regras de acesso FIFO e LIFO e é a sequência mais otimizada para inserção e remoção de itens das extremidades (centrais a latência é maior).
╔═══════════════════════════╦═══════════╦══════════╦═══════════╦═══════════╦══════════════════════════════════════════════════════════════════════════════════════════════════╗
║...........................║...tuple...║...list...║...array...║...deque...║..................................................................................................║
╠═══════════════════════════╬═══════════╬══════════╬═══════════╬═══════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
║s.__add__(s2)..............║.....♦.....║....♦.....║.....♦.....║...........║..s + s2 → concatenação...........................................................................║
║s.__iadd__(s2).............║...........║....♦.....║.....♦.....║.....♦.....║..s += s2 → concatenação in-place.................................................................║
║s.append(e)................║...........║....♦.....║.....♦.....║.....♦.....║..Concatena um elemento após o último.............................................................║
║s.appendleft(e)............║...........║..........║...........║.....♦.....║..Concatena um elemento à esquerda (antes do primeiro)............................................║
║s.byteswap()...............║...........║..........║.....♦.....║...........║..Troca os bytes de todos os itens do array para uma conversão de endianess.......................║
║s.clear()..................║...........║....♦.....║...........║.....♦.....║..Apaga todos os itens............................................................................║
║s.__contains__(e)..........║.....♦.....║....♦.....║.....♦.....║...........║..e in s..........................................................................................║
║s.copy()...................║...........║....♦.....║...........║...........║..Shallow copy (cópia rasa) da lista..............................................................║
║s.__copy__()...............║...........║..........║.....♦.....║.....♦.....║..Suporte para copy.copy(shallow copy ou copora rasa).............................................║
║s.count(e).................║.....♦.....║....♦.....║.....♦.....║.....♦.....║..Conta as ocorrências de um elemento.............................................................║
║s.__deepcopy__()...........║...........║..........║.....♦.....║...........║..Suporte otimizado para copy.deepcopy............................................................║
║s.__delitem__(p)...........║...........║....♦.....║.....♦.....║.....♦.....║..Remove o item da posição p......................................................................║
║s.extend(it)...............║...........║....♦.....║.....♦.....║.....♦.....║..Concatena itens do iterável it..................................................................║
║s.extendleft(i)............║...........║..........║...........║.....♦.....║..Adiciona itens do iterável i à esquerda.........................................................║
║s.fromfile(f, n)...........║...........║..........║.....♦.....║...........║..Concatena n itens do arquivo binário f interpretado como valores de máquina compactos...........║
║s.fromlist(l)..............║...........║..........║.....♦.....║...........║..Concatena itens da lista; se algum deles provocar um TypeError, nenhum valor será concatenado...║
║s.frombytes(b).............║...........║..........║.....♦.....║...........║..Concatena itens da sequência de bytes intepretada como valores de máquina compactos.............║
║s.__getitem__(p)...........║.....♦.....║....♦.....║.....♦.....║.....♦.....║..s[p] → obtém o item de uma posição..............................................................║
║s.__getnewargs__().........║.....♦.....║..........║...........║...........║..Suporte para serialização otimizada com pickle..................................................║
║s.index(e).................║.....♦.....║....♦.....║.....♦.....║...........║..Encontra a posição da primeira ocorrência de e..................................................║
║s.insert(p, e).............║...........║....♦.....║.....♦.....║...........║..Insere o elemento e antes do item na posição p..................................................║
║s.itemsize()...............║...........║..........║.....♦.....║...........║..Tamanho em bytes de cada item do array..........................................................║
║s.__iter__()...............║.....♦.....║....♦.....║.....♦.....║.....♦.....║..Obtém um iterador...............................................................................║
║s.__len__()................║.....♦.....║....♦.....║.....♦.....║.....♦.....║..len(s) → número de itens........................................................................║
║s.__mul__(n)...............║.....♦.....║....♦.....║.....♦.....║...........║..s * n → concatenação repetida...................................................................║
║s.__imul__(n)..............║...........║....♦.....║.....♦.....║...........║..s *= n → concatenação repetida in-place.........................................................║
║s.__rmul__(n)..............║.....♦.....║....♦.....║.....♦.....║...........║..n * s → concatenação repetida invertida (operador reverso)......................................║
║s.pop([p]).................║...........║....♦.....║.....♦.....║.....♦.....║..Remove e retorna o último item (por defalt) ou, opcionalmente, o item na posição p..............║
║s.popleft()................║...........║..........║...........║.....♦.....║..Remove e devolve o primeiro item................................................................║
║s.remove(e)................║...........║....♦.....║.....♦.....║.....♦.....║..Remove a primeira ocorrência do elemento com o valor de e.......................................║
║s.reverse()................║...........║....♦.....║.....♦.....║.....♦.....║..Inverte a ordem dos itens in-place..............................................................║
║s.__reversed__()...........║...........║....♦.....║...........║.....♦.....║..Obtém um iterador para percorrer os itens do último para o primeiro.............................║
║s.rotate(n)................║...........║....♦.....║...........║.....♦.....║..Move n itens de uma extremidade para a outra....................................................║
║s.__setitem__(p, e)........║...........║....♦.....║.....♦.....║.....♦.....║..s[p] = e → coloca e na posição p sobrescrevendo o item existente................................║
║s.sort([key], [reverse])...║...........║....♦.....║...........║...........║..Ordena itens in-place com os argumentos nomeados opcionais key e reverse........................║
║s.tobytes()................║...........║..........║.....♦.....║...........║..Devolve os itens como valores de máquina compactos em um objeto bytes...........................║
║s.tofile(f)................║...........║..........║.....♦.....║...........║..Salva os itens como valores de máquina compactos em um arquivo binário f........................║
║s.tolist().................║...........║..........║.....♦.....║...........║..Devolve os itens como objetos numéricos em uma lista............................................║
║s.typecode.................║...........║..........║.....♦.....║...........║..String de um caractere que identifica o tipo dos itens na linguagem C...........................║
╚═══════════════════════════╩═══════════╩══════════╩═══════════╩═══════════╩══════════════════════════════════════════════════════════════════════════════════════════════════╝
'''