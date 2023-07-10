## **Visão geral das sequências embutidas............Pág. 45**

### ***SEQUÊNCIAS EMBUTIDAS:***
|  | MUTÁVEIS(aceitam mudanças) | IMUTÁVEIS(não aceitam mudanças) |
|:-:|:-:|:-:|
| SIMPLES(armazenam itens de um só tipo) | bytearray, array, memoryview | str, bytes |
| CONTAINER(armazenam itens de tipos diferentes) | list, deque | tuple |

#### **SIMPLES:**
  - Mais compactas, rápidas e fáceis de usar.
  - Limitadas ao armazenamento de dados atômicos como números, caracteres e bytes.

#### **CONTAINER:**
  - Mais flexíveis.
  - Não recomendadas para armazenar objetos mutáveis.

→ Como um exemplo, o tipo mais básico de sequência é list, um container mutável.
</br>


## **List comprehensions e expressões geradoras............Pág. 46**
| List comprehensions(listcomps) | Expressões geradoras(genexps) |
|:-:|:-:|
| para o tipo de sequência embutida list | para todos os demais tipos de sequências embutidas |
## **List comprehensions e legibilidade............Pág. 46**
```python
#___Sem usar list comprehension(listcomps):______
from array import array
from msilib.schema import ODBCAttribute

symbols = '$)!@|' # códigos Unicode(codepoints)
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print("Sem usar list comprehension:", codes)


#___Usando list comprehension(listcomps):______
symbols2 = '$)!@|' # códigos Unicode(codepoints)
codes2 = [ord(symbol2) for symbol2 in symbols2] # list comprehension
print("Usando list comprehension:  ", codes2)


#___Usando expressão geradora(genexp):______
symbols = '$)!@|'
t = tuple(ord(symbol) for symbol in symbols) # com um argumento não é necessário suplicar parênteses para a expressão geradora
import array
a = array.array('I', (ord(symbol) for symbol in symbols)) # com mais de um argumento é necessário usar parênteses nas expressões geradoras
print("Usando expressão geradora duplicando parênteses", t, " Sem duplicar parênteses", a)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes): # genexp 
    print("Usando expressão geradora em laço for", tshirt) # graças à expressão geradora é gerado uma saída que não precisa ser armazenada na memória, isso evitou o custo de criar uma lista de itens somente para alimentar o laço for.


#___Em python 3 as list comprehensions e as epressões geradoras têm seu próprio escopo local,
x = 'ABC'
dummy = [ord(x) for x in x] # list comprehension possui escopo local,
print("Valor da variável preservada fora do escopo", x) # por isso, o valor de x foi preservado,
print("Valor da variável modificada apenas dentro do escopo", dummy) # e a list comprehension gera a lista esperada.

```
</br>


## **Comparação entre listcomps e map/filter............Pág. 48**
## **Produtos cartesianos............Pág. 49**
## **Expressões geradoras............Pág. 50**
## **Tuplas não são apenas listas imutáveis............Pág. 52**
## **Tuplas como registros............Pág. 52**
## **Desempacotamento de tuplas............Pág. 53**
## **Desempacotamento de tuplas aninhadas............Pág. 55**
## **Tuplas nomeadas............Pág. 56**
## **Tuplas como listas imutáveis............Pág. 58**
## **Fatiamento............Pág. 59**
## **Por que as fatias e os intervalos excluem o último item............Pág. 59**
## **Objetos slice............Pág. 60**
## **Fatiamento multidimensional e reticências............Pág. 62**
## **Atribuição de valores a fatias............Pág. 62**
## **Usando + e * com sequências............Pág. 63**
## **Criando listas de listas............Pág. 64**
## **Atribuições combinadas e sequências............Pág. 65**
## **O enigma da atribuição +=............Pág. 67**
## **list.sort e a função embutida sorted............Pág. 69**
## **Administrando sequências ordenadas com bisect............Pág. 71**
## **Pesquisando com bisect............Pág. 71**
## **Inserção com bisect.insort............Pág. 74**
## **Quando uma lista não é a resposta............Pág. 75**
## **Arrays............Pág. 75**
## **Memory Views............Pág. 78**
## **NumPy e SciPy............Pág. 80**
## **Deques e outras filas............Pág. 82**
