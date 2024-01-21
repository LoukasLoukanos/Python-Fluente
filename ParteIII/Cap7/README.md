# Decoradores (decorators) de função e closures

## **Pág. 222 à 224............Básico sobre decoradores**
<details>
<summary></summary>

Um decorador é basicamente uma função (função decoradora) que recebe outra função como parâmetro (chamada de função decorada) que, por sua vez, poderá ser modificada por uma terceira função (uma subfunção da decoradora). Decoradores de função em python permitem "marcar" funções modificando o seu comportamento.

### ***Exemplo simples da sintaxe:***
```python
def decorador(funcao_decorada):
    def subfuncao():
        # Código para modificar a função decorada, se necessário
        # ...

        resultado = funcao_decorada()  # Chamada da função decorada

        # Código após a chamada da função decorada, se necessário
        # ...

        return resultado

    return subfuncao

@decorador
def funcao_decorada():
    # Código da função decorada
    # ...

```

</details>
</br>


## **Pág. 224 à 226............Quando Python executa os decoradores**
<details>
<summary></summary>

Em Python, decoradores de função são funções que envolvem outras funções para estender ou modificar seu comportamento. Eles são frequentemente usados para adicionar funcionalidades a funções existentes de uma maneira elegante e reutilizável. A execução de um decorador de função ocorre quando o módulo que contém a função decorada é importado.

***Vamos entender o processo passo a passo:***

 - **1° - Importação do Módulo:** Quando você importa um módulo em Python, todas as declarações de nível superior (código fora de funções) são executadas.
Se houver uma função decorada no módulo, a função decoradora será executada imediatamente quando o módulo for importado.

 - **2° - Execução do Decorador:** O decorador em si é uma função que aceita outra função como argumento. A função a ser decorada é passada como argumento para o decorador, e a execução do decorador modifica ou estende o comportamento da função.

 - **3° - Definição da Função Decorada:** A função original é redefinida para apontar para a versão decorada.

 - **4° - Chamada da Função Decorada:** Quando a função decorada é chamada explicitamente em algum lugar do código, ela executa o código modificado ou estendido fornecido pelo decorador.

#### ***Exemplo - 1 → (da execução de decoradores):***
 ```python
# Decorador de exemplo
def meu_decorador(funcao):
    def funcao_decorada(*args, **kwargs):
        print("Executando antes da função.")
        resultado = funcao(*args, **kwargs)
        print("Executando depois da função.")
        return resultado
    return funcao_decorada

# Função decorada
@meu_decorador
def minha_funcao():
    print("Executando a função.")

# Importando o módulo (executa o decorador)
# "Executando antes da função." é impresso neste momento
# Nenhuma função é chamada explicitamente ainda
import modulo

# Chamando a função decorada
# Agora, "Executando antes da função." é impresso, em seguida,
# "Executando a função." e, por fim, "Executando depois da função."
minha_funcao()

```

***Enfatizando:***
 - Os decoradores de função são executados assim que o módulo é importado —tempo de importação (import time)—, porém as funções decoradas executam somente quando são explicitamente chamadas —tempo de execução (runtime)—.
 - Um decorador de verdade normalmente é definido em um módulo e aplicado em funções em outros módulos.
 - A maioria dos decoradores define uma função interna e a devolve.

#### ***Exemplo - 2 → (da execução de decoradores):***

```python
registry = []  # registy armazenará referências a funções decoradas com @register.

def register(func):  # register recebe uma função como argumento.
    print('→ no tempo de importação (import time):\nfunção decorada:%s\n' % func)  # exibe a função que está sendo decorada, para demonstração.
    registry.append(func)  # inclui func e registry.
    return func  # devolve func: precisamos devolver uma funçõa; nesse caso, devolvemos a mesma função recebida como argumento.

@register # f1 é uma função decorada com @register.
def f1():
    print('running f1()')

print('→ no tempo de execução (runtime):\nfrequências à funções decoradas com @register: registry%s'%registry)
f1()

'''output:
→ no tempo de importação (import time):
função decorada:<function f1 at 0x00000179087A3BE0>

→ no tempo de execução (runtime):
frequências à funções decoradas com @register: registry[<function f1 at 0x00000179087A3BE0>]
running f1()
'''

```

#### ***Exemplo - 3 → (da execução de decoradores):***

```python
registry = []  # registy armazenará referências a funções decoradas com @register.

def register(func):  # register recebe uma função como argumento.
    print('→ no tempo de importação (import time):\nfunção decorada:%s\n' % func)  # exibe a função que está sendo decorada, para demonstração.
    registry.append(func)  # inclui func e registry.
    return func  # devolve func: precisamos devolver uma funçõa; nesse caso, devolvemos a mesma função recebida como argumento.

@register  # f1 é uma função decorada com @register.
def f1():
    print('running f1()')

@register # f2 é uma função decorada com @register.
def f2():
    print('running f2()')

def f3():  # f3 não é uma fução decorada.
    print('running f3()')

def main():  # main exibe registry e então chama f1(), f2() e f3().
    print('→ no tempo de execução (runtime):\nfrequências à funções decoradas com @register: registry%s'%registry)
    f1()
    f2()
    f3()

if __name__=='__main__':
    main()  # main() é chamado somente se registration.py executar como script.

'''output:
→ no tempo de importação (import time):
função decorada:<function f1 at 0x000001A9665B3BE0>

→ no tempo de importação (import time):
função decorada:<function f2 at 0x000001A9665B3C70>

→ no tempo de execução (runtime):
frequências à funções decoradas com @register: registry[<function f1 at 0x000001A9665B3BE0>, <function f2 at 0x000001A9665B3C70>]
running f1()
running f2()
running f3()
'''

```

