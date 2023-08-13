
## **Pág. 45............Visão geral das sequências embutidas**
<details>
<summary></📖></summary>

### ***SEQUÊNCIAS EMBUTIDAS:***
|  | MUTÁVEIS (mesmo id quando ocorre mudança) | IMUTÁVEIS (novo id quando ocorre "mudança" (na verdade subsituição)) |
|:-:|:-:|:-:|
| SIMPLES (armazenam itens de um só tipo) | bytearray, array, memoryview | str, bytes |
| CONTAINER (armazenam itens de tipos diferentes) | list, deque | tuple |

#### **SIMPLES:**
  - Mais compactas, rápidas e fáceis de usar.
  - Limitadas ao armazenamento de dados atômicos como números, caracteres e bytes.

#### **CONTAINER:**
  - Mais flexíveis.
  - Não recomendadas para armazenar objetos mutáveis.

→ Como um exemplo, o tipo mais básico de sequência é list, um container mutável.

</details>
</br>


## **Pág. 46............List comprehensions e expressões geradoras**
<details>
<summary></📖></summary>

| List comprehensions(listcomps) | Expressões geradoras(genexps) |
|:-:|:-:|
| para o tipo de sequência embutida list | para todos os demais tipos de sequências embutidas |

</details>
</br>


## **Pág. 46............List comprehensions e legibilidade**
<details>
<summary></📖></summary>

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

</details>
</br>


## **Pág. 48 à 52............Comparação entre listcomps e map/filter | Produtos cartesianos | Expressões geradoras | Tuplas não são apenas listas imutáveis | Tuplas como registros**

<details>
<summary></📖></summary>

```python
# 1° EXEMPLO
from pyparsing import line

lax_coordinates = (33.425, -118.408056) #latitude e longitude do Aeroporto Internacional de Londres.
print('    1° exemplo: ', type(lax_coordinates), lax_coordinates) #output: <class 'tuple'> (33.425, -118.408056) 

# 2° EXEMPLO
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014) #Dados sobre Tóquio: nome, ano poputação (milhões), mudança na população (%), área (km²)
print('    2° exemplo: ', type(city), city)#output:<class 'str'> Tokyo
print('    2° exemplo: ', type(year), year)#output:<class 'int'> 2003

# 3° EXEMPLO
traveler_ids = [('USA', '3115855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]#Uma lista de tuplas no formato (country_code, passport_number).
print('    3° exemplo: ', type(traveler_ids), traveler_ids)#output:<class 'list'> [('USA', '3115855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

# 4° EXEMPLO
for passport in sorted(traveler_ids):# À medida que fazemos uma iteração pela lista, o nome passport é associado à cada tupla.
    print('    4° exemplo: ', type(passport), '%s/%s' % passport)# O operador de formatação % entende as tuplas e trata cada item como um campo separado.
    #output:<class 'tuple'> BRA/CE342567, <class 'tuple'> ESP/XDA205856, <class 'tuple'> USA/3115855

# 5° EXEMPLO
for country, _ in traveler_ids:# O laço for sabe como obter os itens de uma tupla separadamente -isso é chamado de "desempacotamento" (unpacking). Nesse caso, não estamos interessados no segundo item, portanto ele é atribuído a_, que é uma variável comumente usada para capturar valores que não queremos usar.
    print('    5° exemplo: ', type(country), country)#output:<class 'str'> USA, <class 'str'> BRA, <class 'str'> ESP

```

</details>
</br>


## **Pág. 53............Desempacotamento de tuplas**
<details>
<summary></📖></summary>

```python
#atribuição paralela:
latitude, longitude = lax_coordinates

#troca (swap) de valores de duas variáveis sem usar uma variável temporária:
latitude, longitude = longitude, latitude
#revertendo:
latitude, longitude = longitude, latitude

#prefixar um argumento com um asterisco * ao chamar uma função:
divmod(20, 8)
t = (20, 8)
divmod(*t)#o prefixo asterisco * serve para informar que a variável contém todos os parâmetros exigidos por divmod, sem precisar separá-los por vírgulas.

#atribuição paralela com o prefixo asterisco *
a, *body, c, d = range(5) # → (a=0, [body = 1, 2], c=3, d=4)
print(a, *body, c, d) # output: 0, 1, 2, 3, 4

```

