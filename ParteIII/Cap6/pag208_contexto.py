from collections import namedtuple

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
