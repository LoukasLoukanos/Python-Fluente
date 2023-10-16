import inspect

from pag210_function_strategy import *
import pag210_function_strategy

# abordagem I___________________________
promos1 = [fidelity_promo, bulk_item_promo, large_order_promo] # "promos1" é definida como uma lista que contém três funções

def best_promo1(order): # define uma função chamada "best_promo1" que recebe um pedido como argumento
    '''
    usa a função "max" para encontrar o maior desconto que pode ser aplicado 
    ao pedido. Ele usa um loop "for" para percorrer todas as funções em 
    "promos1" e aplicá-las ao pedido. O desconto resultante é retornado.
    '''
    return max(promo(order) for promo in promos1)



# abordagem II___________________________
'''
a variável "promos2" é definida como uma lista de funções. Ele usa a função 
"globals" para obter todas as variáveis globais do programa e, em seguida, 
filtra as que terminam com "_promo" e não são "best_promo". Cada variável 
global que corresponde a esse critério é adicionada à lista "promos2".
'''
promos2 = [globals()[name] for name in globals()
            if name.endswith('_promo')
            and name != 'best_promo'] 

def best_promo2(order): # recebe um pedido como argumento.
    '''
    usa a função "max" para encontrar o maior desconto que pode ser aplicado 
    ao pedido. Ele usa um loop "for" para percorrer todas as funções em 
    "promos2" e aplicá-las ao pedido. O desconto resultante é retornado.
    '''
    return max(promo(order) for promo in promos2)



# abordagem III___________________________
'''
a variável "promos3" é definida como uma lista de funções. Ele usa a função 
"inspect.getmembers" para obter todos os membros da classe ou módulo "promotions" 
que são funções. Cada função encontrada é adicionada à lista "promos3".
'''
promos3 = [func for name, func in inspect.getmembers(pag210_function_strategy, inspect.isfunction)]

def best_promo3(order): # recebe um pedido como argumento.
    '''
    usa a função "max" para encontrar o maior desconto que pode ser aplicado ao 
    pedido. Ele usa um loop "for" para percorrer todas as funções em "promos3" e 
    aplicá-las ao pedido. O desconto resultante é retornado.
    '''
    return max(promo(order) for promo in promos3)