</details>
</br>


## **Pág. 55............Desempacotamento de tuplas aninhadas**
<details>
<summary></📖></summary>

```python
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # a tupla aninhada é um par de coordenadas
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

#format() é um dos métodos de formatação de string em Python3. Esse método nos permite concatenar elementos em uma string por meio da formatação posicional
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  # desempacotando as coordenadas atribuindo-as à tupla (latitude, longitude)
    if longitude <= 0: # condições de acesso....
        print(fmt.format(name, latitude, longitude))
```

</details>
</br>


## **Pág. 56 à 58............Tuplas nomeadas | Tuplas como listas imutáveis**
<details>
<summary></📖></summary>

```python
from collections import namedtuple #namedtuples contêm chaves como hash para um valor específico, oferecendo suporte ao acesso do valor tanto pela chave[key] como pela iteração[x]
City = namedtuple('City', 'name country population coordinates')
tokyo = City('tokyo', 'JP', population=36.933, coordinates=(36.689722, 139.691667))
print("acesso por chaves[keys]:\n", tokyo.name, tokyo.country, tokyo.population, tokyo.coordinates)
#↑ou↓
print("acesso por iteração[x]:\n", tokyo[0], tokyo[1], tokyo[2], tokyo[3], "\n......................") 
''' Output:
        —————————————————————
        acesso por chaves[keys]:
         tokyo JP 36.933 (36.689722, 139.691667)
        acesso por iteração[x]:
         tokyo JP 36.933 (36.689722, 139.691667) 
        —————————————————————
'''
#_fields retorna uma tupla com os nomes das [chaves] dos valores da classe namedtuple definida  
print('Retorno de _fields: ', City._fields) # output:('name', 'country', 'population', 'coordinates')

LatLong = namedtuple('LatLong', 'Lat Long') #Lat será a chave[key] do valor 28.613889; e Long será a chave[key] do valor 77.208889 ↓↓↓
delhi_data = ('Delhi NCR', 'IN', 21935, LatLong(28.613889, 77.208889))# LatLong(valor da chave [Lat], valor da chave[Long]) ↑↑↑

# _make() permite instanciar uma tupla nomeada a partir de um iterável.
delhi = City._make(delhi_data) # Os valores das chaves [Lat] e [Long] da namedtuple LatLong() serão, também, os valores da chave [coordinate] da namedtuple City.

 # _asdict() retorna um collections.OrderedDict , chaves e valores...
print('Retorno de _asdict(): ', delhi._asdict()) # output: Retorno de _asdict():  {'name': 'Delhi NCR', 'country': 'IN', 'population': 21935, 'coordinates': LatLong(Lat=28.613889, Long=77.208889)}

for key, value in delhi._asdict().items():
    print('hash [',key, ']', ' = ', value)
    ''' Output:
            hash [ name ]  =  Delhi NCR
            hash [ country ]  =  IN
            hash [ population ]  =  21935
            hash [ coordinates ]  =  LatLong(Lat=28.613889, Long=77.208889)
    '''
```

</details>
</br>


## **Pág. 59 à 62............Fatiamento | Por que as fatias e os intervalos excluem o último item | Objetos slice | Fatiamento multidimensional e reticências**
<details>
<summary></📖></summary>

