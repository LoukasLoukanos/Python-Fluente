'''
    AS TUPLAS TÊM DUPLA FUNÇÃO:
    •podem ser usadas como listas imutáveis
    •podem ser usadas como registros sem nomes de campos
'''
#_____________________________________Tuplas como registros - Pág. 52_____________________________________

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

#atribuição paralela:
latitude, longitude = lax_coordinates

#troca (swap) de valores de duas variáveis sem usar uma variável temporária:
latitude, longitude = longitude, latitude
#revertendo:
latitude, longitude = latitude, longitude

#prefixar um argumento com um asterisco * ao chamar uma função:
divmod(20, 8)
t = (20, 8)
divmod(*t)#o prefixo asterisco * serve para informar que a variável contém todos os parâmetros exigidos por divmod, sem precisar separá-los por vírgulas.

#atribuição paralela com o prefixo asterisco *
a, *body, c, d = range(5) # → (a=0, [body = 1, 2], c=3, d=4)
print(a, *body, c, d) # output: 0, 1, 2, 3, 4


#_________________________Desempacotamento de tuplas aninhadas ou desempacotamento de iteráveis aninhadas - pág 55____________________________________________________________________

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # a tupla aninhada é um par de coordenadas
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  # desempacotando as coordenadas atribuindo-as à tupla (latitude, longitude)
    if longitude <= 0: # condições de acesso....
        print(fmt.format(name, latitude, longitude))

#________________________Tuplas nomeadas - pág 56_________________________________

#________________________Fatiamento - pág 59 à 62_____________________________________________________________________________________________________________________________________
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