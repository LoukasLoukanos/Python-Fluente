from collections import namedtuple

# Define uma namedtuple chamada 'Customer' com campos 'name' e 'fidelity'
#_________↓pag208_contexto.py ou README.md do Cap 6↓_____________________
# Código para o contexto apresentado

# Define uma namedtuple chamada 'Customer' com campos 'name' e 'fidelity'
Customer = namedtuple('Customer', 'name fidelity')

# Define a classe LineItem para representar itens individuais no carrinho
class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

# Define a classe Order, que representa um pedido
class Order:  # the Context
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        # Calcula o total do pedido somando os totais dos itens no carrinho
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        # Calcula o valor devido aplicando desconto, se houver promoção
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        # Representação de string para a classe Order
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

#_________↑pag208_contexto.py ou README.md do Cap 6↑_____________________



#_________↓pag210_function_strategy.py ou README.md do Cap 6↓____________________________
'''
 Trexo de código (está no cap 6) da abordagem do [Padrão de Projeto Baseado em Função].
Compare-o com o código seguinte da versão com decorador que o substitui com muita eficiência:
Obs: o uso de decoradores não substitui o Padrão de Projeto Baseado em Função 
(Strategy pattern function-based implementation), mas sim a eficiência.
'''

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

# (Padrão de Projeto Baseado em Função)
#_________↑pag210_function_strategy.py ou README.md do Cap 6↑____________________________


#_________↓Uso de decorador (substitui o código acima de forma eficiente)↓________________
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


# Instâncias de Customer representando clientes
joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)

# Itens no carrinho representados por instâncias de LineItem
cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermelon', 5, 5.0)]

# Exemplos de pedidos com diferentes estratégias de promoção
Order(joe, cart, fidelity)
#output: Order total: 42.00 due: 42.00

Order(ann, cart, fidelity)
#output: Order total: 42.00 due: 39.90

banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]

Order(joe, banana_cart, bulk_item)
#output: Order total: 30.00 due: 28.50

long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]

Order(joe, long_order, large_order)
#output: Order total: 10.00 due: 9.30

Order(joe, cart, large_order)
#output: Order total: 42.00 due: 42.00


# Exemplos de pedidos usando a melhor estratégia de promoção
Order(joe, long_order, best_promo)
#output: Order total: 10.00 due: 9.30

Order(joe, banana_cart, best_promo)
#output: Order total: 30.00 due: 28.50

Order(ann, cart, best_promo)
#output: Order total: 42.00 due: 39.90



'''output deco:
→ no tempo de importação (import time):
função decorada: <function fidelity at 0x000002382C1F8280>

→ no tempo de importação (import time):
função decorada: <function bulk_item at 0x000002382C1F8310>

→ no tempo de importação (import time):
função decorada: <function large_order at 0x000002382C1F83A0>
'''