```python
l = [10, 20, 30, 40, 50, 60]
print('l[:2] = ', l[:2]) # até, mas não inclusive o (:)2° | output: [10, 20]
print('l[2:] = ', l[2:]) # a partir do 2(:)° | output: [30, 40, 50, 60]

s = 'Bicycle'
print('s[::3] = ', s[::3]) #output: Bye
print('s[::-1] = ', s[::-1]) #output: elcyciB
print('s[::-2] = ', s[::-2]) #output: eccB

invoice = """
0.....6.................................40........52...55........
1909 Pimoroni PiBrella                      $17.50    3    $52.50
1489 6mm TactileSwitch x20                   $4.95    2     $9.90
1510 Panavise Jr. - PV-201                  $28.00    1    $28.00
1601 PiTFT Mini Kit 320x240                 $34.95    1    $34.95
"""
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:] # invoice é cortado nas quebras de linhas depois da 2segunda (a primeira quebra foi após """)
print("__________________________________\n")
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])
```

</details>
</br>


## **Pág. 55............Atribuição de valores a fatias**
<details>
<summary></📖></summary>

```python
m = list(range(10))
print("m =", m, '\n')
#output: m = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

m[2:5] = [20, 30] # no 2°(:) coloca o 20 e o 30 vai em seguida(no 3°); e elimina tudo após até o 5°, mas não inclusive.
print("m[2:5] = [20, 30]\nm =", m, '\n') 
#output: m = [0, 1, 20, 30, 5, 6, 7, 8, 9]

del m[5:7] # deleta tudo a partir do 5°, até o 7°, mas não inclusive.
print("del m[5:7]\nm =", m, '\n') 
#output: m = [0, 1, 20, 30, 5, 8, 9]

m[3::2] = [11, 22] # no 3°(:) coloca 11, e, em seguida, antes do (:)2° —que ao reiniciar em zero é o 9— coloca o 22.
print("m[3::2] = [11, 22]\nm =", m, '\n')
#output: m = [0, 1, 20, 11, 5, 22, 9]

m[2:5] = [100]
print("m[2:5] = [100]\nm =", m, '\n') # no 2°(:) coloca o 100; e elimina tudo após até o 5°, mas não inclusive.
#output: m = [0, 1, 100, 22, 9]
```

</details>
</br>


## **Pág. 63 e 64............Usando + e * com sequências | Criando listas de listas**
<details>
<summary></📖></summary>

```python
n = [1, 2, 3]
print("n * 5: ", (n * 5))
#output: [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

print("5 * 'abcd': ", (5 * 'abcd'))
#output: abcdabcdabcdabcdabcd

#______Listas de listas →→→ COM LISTCOMPREHENSION E EQUIVALENTE:_________________________________
with_listcomp = [['_'] * 3 for i in range(3)] # LISTCOMPREHENSION

print("COM o uso de listcomprehension (obtém resultado desejado):", '\n', with_listcomp, '\n')
#output: [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

with_listcomp[1][2] = 'with_listcomp' # linha por coluna, com índice iniciando em zero.
print("COM o uso de listcomprehension (obtém resultado desejado):", '\n', with_listcomp, '\n')
#output: [['_', '_', '_'], ['_', '_', 'with_listcomp'], ['_', '_', '_']]

# CÓDIGO EQUIVALENTE:
equivalent_with_listcomp = []
for i in range(3):
    row_1 = ['_'] * 3
    equivalent_with_listcomp.append(row_1)

print("código equivalente a COM o uso de listcomprehension (obtém resultado desejado):", '\n', equivalent_with_listcomp, '\n')
#output: [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

equivalent_with_listcomp[1][2] = 'equivalent_with_listcomp' # linha por coluna, com índice iniciando em zero.
print("código equivalente a COM o uso de listcomprehension (obtém resultado desejado):", '\n', equivalent_with_listcomp, '\n')
#output: [['_', '_', '_'], ['_', '_', 'equivalent_with_listcomp'], ['_', '_', '_']]

#______Listas de listas →→→ SEM LISTCOMPREHENSION E EQUIVALENTE:_________________________________
without_listcomp = [['_'] * 3] * 3

print("SEM o uso de listcomprehension (ocorre evento indesejado):", '\n', without_listcomp, '\n')
#output: [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

without_listcomp[1][2] = 'without_listcomp' # linha por coluna, com índice iniciando em zero.
print("SEM o uso de listcomprehension (ocorre evento indesejado):", '\n', without_listcomp, '\n') #evento indesejado → (gera repetições)
#output: [['_', '_', 'without_listcomp'], ['_', '_', 'without_listcomp'], ['_', '_', 'without_listcomp']]

# CÓDIGO EQUIVALENTE:
row_2 = ['_'] * 3
equivalent_without_listcomp = []
for i in range(3):
    equivalent_without_listcomp.append(row_2)

print("código equivalente a SEM o uso de listcomprehension (ocorre evento indesejado):", '\n', equivalent_without_listcomp, '\n')
#output: [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

equivalent_without_listcomp[1][2] = 'equivalent_with_listcomp' # linha por coluna, com índice iniciando em zero.
print("código equivalente a SEM o uso de listcomprehension (ocorre evento indesejado):", '\n', equivalent_without_listcomp, '\n') #evento indesejado → (gera repetições)
#output: [['_', '_', 'equivalent_with_listcomp'], ['_', '_', 'equivalent_with_listcomp'], ['_', '_', 'equivalent_with_listcomp']] 
```

