'''
    AS TUPLAS TÊM DUPLA FUNÇÃO:
    •podem ser usadas como listas imutáveis
    •podem ser usadas como registros sem nomes de campos
'''
#_____________________________________Tuplas como registros_____________________________________

# 1° EXEMPLO
lax_coordinates = (33.425, -118.408056) #latitude e longitude do Aeroporto Internacional de Londres.
print('    1° exemplo: ', type(lax_coordinates), lax_coordinates)

# 2° EXEMPLO
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014) #Dados sobre Tóquio: nome, ano poputação (milhões), mudança na população (%), área (km²)
print('    2° exemplo: ', type(city), city)
print('    2° exemplo: ', type(year), year)

# 3° EXEMPLO
traveler_ids = [('USA', '3115855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]#Uma lista de tuplas no formato (country_code, passport_number).
print('    3° exemplo: ', type(traveler_ids), traveler_ids)

# 4° EXEMPLO
for passport in sorted(traveler_ids):# À medida que fazemos uma iteração pela lista, o nome passport é associado à cada tupla.
    print('    4° exemplo: ', type(passport), '%s/%s' % passport)# O operador de formatação % entende as tuplas e trata cada item como um campo separado.

# 5° EXEMPLO
for country, _ in traveler_ids:# O laço for sabe como obter os itens de uma tupla separadamente -isso é chamado de "desempacotamento" (unpacking). Nesse caso, não estamos interessados no segundo item, portanto ele é atribuído a_, que é uma variável comumente usada para capturar valores que não queremos usar.
    print('    5° exemplo: ', type(country), country)
'''
OUTPUT:
    1° exemplo:  <class 'tuple'> (33.425, -118.408056)    2° exemplo:  <class 'str'> Tokyo    2° exemplo:  <class 'int'> 2003
    3° exemplo:  <class 'list'> [('USA', '3115855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
    4° exemplo:  <class 'tuple'> BRA/CE342567
    4° exemplo:  <class 'tuple'> ESP/XDA205856
    4° exemplo:  <class 'tuple'> USA/3115855
    5° exemplo:  <class 'str'> USA
    5° exemplo:  <class 'str'> BRA
    5° exemplo:  <class 'str'> ESP
'''
