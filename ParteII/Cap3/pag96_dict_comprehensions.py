'''
• Mapeamento ou Dicionário (dict) ou hash[key]=value é uma coleção de objetos armazenados 
  por uma chave e valor, ao contrário de sequências que armazenam pela posição dos itens.
'''

# Uma sequência de itens ou lista de pares
DIAL_CODES = [(86, 'China'), (91, 'India'), (1, 'United States'), (62, 'Indonesia'), (55, 'Brazil'), (92, 'Pakistan'), (880, 'Bangladesh'), (234, 'Nigeria'), (7, 'Russia'), (81, 'Japan'),]   

# Criando um Mapeamento (dicionário ou hash[key]=value) com o método dict()__________________________________________________________________
metodo_dict = dict(DIAL_CODES) #método dict()
print('Chaves e valores:', metodo_dict) #output: Chaves e valores: {86: 'China', 91: 'India', 1: 'United States', 62: 'Indonesia', 55: 'Brazil', 92: 'Pakistan', 880: 'Bangladesh', 234: 'Nigeria', 7: 'Russia', 81: 'Japan'}
print('Chaves:', metodo_dict.keys()) #output: Chaves: dict_keys([86, 91, 1, 62, 55, 92, 880, 234, 7, 81])
print('Valores:', metodo_dict.values()) #output: Valores: dict_values(['China', 'India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Bangladesh', 'Nigeria', 'Russia', 'Japan'])

# Criando um Mapeamento (dicionário ou hash[key]=value) com dict comprehensions______________________________________________________________
dict_comprehensions = {key: value for key, value in DIAL_CODES} #dict comprehensionsa
print('Chaves e valores:', dict_comprehensions) #output: Chaves e valores: {86: 'China', 91: 'India', 1: 'United States', 62: 'Indonesia', 55: 'Brazil', 92: 'Pakistan', 880: 'Bangladesh', 234: 'Nigeria', 7: 'Russia', 81: 'Japan'}
print('Chaves:', dict_comprehensions.keys()) #output: Chaves: dict_keys([86, 91, 1, 62, 55, 92, 880, 234, 7, 81])
print('Valores:', dict_comprehensions.values()) #output: Valores: dict_values(['China', 'India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Bangladesh', 'Nigeria', 'Russia', 'Japan'])

dict_comprehensions_2 = {key: value.upper() for key, value in dict_comprehensions.items() if key<66} #dict comprehensions
print(dict_comprehensions_2) #output: {1: 'UNITED STATES', 62: 'INDONESIA', 55: 'BRAZIL', 7: 'RUSSIA'}