</details>
</br>


## **Pág. 65............Atribuições combinadas e sequências**
<details>
<summary></📖></summary>

```python
#___SEQUÊNCIAS EMBUTIDAS MUTÁVEIS continuam sendo o mesmo objeto ao acrescentar itens_____________________
mutavel_list = [1, 2, 3]
print("sequência mutável list: ", mutavel_list)
print("id da sequência mutável list: ", id(mutavel_list))
#output: 2639841919104

mutavel_list *= 2 #possuirá o mesmo id pois continua sendo o mesmo objeto ao acrescentar itens
print("sequência mutável list: ", mutavel_list)
print("id da sequência mutável list: ", id(mutavel_list), '\n')
#output: 2639841919104

#___SEQUÊNCIAS EMBUTIDAS IMUTÁVEIS geram outros objetos ao acrescentar itens_____________________________
imutavel_tuple = (1, 2, 30)
print("sequência imutável tuple: ", imutavel_tuple)
print("id da sequência imutável tuple: ", id(imutavel_tuple))
#output: 2639828257536

imutavel_tuple *= 2 #possuirá outro id pois se torna outro objeto ao acrescentar itens
print("sequência imutável tuple: ", imutavel_tuple)
print("id da sequência imutável tuple: ", id(imutavel_tuple))
#output: 2639841656736

# OBS: !!!
# A SEQUÊNCIA EMBUTIDA IMUTÁVEL SIMPLES str (string) é uma exceção; pois as instâncias de str são alocadas em 
# memória com espaço extra, de modo que a concatenação não exigirá uma cópia da string completa todas as vezes.
```

</details>
</br>


## **Pág. 67............O enigma da atribuição +=**
<details>
<summary></📖></summary>

```python
t = (1, 2, [30, 40])
'''
t[2] += [50, 60]
output: TypeError: 'tuple' object does not support item assignment

print(t)
output: (1, 2, [30, 40, 50, 60])
'''

#inspecionar bytecode Python para ver o que ocorre internamente:
import dis
dis.dis('t[2] += [50, 60]')
''' 
output:
.1............0 LOAD_NAME................0 (t)
..............2 LOAD_CONST...............0 (2)
..............4 DUP_TOP_TWO..............
..............6 BINARY_SUBSCR............ →→→ coloca o valor de t[2] no TOS (Top Of Stack, ou Topo de Pilha)
..............8 LOAD_CONST...............1 (50)
.............10 LOAD_CONST...............2 (60)
.............12 BUILD_LIST...............2
.............14 INPLACE_ADD.............. →→→ Executa TOS += [50, 60]. Isso funciona quando TOS refere-se a um objeto mutável (uma lista no exemplo)
.............16 ROT_THREE................
.............18 STORE_SUBSCR............. →→→ Faz a atribuição t[2] = TOS. Isso falha se s é imutável (a tupla t)
.............20 LOAD_CONST...............3 (None)
.............22 RETURN_VALUE.............
'''

# →→→→→→→→→ CONCLUSÃO: colocar itens mutáveis(list, no exemplo) em imutáveis(tupla, no exemplo) não é uma boa ideia. ←←←←←←←←←
```

