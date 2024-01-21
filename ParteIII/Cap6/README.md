# Padrões de Projeto
Em Python, existem duas abordagens principais para escrever código estruturado e reutilizável que podem determinar quando se deve usar funções e quando usar classes, a escolha depende do problema e das necessidades do código:


## **1 - Padrão de Projeto Baseado em Função (Strategy pattern function-based implementation)**
<details>
<summary></summary>

Se concentram em funções independentes e reutilizáveis (é mais modular e reutilizável).

  - Exemplo simples:
    ```python
    def saudacao(nome):
        return "Olá, " + nome + "!"

    def despedida(nome):
        return "Tchau, " + nome + "!"

    def processar_saudacao(funcao_saudacao, nome):
        return funcao_saudacao(nome)

    nome_pessoa = "Maria"
    print(processar_saudacao(saudacao, nome_pessoa))
    print(processar_saudacao(despedida, nome_pessoa))

    ```

  - Exemplo avançado:
    ```python
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    def calcular(operacao, a, b):
        return operacao(a, b)

    resultado = calcular(somar, 5, 3)
    print(resultado)

    resultado = calcular(subtrair, 10, 7)
    print(resultado)

    ```


</details>
</br>


## **2 - Padrão de Projeto Clássico Baseado em Classe (Strategy pattern clássic implementation)**
<details>
<summary></summary>

Encapsulam dados e comportamentos em um único objeto (é mais voltada para a criação de objetos).

  - Exemplo simples:
    ```python
    class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    retangulo1 = Retangulo(5, 3)
    print(retangulo1.calcular_area())

    ```

  - Exemplo avançado:
    ```python
    class Animal:
        def fazer_som(self):
            pass
          
    class Cachorro(Animal):
        def fazer_som(self):
            print("Au au!")

    class Gato(Animal):
        def fazer_som(self):
            print("Miau!")

    animais = [Cachorro(), Gato()]

    for animal in animais:
        animal.fazer_som()

    ```


</details>
</br>


<hr>

# Outros padrões além dos baseados em função e em classe

## **Programação Orientada a Eventos**
<details>
<summary></summary>

Nesse padrão, o programa é composto por uma série de eventos que ocorrem em resposta a ações do usuário ou do sistema. A biblioteca padrão de Python oferece suporte para a programação orientada a eventos através do módulo "asyncio":

  - Exemplo simples:
    ```python
    from tkinter import Tk, Button

    def botao_clicado():
        print("Botão foi clicado!")

    janela = Tk()
    botao = Button(janela, text="Clique aqui", command=botao_clicado)
    botao.pack()
    janela.mainloop()

    ```

  - Exemplo avançado:
    ```python
    import tkinter as tk

    class Aplicacao(tk.Tk):
        def __init__(self):
            super().__init__()
            self.botao = tk.Button(self, text="Clique aqui")
            self.botao.bind("<Button-1>", self.botao_clicado)
            self.botao.pack()

        def botao_clicado(self, event):
            print("Botão foi clicado!")

    app = Aplicacao()
    app.mainloop()

    ```

</details>
</br>


## **Programação Funcional**
<details>
<summary></summary>

Nesse padrão, as funções são tratadas como valores e podem ser passadas como argumentos para outras funções. Python suporta programação funcional através de recursos como funções lambda, map(), filter() e reduce().

  - Exemplo simples:
    ```python
    numeros = [1, 2, 3, 4, 5]

    dobro = list(map(lambda x: x * 2, numeros))
    print(dobro)

    soma = reduce(lambda x, y: x + y, numeros)
    print(soma)

    ```

  - Exemplo avançado:
    ```python
    from functools import reduce

    numeros = [1, 2, 3, 4, 5]

    dobro_pares = list(filter(lambda x: x % 2 == 0, map(lambda x: x * 2, numeros)))
    print(dobro_pares)

    soma = reduce(lambda x, y: x + y, numeros, 0)
    print(soma)

    ```

</details>
</br>


## **Programação Reativa**
<details>
<summary></summary>

Esse padrão é semelhante à programação orientada a eventos, mas em vez de lidar com eventos de forma imperativa, ele utiliza fluxos de dados reativos. A biblioteca "RxPY" fornece suporte para programação reativa em Python.

  - Exemplo simples:
    ```python
    import rx

    def observer(evento):
        print("Evento recebido:", evento)

    observavel = rx.from_iterable([1, 2, 3, 4, 5])
    observavel.subscribe(observer)

    ```

  - Exemplo avançado:
    ```python
    import rx
    from rx.subject import Subject
    
    subject = Subject()
    
    def observer1(evento):
        print("Observer 1:", evento)
    
    def observer2(evento):
        print("Observer 2:", evento)
    
    subject.subscribe(observer1)
    subject.on_next("Evento 1")
    subject.subscribe(observer2)
    subject.on_next("Evento 2")
    
    ```

</details>
</br>


## **Programação Assíncrona**
<details>
<summary></summary>

Esse padrão é baseado no uso de corrotinas, que são funções que podem ser pausadas e retomadas posteriormente. A programação assíncrona permite que múltiplas tarefas sejam executadas simultaneamente, o que pode melhorar o desempenho de aplicativos. Python suporta programação assíncrona através do módulo "asyncio".

  - Exemplo simples:
    ```python
    import asyncio

    async def tarefa_demorada():
        print("Iniciando tarefa...")
        await asyncio.sleep(2)
        print("Tarefa concluída!")

    async def main():
        print("Executando tarefa assíncrona...")
        await tarefa_demorada()
        print("Tarefa assíncrona concluída!")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

    ```

  - Exemplo avançado:
    ```python
    import asyncio
    
    async def tarefa_demorada():
        print("Iniciando tarefa...")
        await asyncio.sleep(2)
        print("Tarefa concluída!")
        return "Resultado da tarefa"
    
    async def main():
        print("Executando tarefa assíncrona...")
        resultado = await tarefa_demorada()
        print("Tarefa assíncrona concluída! Resultado:", resultado)
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    
    ```

