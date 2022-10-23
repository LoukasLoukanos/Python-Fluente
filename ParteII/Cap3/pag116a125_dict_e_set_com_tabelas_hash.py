
'''
As chaves dos dict ou dicionários ou hash[key]=value precisam ser objetos hashable:
♦ Um objeto é hashable se:
 • 1 - Tiver um valor de hash que nunca mude: i.e., oferecer suporte a função hash por meio de um método __hash__ que sempre devolva o mesmo valor. 
 • 2 - Puder ser comparado com outros objetos: i.e., possuir suporte à igualdade por meio do método __eq__().
 → Se a == b é True, então hash(a) == hash(b) também deve ser True.
'''

# Códigos de discagem dos dez países mais populosos
DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]

d1 = dict(DIAL_CODES)  # d1 é criado a partir de tuplas, em ordem decrescente por padrão.

d2 = dict(sorted(DIAL_CODES))  # d2 é criado com tuplas ordenadas de acordo com o código de discagem do país.

d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))  # d3 é cria com tuplas ordenadas de acordo com o nome do país

print('d1:', d1.keys())
print('d2:', d2.keys())
print('d3:', d3.keys())
'''output:
d1: dict_keys([86, 91, 1, 62, 55, 92, 880, 234, 7, 81])
d2: dict_keys([1, 7, 55, 62, 81, 86, 91, 92, 234, 880])
d3: dict_keys([880, 55, 86, 91, 62, 81, 234, 92, 7, 1])
'''
assert d1 == d2 and d2 == d3  # d4 os dicionários são comparados como iguais, pois armazenam as mesmas células/baldes(bucket)/pares key:value.