</details>
</br>


## **Pág. 226 à 228............Padrão Strategy melhorado com decorador**
<details>
<summary></summary>

### TRECHO I *(Contextualização)*
**Código para todo o contexto apresentado:**</br>
*(em pag208_contexto.py ou README.md do Cap 6)*

```python
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

```

</br>

### TRECHO II *("Tese")*
**O código (cap 6) da abordagem do [Padrão de Projeto Baseado em Função] para ser comparado com o código muito mais eficiente com uso de decorador do TRECHO III, abaixo↓:**</br>
*(em pag210_function_strategy.py + pag216_abordages.py ou README.md do Cap 6)*

```python
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


# Possibilidades de usos para as funções definidas:
# Possibilidade 1___________________________
promos1 = [fidelity_promo, bulk_item_promo, large_order_promo] # "promos1" é definida como uma lista que contém três funções

def best_promo1(order): # define uma função chamada "best_promo1" que recebe um pedido como argumento
    '''usa a função "max" para encontrar o maior desconto que pode ser aplicado 
    ao pedido. Ele usa um loop "for" para percorrer todas as funções em 
    "promos1" e aplicá-las ao pedido. O desconto resultante é retornado.'''
    return max(promo(order) for promo in promos1)


# Possibilidade 2___________________________
'''a variável "promos2" é definida como uma lista de funções. Ele usa a função 
"globals" para obter todas as variáveis globais do programa e, em seguida, 
filtra as que terminam com "_promo" e não são "best_promo". Cada variável 
global que corresponde a esse critério é adicionada à lista "promos2".'''
promos2 = [globals()[name] for name in globals()
            if name.endswith('_promo')
            and name != 'best_promo'] 

def best_promo2(order): # recebe um pedido como argumento.
    '''usa a função "max" para encontrar o maior desconto que pode ser aplicado 
    ao pedido. Ele usa um loop "for" para percorrer todas as funções em 
    "promos2" e aplicá-las ao pedido. O desconto resultante é retornado.'''
    return max(promo(order) for promo in promos2)


# Possibilidade 3___________________________
'''a variável "promos3" é definida como uma lista de funções. Ele usa a função 
"inspect.getmembers" para obter todos os membros da classe ou módulo "promotions" 
que são funções. Cada função encontrada é adicionada à lista "promos3".'''
promos3 = [func for name, func in inspect.getmembers(pag210_function_strategy, inspect.isfunction)]

def best_promo3(order): # recebe um pedido como argumento.
    '''usa a função "max" para encontrar o maior desconto que pode ser aplicado ao 
    pedido. Ele usa um loop "for" para percorrer todas as funções em "promos3" e 
    aplicá-las ao pedido. O desconto resultante é retornado.'''
    return max(promo(order) for promo in promos3)

```

</br>

### TRECHO III *("Antítese e Síntese")*
**Código com o uso de decorador (substitui o código do cap 6 da abordagem do [Padrão de Projeto Baseado em Função] acima↑ de forma eficiente):**</br>
Obs: Ainda estamos utilizando o Padrão de Projeto Baseado em Função, porém com uma abordagem mais eficiente através do uso de decorador.</br>
*(Pág. 226 à 228............Padrão Strategy melhorado com decorador)*

```python
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



'''output:
→ no tempo de importação (import time):
função decorada: <function fidelity at 0x000002382C1F8280>

→ no tempo de importação (import time):
função decorada: <function bulk_item at 0x000002382C1F8310>

→ no tempo de importação (import time):
função decorada: <function large_order at 0x000002382C1F83A0>
'''

```

</details>
</br>


## **Pág. 228 à 230............Regras para escopo de variáveis**
<details>
<summary></summary>


</details>
</br>

## **Pág. xxx à xxx............Nome | (Nome)?**
<details>
<summary></summary>


</details>
</br>

## **Pág. 247 à 248............Um decorador de registro parametrizado**
<details>
<summary></summary>

```python
registry = set()  # registry agora é um set, portanto adicionar e remover funções é mais rápido

def register(active=True):  # register aceita um argumento nomeado opcional
    def decorate(func):  # a função interna decorate é o verdadeiro decorador, observe como ela aceita uma função como argumento
        print('→ no tempo de importação (import time):\nfunção decorada: %s\nactive=%s\n' % (func, active))
        if active:   # registra func somente se o argumento active (recuperado da closure) for True
            registry.add(func)
        else:
            registry.discard(func)  # Se not active e func in registry, remove a função

        return func  # Como decorate é um decorador, ele precisa devolver uma função
    return decorate  # register é nossa fábrica de decoradores, portanto ela devolve decorate.

@register(active=False)  # A fábria @register deve ser chamada como uma função, com os parâmetros desejados
def f1():
    print('running f1()')

@register()  # Se nenhum parâmetro for passado, register ainda deve ser chamado como uma função — @register — para devolver o verdadeiro decorador decorate
def f2():
    print('running f2()')

def f3():
    print('running f3()')

print('→ no tempo de execução (runtime):\nregistry[] =', registry)
f3()

'''output:
→ no tempo de importação (import time):
função decorada: <function f1 at 0x000001FDCFF53BE0>
active=False

→ no tempo de importação (import time):
função decorada: <function f2 at 0x000001FDCFF53C70>
active=True

→ no tempo de execução (runtime):
registry[] = {<function f2 at 0x000001FDCFF53C70>}
running f3()
'''

```

</details>
</br>