</details>
</br>


## **Pág. 69............list.sort e a função embutida sorted**
<details>
<summary></📖></summary>

```python
'''
• list.sort: ordena uma lista in-place (não cria nova lista, altera a lista original)
• sorted: não ordena uma lista in-place (cria nova lista, não altera a lista original)
→ Sintaxe:
    <facultativo>
    sorted(list, <reverse=True>, <key=str.lower/key=len/key=str/key=int>)
'''
fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits) #sorted: cria uma nova lista de strings em órdem alfabética
#output: ['apple', 'banana', 'grape', 'raspberry']
print(fruits) #a lista original não foi alterada
#output: ['grape', 'raspberry', 'apple', 'banana']

sorted(fruits, reverse=True) #sorted: cria uma nova lista de strings com reverse que deixa em órdem alfabética reversa
#output: ['raspberry', 'grape', 'banana', 'apple']
print(fruits) #a lista original não foi alterada
#output: ['grape', 'raspberry', 'apple', 'banana']

sorted(fruits, key=len) #sorted: cria uma nova lista de strings com key que ordenada de acordo com o tamanho de cada string
#output: ['grape', 'apple', 'banana', 'raspberry']
print(fruits) #a lista original não foi alterada
#output: ['grape', 'raspberry', 'apple', 'banana']

sorted(fruits, key=len, reverse=True) #sorted: cria uma nova lista de strings com key que ordenada de acordo com o tamanho de cada string e com reverse que deixa em órdem reversa
#output: ['raspberry', 'banana', 'grape', 'apple']
print(fruits) #a lista original não foi alterada
#output: ['grape', 'raspberry', 'apple', 'banana']

print(fruits.sort()) #list.sort: ordena a lista in-place (não cria nova lista, altera a lista original)
#output: None → retorna None para nos lembrar de que o objeto-alvo é aterado e que não foi criado uma nova cópia
print(fruits) #a lista original foi alterada
#output: ['apple', 'banana', 'grape', 'raspberry']


nomes = ['Aluno', 'alfa', 'Abcd', 'abcd']
sorted(nomes) #sorted: cria uma nova lista de strings em órdem alfabética
#output:['Abcd', 'Aluno', 'abcd', 'alfa']
print(nomes) #a lista original não foi alterada
#output:['Aluno', 'alfa', 'Abcd', 'abcd']

nomes.sort(key=str.lower) #sorted: #list.sort: ordena a lista in-place (não cria nova lista, altera a lista original) com key=str.lower que ordena sem levar em consideração letras maiúsculas e minúsculas
#output: None → retorna None para nos lembrar de que o objeto-alvo é aterado e que não foi criado uma nova lista, mas alterado a lista original
print(nomes) #a lista original foi alterada
#output:['Abcd', 'abcd', 'alfa', 'Aluno']

sorted(nomes, key=len) #sorted: cria uma nova lista de strings com key=len que ordenada de acordo com o tamanho de cada string
#output:['Abcd', 'abcd', 'alfa', 'Aluno'] → ♦compare... ↓↓↓
print(nomes) #a lista original não foi alterada
#output:['Abcd', 'abcd', 'alfa', 'Aluno']

sorted(nomes, key=len, reverse=True) #sorted: cria uma nova lista de strings com key=len que ordenada de acordo com o tamanho de cada string e com reverse=True que deixa em órdem reversa
#output:['Aluno', 'Abcd', 'abcd', 'alfa'] → ♦compare... ↑↑↑
print(nomes) #a lista original não foi alterada
#output:['Abcd', 'abcd', 'alfa', 'Aluno']


str_int = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
#sorted(str_int) → output: "TypeError: '<' not supported between instances of 'str' and 'int'" (solução: key=int/strt↓)

sorted(str_int, key=int) #sorted: cria uma nova lista com key=int que ordenada tratando todos os itens como tipo inteiro
#output:[0, '1', 5, 6, '9', 14, 19, '23', 28, '28']
print(str_int) #a lista original não foi alterada
#output:[28, 14, '28', 5, '9', '1', 0, 6, '23', 19]

sorted(str_int, key=str) #sorted: cria uma nova lista com key=str que ordenada tratando todos os itens como tipo string
#output:[0, '1', 14, 19, '23', 28, '28', 5, 6, '9']
print(str_int) #a lista original não foi alterada
#output:[28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
```