</details>
</br>


## **Padrão Command**
<details>
<summary></summary>

O padrão de projeto Command é um padrão comportamental que encapsula uma solicitação como um objeto, permitindo que você parametrize clientes com diferentes solicitações, enfileire ou registre solicitações e implemente operações desfazer. Em Python, o padrão Command pode ser implementado da seguinte maneira:

1. Crie uma classe abstrata chamada Command que define a interface para todos os comandos concretos:
    ```python
    from abc import ABC, abstractmethod
    
    class Command(ABC):
        @abstractmethod
        def execute(self):
            pass
    ```
    
2. Implemente as classes concretas de comandos, que herdam da classe Command e implementam o método execute():
    ```python
    class ComandoConcreto1(Command):
        def execute(self):
            # Lógica específica do comando 1
            pass
    
    class ComandoConcreto2(Command):
        def execute(self):
            # Lógica específica do comando 2
            pass
    ```

3. Crie uma classe chamada Invoker que invoca os comandos:
    ```python
    class Invoker:
        def __init__(self):
            self._comando = None
    
        def set_comando(self, comando):
            self._comando = comando
    
        def executar_comando(self):
            self._comando.execute()
    ```

4. Utilize o padrão Command criando instâncias dos comandos e configurando o invocador:
    ```python
    comando1 = ComandoConcreto1()
    comando2 = ComandoConcreto2()
    
    invocador = Invoker()
    invocador.set_comando(comando1)
    invocador.executar_comando()
    
    invocador.set_comando(comando2)
    invocador.executar_comando()
    ```

Dessa forma, você pode criar diferentes comandos e configurá-los no invocador para que eles sejam executados quando necessário. O padrão Command ajuda a separar o objeto que emite o comando do objeto que o executa, permitindo maior flexibilidade e extensibilidade no design do seu código.

</details>
</br>


## **Pág. 205 à 207............Estudo de caso: Refatorando Strategy**
<details>
<summary></summary>

Código para o contexto dos exemplos apresentados nos outros códigos a seguir:

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

</details>
</br>


## **Pág. 208 à 210............Strategy clássico**
<details>
<summary></summary>

Padrão de Projeto Clássico Baseado em Classe (Strategy pattern clássic implementation):

```python
from abc import ABC, abstractmethod
from pag208_contexto import *

#_________↓Padrão de Projeto Clássico Baseado em Classe↓__________________
class Promotion(ABC):  # the Strategy: an Abstract Base Class

    @abstractmethod
    def discount(self, order):
        """Return discount as a positive dollar amount"""


class FidelityPromo(Promotion):  # first Concrete Strategy
    """5% discount for customers with 1000 or more fidelity points"""

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):  # second Concrete Strategy
    """10% discount for each LineItem with 20 or more units"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):  # third Concrete Strategy
    """7% discount for orders with 10 or more distinct items"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0
#_________↑Padrão de Projeto Clássico Baseado em Classe↑__________________


# dois clientes: joe não tem nenhum ponto no programa de fidelidade, ann tem 1100 pontos.
joe = Customer('John Doe', 0) 
ann = Customer('Ann Smith', 1100)

# um carrinho de compras 'banana_cart' com 30 unidades de banana e 10 maçãs 
banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
# aplicando desconto em um Order, passando a classe de promoção BulkItemPromo como argumento
Order(joe, banana_cart, BulkItemPromo()) # graças a BulkItemPromo, joe obtém um desconto de 1,5 dólar nas bananas
#output: <Order total: 30.00 due: 28.50>

# um carrinho de compras com três itens
cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]
# aplicando desconto em um Order, passando a classe de promoção FidelityPromo como argumento
Order(joe, cart, FidelityPromo()) # A promoção FidelityPromo não dá nenhum desconto a joe
#output: <Order total: 42.00 due: 42.00>
Order(ann, cart, FidelityPromo()) # A promoção FidelityPromo dá desconto de 5% na promoção a ann porque ela tem pelo menos 1000 pontos
#output: <Order total: 42.00 due: 39.90>

# o carrinho de compras 'long_order' tem 10 itens diferentes a um dólar cada
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
# aplicando desconto em um Order, passando a classe de promoção LargeOrderPromo como argumento
Order(joe, long_order, LargeOrderPromo()) # joe obtém um desconto de 7% no total do produto por causa de LargeOrderPromo
#output: <Order total: 10.00 due: 9.30>

```

</details>
</br>

## **Pág. 210 à 213............Strategy orientado a função**
<details>
<summary></summary>

Padrão de Projeto Baseado em Função (Strategy pattern function-based implementation):

```python
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
```

</details>
</br>


## **Pág. 213 à 221............Escolendo a melhor estratégia: abordagem simples | Encontrando estratégias em um módulo | Command**
<details>
<summary></summary>

Possibilidades dos benefícios disponibilizados apenas para o padrão de projeto baseado em função:

```python
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


# Possibilidade IV___________________________
# A forma mais eficiente para estes códigos é com o uso de decorador 
# → ver código em pág226a228__strategy_best4.py ou README.md do Cap 7 no TRECHO III.
# Obs: o uso de decoradores não substitui o Padrão de Projeto Baseado em Função (Strategy pattern function-based implementation), mas sim a eficiência.

```

</details>
