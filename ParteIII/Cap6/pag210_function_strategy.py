# Padrão de Projeto Baseado em Função (Strategy pattern function-based implementation):

from pag208_contexto import *

#_________↓Padrão de Projeto Baseado em Função↓__________________
def fidelity_promo(order):  # cada estratégia é uma função
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0
#_________↑Padrão de Projeto Baseado em Função↑__________________


# dois clientes: joe não tem nenhum ponto no programa de fidelidade, ann tem 1100 pontos.
joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)

# um carrinho de compras 'banana_cart' com 30 unidades de banana e 10 maçãs 
banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
# aplicando desconto em um Order, passando a função de promoção bulk_item_promo como argumento
Order(joe, banana_cart, bulk_item_promo) # graças a bulk_item_promo, joe obtém um desconto de 1,5 dólar nas bananas
#output: <Order total: 30.00 due: 28.50>

# um carrinho de compras com três itens
cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]
# aplicando desconto em um Order, passando a função de promoção fidelity_promo como argumento
Order(joe, cart, fidelity_promo) # A promoção FidelityPromo não dá nenhum desconto a joe
#output: <Order total: 42.00 due: 42.00>
Order(ann, cart, fidelity_promo)  # A promoção fidelity_promo dá desconto de 5% na promoção a ann porque ela tem pelo menos 1000 pontos
#output: <Order total: 42.00 due: 39.90>

# o carrinho de compras 'long_order' tem 10 itens diferentes a um dólar cada
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
# aplicando desconto em um Order, passando a função de promoção large_order_promo como argumento
Order(joe, long_order, large_order_promo) # joe obtém um desconto de 7% no total do produto por causa de LargeOrderPromo
#output: <Order total: 10.00 due: 9.30>


#Ver [Uso de decorador (substitui o código acima de forma eficiente)] na pág 226 à 228 → pag226a228__strategy_best4.py ou README.md 7