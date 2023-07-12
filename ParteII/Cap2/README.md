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
</br>


## **Desempacotamento de tuplas............Pág. 53**
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
</br>


## **Desempacotamento de tuplas aninhadas............Pág. 55**
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
</br>


## **Tuplas nomeadas............Pág. 56**
```python

```
</br>


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
