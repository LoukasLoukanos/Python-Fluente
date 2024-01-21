# Possibilidades dos benefícios disponibilizados apenas para o padrão de projeto baseado em função

import inspect
from pag208_contexto import *
from pag210_function_strategy import *
import pag210_function_strategy

# Possibilidade I___________________________
promos1 = [fidelity_promo, bulk_item_promo, large_order_promo] # "promos1" é definida como uma lista que contém três funções

def best_promo1(order): # define uma função chamada "best_promo1" que recebe um pedido como argumento
    '''
    usa a função "max" para encontrar o maior desconto que pode ser aplicado 
    ao pedido. Ele usa um loop "for" para percorrer todas as funções em 
    "promos1" e aplicá-las ao pedido. O desconto resultante é retornado.
    '''
    return max(promo(order) for promo in promos1)



# Possibilidade II___________________________
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



# Possibilidade III___________________________
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


#_________↓Uso de decorador (substitui os códigos acima de forma eficiente)↓________________
# Obs: o uso de decoradores não substitui o Padrão de Projeto Baseado em Função 
# (Strategy pattern function-based implementation), mas sim a eficiência.

promos = []  # A lista promos para armazenar as estratégias de promoção disponíveis

# Função de decorador para adicionar funções de promoção à lista promos
def promotion(promo_func):  # O decorador promotion devolve promo_func inalterada após adicioná-la à lista promos.
    print('→ no tempo de importação (import time):\nfunção decorada: %s\n' % promo_func)
    promos.append(promo_func)
    return promo_func

# Decoradores aplicados a funções de promoção específicas
@promotion  # Qualquer função decorada com @promotion será adicionada a promos.
def fidelity(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

# Função para selecionar a melhor promoção disponível
def best_promo(order):  # Nenhuma alteração é necessária em best_promos, pois ela baseia-se na lista promos.
    """Select best discount available"""
    return max(promo(order) for promo in promos)

#_________↑Uso de decorador (substitui o código acima de forma eficiente)↑________________