</details>
</br>


## **Pág. 71 à Pág. 74............Administrando sequências ordenadas com bisect | Pesquisando com bisect | Inserção com bisect.insor**
<details>
<summary></📖></summary>

```python
'''
Módulo bisect oferece duas funções — bisect e insort— que usam algoritmo 
de busca binária para pesquisar e inserir itens em [sequências ordenadas].
♦ sintaxe:
    este_indice = bisect.bisect(sequencia_ordenada, valor) → valor é inserido no índice correto da sequencia_ordenada. É retornado o valor desse índice o qual foi atribuido à este_indice
    bisect.insort(seq, item) → permite a inserção de item de forma ordenada na sequência seq 
♦ comportamento:
    • bisect.bisect() é um alias para bisect.bisect_rigth(), que insere à direita do índice procurado; → bisect.bisect_left() insere à esquerda do índice.
    • limitar a pesquisa a uma sequência, o default do argumento lo é 0 e de hi é o len(): [5, 3 ,7 ,8 ,9] → (lo=3, hi=9) → [3, 7, 8, 9], len()=3
'''
import bisect
import sys
import random
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

print('\nTodas as notas obtidas:', [grade(score) for score in [33, 99, 77, 70 ,89, 90, 100]], '\np/ as respectivas pontuações: [33, 99, 77, 70 ,89, 90, 100]')

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

Todas as notas obtidas: ['F', 'A', 'C', 'C', 'B', 'A', 'A']
p/ as respectivas pontuações: [33, 99, 77, 70 ,89, 90, 100]
'''

# Exemplo de uso do módulo bisect em inserção de itens em sequência ordenada com bisect.insort(seq, item):____________________________________
SIZE = 7

random.seed(1729)

my_list = []
print("\nInserindo itens ordenadamente com bisect.insort(): ")
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

'''output:
Inserindo itens ordenadamente com bisect.insort():
10 -> [10]
 0 -> [0, 10]
 6 -> [0, 6, 10]
 8 -> [0, 6, 8, 10]
 7 -> [0, 6, 7, 8, 10]
 2 -> [0, 2, 6, 7, 8, 10]
10 -> [0, 2, 6, 7, 8, 10, 10]
'''
```

</details>
</br>


## **Pág. 75............Quando uma lista não é a resposta | Arrays**
<details>
<summary><📖/></summary>

Arrays em Python, especificamente referindo-se a arrays da biblioteca NumPy, podem ser superiores às listas nativas em várias situações, especialmente quando se trata de computação numérica, eficiência e manipulação avançada de dados.

</details>
</br>

## **Pág. 78 à Pág. 80............Memory Views | NumPy e SciPy**
<details>
<summary><📖/></summary>

### ***Memory Views X NumPy e SciPy***
Enquanto as memory views são úteis para acessar dados de arrays sem copiá-los, NumPy e SciPy vão além, oferecendo uma ampla gama de funcionalidades matemáticas, científicas e de engenharia. Essas bibliotecas permitem manipulações mais sofisticadas, operações vetoriais, otimização e análise de dados complexos que vão além do escopo das memory views.

#### **Memory Views:**
As memory views são uma maneira eficiente de acessar dados de arrays em um formato específico sem copiar os dados. Elas são úteis para trabalhar com grandes volumes de dados, mas têm limitações em termos de funcionalidades e operações.

