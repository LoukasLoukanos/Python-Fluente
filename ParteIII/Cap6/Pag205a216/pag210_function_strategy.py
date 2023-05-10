# Padrão de Projeto: Strategy pattern function-based implementation

from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # the Context

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)  # Para calcular um desconto, basta chamar a função self.promotion()
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

# não há classe abstrata

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


joe = Customer('John Doe', 0) # mesma configuração de teste do exemplo pag208_classic_strategy.py
ann = Customer('Ann Smith', 1100)

cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]

Order(joe, cart, fidelity_promo)  # para aplicar uma estratégia de desconto em um Order, basta passar a função de promoção como argumento
#output: <Order total: 42.00 due: 42.00>
Order(ann, cart, fidelity_promo)
#output: <Order total: 42.00 due: 39.90>

banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]

Order(joe, banana_cart, bulk_item_promo)  # uma função diferente de promoção é usada nesse caso
#output: <Order total: 30.00 due: 28.50>

long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]

Order(joe, long_order, large_order_promo)
#output: <Order total: 10.00 due: 9.30>
Order(joe, cart, large_order_promo)
#output: <Order total: 42.00 due: 42.00>