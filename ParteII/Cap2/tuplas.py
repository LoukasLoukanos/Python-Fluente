'''
    A SEQUÊNCIA EMBUTIDA IMUTÁVEL TUPLA TEM DUPLA FUNÇÃO:
    •pode ser usada como lista imutável
    •pode ser usada como registros sem nomes de campos
'''
#_____________________________________Tuplas como registros - Pág. 52__________________________________________________________________________________________________________________
print("_______________________________Tuplas como registros - Pág. 52_______________________________")
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



#_________________________Desempacotamento de tuplas ou desempacotamento de iteráveis e capturando itens excedentes com asterisco * - pág 53, 54 e 55_________________________________
print("___________________Desempacotamento de tuplas ou desempacotamento de iteráveis e capturando itens excedentes com asterisco * - pág 53, 54 e 55___________________")
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


#_________________________Desempacotamento de tuplas aninhadas ou desempacotamento de iteráveis aninhadas - pág 55____________________________________________________________________
print("___________________Desempacotamento de tuplas aninhadas ou desempacotamento de iteráveis aninhadas - pág 55___________________")
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

#________________________Tuplas nomeadas - pág 56 à 58_________________________________________________________________________________________________________________________________
print('__________________Tuplas nomeadas - pág 56 à 58__________________')
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

#________________________Fatiamento - pág 59 à 62_____________________________________________________________________________________________________________________________________
print("__________________Fatiamento - pág 59 à 62__________________")
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
print("——————————————————————————————————")

#________________________Atribuição de valores à fatias - pág 62______________________________________________________________________________________________________________________
print("__________________Atribuição de valores à fatias - pág 62__________________")
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

#________________________Usando + e * com sequências - pág 62 à 65____________________________________________________________________________________________________________________
print("__________________Usando + e * com sequências - pág 62 à 65__________________")
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