```python
import numpy as np

# Criar um array numpy
arr = np.array([1, 2, 3, 4, 5])

# Criar um memory view
mem_view = memoryview(arr)

# Acessar os elementos através do memory view
for element in mem_view:
    print(element)
```

#### **NumPy:**
NumPy é uma biblioteca que expande significativamente as funcionalidades de manipulação de arrays, oferecendo uma ampla gama de funções matemáticas, operações de álgebra linear, broadcasting e muito mais.

```python
import numpy as np

# Criar um array numpy
arr = np.array([1, 2, 3, 4, 5])

# Multiplicar todos os elementos por 2 usando NumPy
arr_times_2 = arr * 2
print(arr_times_2)
```

#### **SciPy:**
SciPy é uma biblioteca construída sobre o NumPy que oferece funcionalidades específicas para ciência e engenharia. Ela inclui módulos para otimização, processamento de sinais, estatísticas, interpolação e muito mais.

```python
import numpy as np
from scipy import interpolate

# Criar pontos x e y para interpolação
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])

# Criar uma função interpoladora usando SciPy
f = interpolate.interp1d(x, y, kind='linear')

# Calcular valor interpolado em x = 2.5
interpolated_value = f(2.5)
print(interpolated_value)

```

</details>
</br>


## **Pág. 82............Deques e outras filas | resumo[Métodos de tuple, list, array e deque]**
<details>
<summary><📖/></summary>

### ***SEQUÊNCIAS EMBUTIDAS:***
|  | MUTÁVEIS (mesmo id quando ocorre mudança) | IMUTÁVEIS (novo id quando ocorre "mudança" (na verdade subsituição)) |
|:-:|:-:|:-:|
| SIMPLES (armazenam itens de um só tipo) | bytearray, array, memoryview | str, bytes |
| CONTAINER (armazenam itens de tipos diferentes) | list, deque | tuple |

#### **SIMPLES:**
  - Mais compactas, rápidas e fáceis de usar.
  - Limitadas ao armazenamento de dados atômicos como números, caracteres e bytes.

#### **CONTAINER:**
  - Mais flexíveis.
  - Não recomendadas para armazenar objetos mutáveis.

→ Como um exemplo, o tipo mais básico de sequência é list, um container mutável.</br></br>

Objeto hashable é um ojeto capaz de possuir um hash (um id como sha1 ou MD5):</br>
 ✓ Terá um valor de hash que não muda (possuirá um método __hash__())</br>
 ✓ Será comparável com outros objetos (possuirá um método __eq__())</br></br>

Condição para um objeto ser hashable:</br>
 → Deve ser IMUTÁVEL — str, bytes e tuple (exceto se conter referências a objetos que não são hashable)—.</br></br>

Nota:</br>
 → frozenset é uma função que transforma objetos MUTÁVEIS em IMUTÁVEIS.</br></br>

### ***MÉTODOS DE TUPLE, LIST, ARRAY E DEQUE:***
● tuple aceita os métodos de list, com exceção do método __reversed__() e de todos os métodos que acrescentam ou removem itens, pois tuple é IMUTÁVEL.</br>
● array é mais eficiente que list (exceto pela limitância de ser do tipo de sequência SIMPLES) para sequências contendo apenas tipo de valores numéricos.</br>
● deque permite as regras de acesso FIFO e LIFO e é a sequência mais otimizada para inserção e remoção de itens das extremidades (centrais a latência é maior).</br>
|  | tuple | list | array | deque |  |
|:-:|:-:|:-:|:-:|:-:|:-:|
| s.__add__(s2) | ♦ | ♦ | ♦ |  | s + s2 → concatenação |
| s.__iadd__(s2) |  | ♦ | ♦ | ♦ | s += s2 → concatenação in-place |
| s.append(e) |  | ♦ | ♦ | ♦ | Concatena um elemento após o último |
| s.appendleft(e) |  |  |  | ♦ | Concatena um elemento à esquerda (antes do primeiro) |
| s.byteswap() |  |  | ♦ |  | Troca os bytes de todos os itens do array para uma conversão de endianess |
| s.clear() |  | ♦ |  | ♦ | Apaga todos os itens |
| s.__contains__(e) | ♦ | ♦ | ♦ |  | e in s |
| s.copy() |  | ♦ |  |  | Shallow copy (cópia rasa) da lista |
| s.__copy__() |  |  | ♦ | ♦ | Suporte para copycopy(shallow copy ou copora rasa) |
| s.count(e) | ♦ | ♦ | ♦ | ♦ | Conta as ocorrências de um elemento |
| s.__deepcopy__() |  |  | ♦ |  | Suporte otimizado para copydeepcopy |
| s.__delitem__(p) |  | ♦ | ♦ | ♦ | Remove o item da posição p |
| s.extend(it) |  | ♦ | ♦ | ♦ | Concatena itens do iterável it |
| s.extendleft(i) |  |  |  | ♦ | Adiciona itens do iterável i à esquerda |
| s.fromfile(f, n) |  |  | ♦ |  | Concatena n itens do arquivo binário f interpretado como valores de máquina compactos |
| s.fromlist(l) |  |  | ♦ |  | Concatena itens da lista; se algum deles provocar um TypeError, nenhum valor será concatenado |
| s.frombytes(b) |  |  | ♦ |  | Concatena itens da sequência de bytes intepretada como valores de máquina compactos |
| s.__getitem__(p) | ♦ | ♦ | ♦ | ♦ | s[p] → obtém o item de uma posição |
| s.__getnewargs__() | ♦ |  |  |  | Suporte para serialização otimizada com pickle |
| s.index(e) | ♦ | ♦ | ♦ |  | Encontra a posição da primeira ocorrência de e |
| s.insert(p, e) |  | ♦ | ♦ |  | Insere o elemento e antes do item na posição p |
| s.itemsize() |  |  | ♦ |  | Tamanho em bytes de cada item do array |
| s.__iter__() | ♦ | ♦ | ♦ | ♦ | Obtém um iterador |
| s.__len__() | ♦ | ♦ | ♦ | ♦ | len(s) → número de itens |
| s.__mul__(n) | ♦ | ♦ | ♦ |  | s * n → concatenação repetida |
| s.__imul__(n) |  | ♦ | ♦ |  | s *= n → concatenação repetida in-place |
| s.__rmul__(n) | ♦ | ♦ | ♦ |  | n * s → concatenação repetida invertida (operador reverso) |
| s.pop([p]) |  | ♦ | ♦ | ♦ | Remove e retorna o último item (por defalt) ou, opcionalmente, o item na posição p |
| s.popleft() |  |  |  | ♦ | Remove e devolve o primeiro item |
| s.remove(e) |  | ♦ | ♦ | ♦ | Remove a primeira ocorrência do elemento com o valor de e |
| s.reverse() |  | ♦ | ♦ | ♦ | Inverte a ordem dos itens in-place |
| s.__reversed__() |  | ♦ |  | ♦ | Obtém um iterador para percorrer os itens do último para o primeiro |
| s.rotate(n) |  | ♦ |  | ♦ | Move n itens de uma extremidade para a outra |
| s.__setitem__(p, e) |  | ♦ | ♦ | ♦ | s[p] = e → coloca e na posição p sobrescrevendo o item existente |
| s.sort([key], [reverse]) |  | ♦ |  |  | Ordena itens in-place com os argumentos nomeados opcionais key e reverse |
| s.tobytes() |  |  | ♦ |  | Devolve os itens como valores de máquina compactos em um objeto bytes |
| s.tofile(f) |  |  | ♦ |  | Salva os itens como valores de máquina compactos em um arquivo binário f |
| s.tolist() |  |  | ♦ |  | Devolve os itens como objetos numéricos em uma lista |
| s.typecode |  |  | ♦ |  | String de um caractere que identifica o tipo dos itens na linguagem C |

</details>
</br>
