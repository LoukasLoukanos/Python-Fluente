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

**Caso b não tenha sido definido:**</br>
*→Gera erro por falta da definição*</br>
**Eventos nas variáveis a e b:**
 - Carrega 'a' como LOCAL (LOAD_FAST)
 - Carrega 'b' como GLOBAL (LOAD_GLOBAL)

```python
def f1(a):
    print(a)
    print(b)


from dis import dis
dis(f1)
# output:
  2           0 LOAD_GLOBAL              0 (print)              # Carrega a função global 'print'
              2 LOAD_FAST                0 (a)                  # Carrega 'a' como LOCAL (LOAD_FAST)
              4 CALL_FUNCTION            1                      # Chama a função 'print' com 1 argumento
              6 POP_TOP                                         # Remove o topo da pilha

  3           8 LOAD_GLOBAL              0 (print)              # Carrega a função global 'print'
             10 LOAD_GLOBAL              1 (b)                  # Carrega 'b' como GLOBAL (LOAD_GLOBAL)
             12 CALL_FUNCTION            1                      # Chama a função 'print' com 1 argumento
             14 POP_TOP                                         # Remove o topo da pilha
             16 LOAD_CONST               0 (None)               # Carrega a constante None
             18 RETURN_VALUE                                    # Retorna o valor


f1(3)
'''output:
3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in f1
NameError: name 'b' is not defined
'''

```

</br>

**Caso b tenha sido definido após a função:**</br>
*→Executa normalmente*</br>
**Eventos nas variáveis a e b:**
 - Carrega 'a' como LOCAL (LOAD_FAST)
 - Carrega 'b' como GLOBAL (LOAD_GLOBAL)

```python
def f1(a):
    print(a)
    print(b)


from dis import dis
dis(f1)
# output:
  2           0 LOAD_GLOBAL              0 (print)                          # Carrega a função global 'print'
              3 LOAD_FAST                0 (a)                              # Carrega 'a' como LOCAL (LOAD_FAST)
              6 CALL_FUNCTION            1 (1 positional, 0 keyword pair)   # Chama a função 'print' com 1 argumento
              9 POP_TOP                                                     # Remove o topo da pilha

  3          10 LOAD_GLOBAL              0 (print)                          # Carrega a função global 'print'
             13 LOAD_GLOBAL              1 (b)                              # Carrega 'b' como GLOBAL (LOAD_GLOBAL)
             16 CALL_FUNCTION            1 (1 positional, 0 keyword pair)   # Chama a função 'print' com 1 argumento
             19 POP_TOP                                                     # Remove o topo da pilha
             20 LOAD_CONST               0 (None)                           # Carrega a constante None
             23 RETURN_VALUE                                                # Retorna o valor


b = 6
f1(3)
'''output:
3
6
'''

```

</br>

**Caso algum valor seja atribuido a b na função sem definir b como global:**</br>
*→ ocorre um erro pois quando o interpretador python compila o corpo da função, ele decide que b é uma variável local, pois foi feita uma atribuição a b na função.*</br>
**Eventos nas variáveis a e b:**
 - Carrega 'a' como LOCAL (LOAD_FAST)
 - Carrega 'b' como LOCAL (LOAD_FAST)
 - Armazena o valor constante 9 na variável local 'b' (STORE_FAST)

```python
b = 6
def f2(a):
    #global b
    print(a)
    print(b)
    b = 9


from dis import dis
dis(f2)
# output:
  2           0 LOAD_GLOBAL              0 (print)                          # Carrega a função global 'print'
              3 LOAD_FAST                0 (a)                              # Carrega 'a' como LOCAL (LOAD_FAST)
              6 CALL_FUNCTION            1 (1 positional, 0 keyword pair)   # Chama a função 'print' com 1 argumento
              9 POP_TOP                                                     # Remove o topo da pilha

  3          10 LOAD_GLOBAL              0 (print)                          # Carrega a função global 'print'
             13 LOAD_FAST                1 (b)                              # Carrega 'b' como LOCAL (LOAD_FAST)
             16 CALL_FUNCTION            1 (1 positional, 0 keyword pair)   # Chama a função 'print' com 1 argumento
             19 POP_TOP                                                     # Remove o topo da pilha

  4          20 LOAD_CONST               1 (9)                              # Carrega a constante 9
             23 STORE_FAST               1 (b)                              # Armazena o valor constante 9 na variável local 'b' (STORE_FAST)
             26 LOAD_CONST               0 (None)                           # Carrega a constante None
             29 RETURN_VALUE                                                # Retorna o valor


f2(3)
'''output:
3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in f2
UnboundLocalError: local variable 'b' referenced before assignment
'''

```

</br>

**Caso algum valor seja atribuido a b na função definindo b como global:**</br>
*→ não ocorre o mesmo erro de quando o interpretador python, ao compilar o corpo da função, decidir que b é uma variável local, e executa normalmente.*</br>
**Eventos nas variáveis a e b:**
 - Carrega 'a' como LOCAL (LOAD_FAST)
 - Carrega 'b' como GLOBAL (LOAD_GLOBAL)
 - Armazena o valor constante 9 na variável global 'b' (STORE_GLOBAL)
 
```python
b = 6
def f2(a):
    global b
    print(a)
    print(b)
    b = 9


from dis import dis
dis(f3)
# output:
  3           0 LOAD_GLOBAL              0 (print)                          # Carrega a função global 'print'
              3 LOAD_FAST                0 (a)                              # Carrega 'a' como LOCAL (LOAD_FAST)
              6 CALL_FUNCTION            1 (1 positional, 0 keyword pair)   # Chama a função 'print' com 1 argumento
              9 POP_TOP                                                     # Remove o topo da pilha

  4          10 LOAD_GLOBAL              0 (print)                          # Carrega a função global 'print'
             13 LOAD_GLOBAL              1 (b)                              # Carrega 'b' como GLOBAL (LOAD_GLOBAL)
             16 CALL_FUNCTION            1 (1 positional, 0 keyword pair)   # Chama a função 'print' com 1 argumento
             19 POP_TOP                                                     # Remove o topo da pilha

  5          20 LOAD_CONST               1 (9)                              # Carrega a constante 9
             23 STORE_GLOBAL             1 (b)                              # Armazena o valor constante 9 na variável global 'b' (STORE_GLOBAL)
             26 LOAD_CONST               0 (None)                           # Carrega a constante None
             29 RETURN_VALUE                                                # Retorna o valor


f2(3)
'''output:
3
6
'''

```

</br>

**editar e descrever↓:**</br>
*descrevendo*

**Caso algum valor seja atribuido a b na função definindo b como nonlocal (escopo externo ao escopo atual):**</br>
*→ não ocorre o mesmo erro de quando o interpretador python, ao compilar o corpo da função, decidir que b é uma variável local, e executa normalmente.*</br>
**Eventos nas variáveis a e b:**
 - Carrega 'a' como LOCAL (LOAD_FAST)
 - Carrega 'b' do escopo envolvente (nonlocal) (LOAD_DEREF)
 - Armazena o valor constante 7 na variável envolvente 'b' (STORE_DEREF)
 
```python
def f4(b):
    def f5(a):
        nonlocal b # b pertence a um escopo externo ao escopo atual, mas não é global (explicação de nonlocal abaixo↓↓↓ )
        print(a)
        print(b)
        b = 7
    return f5


from dis import dis
dis(f5)
# output:
  4           0 LOAD_GLOBAL              0 (print)                          # Carrega a função global 'print'
              2 LOAD_FAST                0 (a)                              # Carrega 'a' como LOCAL (LOAD_FAST)
              4 CALL_FUNCTION            1                                  # Chama a função 'print' com 1 argumento
              6 POP_TOP                                                     # Remove o topo da pilha

  5           8 LOAD_GLOBAL              0 (print)                          # Carrega a função global 'print'
             10 LOAD_DEREF               0 (b)                              # Carrega 'b' do escopo envolvente (nonlocal) (LOAD_DEREF)
             12 CALL_FUNCTION            1                                  # Chama a função 'print' com 1 argumento
             14 POP_TOP                                                     # Remove o topo da pilha

  6          16 LOAD_CONST               1 (7)                              # Carrega a constante 7
             18 STORE_DEREF              0 (b)                              # Armazena o valor constante 7 na variável envolvente 'b' (STORE_DEREF)
             20 LOAD_CONST               0 (None)                           # Carrega a constante None
             22 RETURN_VALUE                                                # Retorna o valor


f5 = f4(8)
f5(2)
'''output:
2
8
'''

```

</details>
</br>


## **Pág. 232 à 234............Closures**
<details>
<summary></summary>

### Closures
Uma closure em Python ocorre quando uma função definida dentro de outra função (função interna) faz referência a variáveis da função externa (função externa). Essas variáveis são "capturadas" pela função interna, permitindo que ela as acesse mesmo após a conclusão da execução da função externa. Isso cria um escopo estendido para a função interna, tornando-a uma closure.</br></br>

Além disso, as closures podem acessar variáveis globais definidas fora de seu escopo, mas não podem modificar essas variáveis diretamente, a menos que sejam declaradas como globais explicitamente. Isso é útil para manter um estado persistente entre chamadas de função sem a necessidade de variáveis globais.</br></br>

Em síntese, as closures em Python oferecem uma maneira poderosa de criar funções com escopo estendido, permitindo o acesso a variáveis externas e mantendo um estado persistente. Essa capacidade é especialmente útil em situações onde funções aninhadas são necessárias para encapsular comportamentos específicos.</br></br>

Resumindo, uma closure é uma função que preserva as associações com as variáveis livres existentes quando a função é definida, 
de modo que elas possam ser usadas posteriormente quando a função for chamada e o escopo de definição não estiver mais disponível.</br></br>

→ Note que a única situação em que uma função pode precisar lidar com variáveis 
  externas que não sejam globais é quando ela está aninhada em outra função</br></br>

#### **Exemplo:**

```python

# Um exemplo de classe (não de função Closure) ____________________________________________

class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

# a classe Avarager cria instâncias que são invocáveis → _ _call_ _

avg = Averager()
avg(10)
# output: 10.0 → sem média

avg(11)
# output: 10.5 → média entre 10 e 11

avg(12)
# output: 11.0 → média entre 10 e 12



# Um exemplo de função Closure ___________________________________________________________

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager

# a função make_averager devolve um objeto função averager → return


'''
'series' é uma variável livre (free variable) → termo técnico: indica que uma variável não tem uma associação no escopo local

A inspeção do objeto averager devolvido mostra como python mantém os nomes das variáveis
locais e livres no atributo _ _code_ _, que representa o corpo compilado da função
'''

avg2 = make_averager() # Criando uma instância da função make_averager


# Acessando variáveis locais da função interna (averager)
local_variables = avg2.__code__.co_varnames
print(local_variables)  # ('new_value', 'total')

# Acessando variáveis livres (free variables)
free_variables = avg2.__code__.co_freevars
print(free_variables)  # ('series',)

# Acessando o conteúdo das células (closure)
closure_contents = avg2.__closure__[0].cell_contents
print(closure_contents)  # []


avg2(10)
# output: 10.0 → sem média

avg2(11)
# output: 10.5 → média entre 10 e 11

avg2(12)
# output: 11.0 → média entre 10 e 12

# Acessando novamente o conteúdo das células após a modificação da closure
closure_contents_after_append = avg2.__closure__[0].cell_contents
print(closure_contents_after_append)  # [10, 11, 12]


'''
Se executar avg2.__closure__, obterá um objeto que representa as células de closure associadas à função avg2. 
O retorno é algo semelhante a (<cell at 0x107a44f78: list object at 0x107a91a48>,). 
Isso significa que há uma célula na closure, e essa célula está referenciando um objeto do tipo lista.

Para entender mais sobre o conteúdo específico dessa célula, podemos acessar o conteúdo da célula usando 
avg2.__closure__[0].cell_contents. Nesse caso, o conteúdo da célula seria o objeto da lista que a função 
está "lembrando". Se você adicionou valores à lista através da função avg2, o conteúdo da célula refletirá 
essas alterações.
'''

```

</details>
</br>



## **Pág. 235 à 236............Declaração nonlocal**
<details>
<summary></summary>

A declaração ***nonlocal*** foi introduzida no python 3, ela permite sinalizar 
uma varável como *livre*, mesmo que ela receba um novo valor na função.

```python
# Sem declaração nonlocal______________________________________

'''
Ao tentar refazer a associação em count = count + 1 no corpo da função, foi criado implicitamente a variável local count.
Nesse caso count deixou de ser uma variável livre, sendo assim, não salva na closure, causando o erro de referenciamento.
'''

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total/count

    return averager

avg = make_averager()
avg(10)
'''output:
Traceback (most recent call last):
  File "main.py", line 13, in <module>
    avg(10)
  File "main.py", line 6, in averager
    count += 1
UnboundLocalError: local variable 'count' referenced before assignment
'''


# Com declaração nonlocal______________________________________

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total/count

    return averager

avg = make_averager()
avg(10)
#output: 10.0

```

</details>
</br>


## **Pág. 237 à 238............Implementando um decorador simples**
<details>
<summary></summary>

### **→ O comportamenteo típico de um decorador:**
*Substituir a função decorada por uma nova função que aceite os mesmos argumentos e devolva*</br>
*o que a função decorada deveria devolver, além de fazer outros processamentos também.*</br>

</br>

No exemplo, a ***função factorial*** retorna o seu resultado definido com incrementações feitas pelo **decorador clock**,</br>
ou seja, por ser ***decorada*** pelo **decorador clock**, ***factorial*** é utilizada para o retorno da **subfunção do decorador**,</br>
o qual adiciona informações do tempo de execução da ***função decorada factorial*** juntamente com o retorno de *factorial*.</br>

```python
import time

def clock(func):
    def clocked(*args): # aceita qualquer quantidade de argumentos posicionais
        t0 = time.time() # Obtém o tempo atual em segundos (ex: 26/01/22 às 18:08)
        result = func(*args) # Chama a função original e armazena o resultado
        elapsed = time.time() - t0 # Calcula o tempo decorrido subtraindo o inicial t0 do final
        name = func.__name__ # Obtém o nome da função original
        arg_str = ', '.join(repr(arg) for arg in args) # Cria uma string representando os argumentos
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result)) # Imprime uma mensagem formatada com informações sobre a execução da função
        return result # Retorna o resultado da execução da função original
    return clocked # Retorna a função interna decorada


@clock # Define uma função decorada 'snooze' que pausa a execução por um número de segundos
def snooze(seconds):
    time.sleep(seconds)


@clock # Define uma função decorada 'factorial' que calcula o fatorial de um número
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

if __name__ == '__main__': # Bloco executado quando o script é executado diretamente
    print('_' * 40, 'Calling snooze(.123)') # Imprime uma linha de asteriscos indicando a chamada da função 'snooze'
    snooze(.123) # Chama a função 'snooze' com o argumento 0.123 (tempo em segundos)
    print('_' * 40, 'Calling factorial(6)') # Imprime uma linha de asteriscos indicando a chamada da função 'factorial'
    print('6! =', factorial(6)) # Chama a função 'factorial' com o argumento 6 e imprime o resultado
    print('referência armazenada em factorial:', factorial.__name__) # factorial armazenará uma referência à função clocked


'''output:
________________________________________ Calling snooze(.123)
[0.12324572s] snooze(0.123) -> None
________________________________________ Calling factorial(6)
[0.00000143s] factorial(1) -> 1
[0.00002337s] factorial(2) -> 2
[0.00003552s] factorial(3) -> 6
[0.00004721s] factorial(4) -> 24
[0.00005960s] factorial(5) -> 120
[0.00007534s] factorial(6) -> 720
6! = 720
referência armazenada em factorial: clocked
'''

```

</details>
</br>


## **Pág. 239 à 240............Decorador @functools.wraps (Pág. 237 à 238...versão melhorada de 'Implementando um decorador simples')**
<details>
<summary></summary>

O decorador @functools.wraps é usado para preservar os metadados da função original quando você está criando um decorador. Ele é uma ferramenta útil para garantir que a função decorada mantenha as informações relevantes da função original, como o nome da função, a documentação, as anotações e assim por diante.</br>

Ao criar um decorador, você define uma função interna (decorador) que envolve a função original. No entanto, ao fazer isso, você pode acabar substituindo metadados importantes da função original pela função interna, o que pode causar confusão ao usar ferramentas que dependem dessas informações (por exemplo, ferramentas de geração de documentação).</br>

O @functools.wraps(func) resolve esse problema, atualizando a função interna com os metadados da função original. Isso significa que, quando você usa @functools.wraps, a função interna terá o mesmo nome, docstring, anotações e outros metadados da função original.</br>

Portanto, o uso de @functools.wraps é uma prática recomendada ao criar decoradores para garantir que as informações importantes da função original sejam mantidas na função decorada.</br>
 
</br>

#### **Exemplo Simples:**

```python
import functools

# Define um decorador chamado my_decorator
def my_decorator(func):
    # Usa functools.wraps para preservar os metadados da função original
    @functools.wraps(func)
    # Define uma função interna chamada wrapper que envolve a função original
    def wrapper(*args, **kwargs):
        print("Decorator executing")  # Imprime uma mensagem indicando que o decorador está sendo executado
        # Chama a função original e retorna o resultado
        return func(*args, **kwargs)
    
    # Retorna a função interna wrapper decorada
    return wrapper

# Usa o decorador my_decorator para decorar a função example_function
@my_decorator
def example_function():
    """This is an example function."""
    print("Function executing")  # Imprime uma mensagem indicando que a função está sendo executada


# Se não usarmos @functools.wraps, a docstring e o nome podem ser afetados
print(example_function.__name__)  # Output: wrapper
print(example_function.__doc__)   # Output: None

# Usando @functools.wraps, preservamos os metadados da função original
print(example_function.__name__)  # Output: example_function
print(example_function.__doc__)   # Output: This is an example function.

```

</br>

#### **Versão melhorada de 'Pág. 237 à 238...Implementando um decorador simples' com o uso do decorador @functools.wraps(func):**

```python
import time  # Importa o módulo de tempo
import functools  # Importa o módulo functools para ajudar na criação do decorador

def clock(func):
    @functools.wraps(func)  # Usa o decorador wraps para preservar metadados da função original
    def clocked(*args, **kwargs):  # Define uma função interna que aceita qualquer quantidade de argumentos posicionais
        t0 = time.time()  # Obtém o tempo inicial em segundos
        result = func(*args, **kwargs)  # Chama a função original e armazena o resultado
        elapsed = time.time() - t0  # Calcula o tempo decorrido subtraindo o tempo inicial do tempo final
        name = func.__name__  # Obtém o nome da função original
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))  # Cria uma string representando os argumentos posicionais
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))  # Cria uma string representando os argumentos nomeados
        arg_str = ', '.join(arg_list)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))  # Imprime uma mensagem formatada com informações sobre a execução da função
        return result  # Retorna o resultado da execução da função original
    return clocked  # Retorna a função interna decorada
    
@clock # Define uma função decorada 'snooze' que pausa a execução por um número de segundos
def snooze(seconds):
    time.sleep(seconds)


@clock # Define uma função decorada 'factorial' que calcula o fatorial de um número
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

if __name__ == '__main__': # Bloco executado quando o script é executado diretamente
    # → as linhas comentadas abaixo trazem o mesmo resultado do código 'Pág. 237 à 238...Implementando um decorador simples',
    # o objetivo aqui é frizar que usando @functools.wraps, preservamos os metadados da função original, observe factorial.__name__:
    
    '''
    print('_' * 40, 'Calling snooze(.123)') # Imprime uma linha de asteriscos indicando a chamada da função 'snooze'
    snooze(.123) # Chama a função 'snooze' com o argumento 0.123 (tempo em segundos)
    print('_' * 40, 'Calling factorial(6)') # Imprime uma linha de asteriscos indicando a chamada da função 'factorial'
    print('6! =', factorial(6)) # Chama a função 'factorial' com o argumento 6 e imprime o resultado
    '''

    print('referência armazenada em factorial:', factorial.__name__) # factorial armazenará uma referência à função clocked


#output: referência armazenada em factorial: factorial

'''
salientando que em 'Pág. 237 à 238...Implementando um decorador simples' o resultado do output é:
output: referência armazenada em factorial: clocked
ou seja, não foi preservado os metadados da função original
'''

```

</details>
</br>


## **Pág. 240 à 242............Decoradores da biblioteca padrão | Memorização com o Decorador functools.lru_cache**
<details>
<summary></summary>

A memorização (caching) é uma técnica utilizada para armazenar os resultados de chamadas de função com determinados argumentos, a fim de evitar recálculos custosos quando a mesma chamada é feita novamente com os mesmos argumentos. O módulo functools em Python fornece o decorador lru_cache (Least Recently Used Cache) que pode ser usado para implementar memorização de forma eficiente.

### Características importantes do **functools.lru_cache**:

**Funcionamento:**</br>
lru_cache armazena as chamadas mais recentes da função e seus resultados em um cache limitado por tamanho. Quando a capacidade máxima do cache é atingida, as entradas menos recentemente usadas são removidas para abrir espaço para novas entradas.
</br>

**Decoração de Funções:**</br>
O lru_cache é utilizado como um decorador e deve ser colocado acima da definição da função que você deseja memorizar.

```python
from functools import lru_cache

@lru_cache(maxsize=None)  # maxsize=None significa um cache de tamanho ilimitado
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```
</br>

**Parâmetro maxsize:**
O parâmetro maxsize determina o número máximo de chamadas que serão armazenadas no cache. Se maxsize for definido como None (padrão), o cache será de tamanho ilimitado.
</br>

**Eficiência:**
A lru_cache é eficiente em termos de memória e pode significativamente acelerar funções recursivas ou que envolvem cálculos intensivos, ao evitar a recálculo de resultados para as mesmas entradas.

```python
# Exemplo de uso
result = fibonacci(5)
```
</br>

**Invalidação do Cache:**
Em algumas situações, pode ser necessário invalidar manualmente o cache. Isso pode ser feito chamando o método cache_clear() na função decorada.

```python
fibonacci.cache_clear()  # Limpa o cache da função fibonacci
```

É importante observar que a lru_cache deve ser usada com cuidado, pois ela armazena resultados anteriores em memória. Em situações em que a função pode ter um conjunto muito grande de entradas únicas, pode ser necessário ajustar o maxsize ou considerar outras estratégias de cache.

### **Exemplo de uso da técnica de otimização com o decorador functools.lru_cache**
Nota importante:
 - Para calcular fibonacci(30), com functools.lru_cache, 31 chamadas serão feitas em 0,0005s (aproximadamente) em um Core i7;
 - Para calcular fibonacci(30), sem functools.lru_cache, 2.692.537 chamadas serão feitas em 17,7s (aproximadamente) em um Core i7.

```python
# contextualização_____________________________________________________________________________________________________
import time

def clock(func):
    def clocked(*args): # aceita qualquer quantidade de argumentos posicionais
        t0 = time.time() # Obtém o tempo atual em segundos (ex: 26/01/22 às 18:08)
        result = func(*args) # Chama a função original e armazena o resultado
        elapsed = time.time() - t0 # Calcula o tempo decorrido subtraindo o inicial t0 do final
        name = func.__name__ # Obtém o nome da função original
        arg_str = ', '.join(repr(arg) for arg in args) # Cria uma string representando os argumentos
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result)) # Imprime uma mensagem formatada com informações sobre a execução da função
        return result # Retorna o resultado da execução da função original
    return clocked # Retorna a função interna decorada

# contextualização_____________________________________________________________________________________________________


# sem o uso de functools.lru_cache_____________________________________________________________________________________
# ♦ Exemplo dispondo de muita recursividade de forma repetitiva onde esses procedimentos poderiam ser evitados de forma 
#   otimizada salvando os resultados de chamadas prévias com a técnica de otimização com o decorador functools.lru_cache 

@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    print(fibonacci(6))

'''output:
[0.00000095s] fibonacci(0) -> 0
[0.00000072s] fibonacci(1) -> 1
[0.00002265s] fibonacci(2) -> 1
[0.00000048s] fibonacci(1) -> 1
[0.00000048s] fibonacci(0) -> 0
[0.00000072s] fibonacci(1) -> 1
[0.00001144s] fibonacci(2) -> 1
[0.00002265s] fibonacci(3) -> 2
[0.00005531s] fibonacci(4) -> 3
[0.00000072s] fibonacci(1) -> 1
[0.00000048s] fibonacci(0) -> 0
[0.00000072s] fibonacci(1) -> 1
[0.00001097s] fibonacci(2) -> 1
[0.00002098s] fibonacci(3) -> 2
[0.00000048s] fibonacci(0) -> 0
[0.00000048s] fibonacci(1) -> 1
[0.00001097s] fibonacci(2) -> 1
[0.00000048s] fibonacci(1) -> 1
[0.00000048s] fibonacci(0) -> 0
[0.00000048s] fibonacci(1) -> 1
[0.00001097s] fibonacci(2) -> 1
[0.00002170s] fibonacci(3) -> 2
[0.00004268s] fibonacci(4) -> 3
[0.00007319s] fibonacci(5) -> 5
[0.00013947s] fibonacci(6) -> 8
8
'''
# •→ Desperdício evidente: fibonacci(1) é chamado oito vezes, fibonacci(2) é chamado cinco vezes, etc...
# sem o uso de functools.lru_cache_____________________________________________________________________________________


# Com o uso de functools.lru_cache_____________________________________________________________________________________
# ♦ Exemplo dispondo de pouca recursividade, evitando repetições de procedimentos, salvando os 
#   resultados de chamadas prévias com a técnica de otimização com o decorador functools.lru_cache,

import functools

@functools.lru_cache() # sem parâmetros
@clock  # DECORADORES EMPILHADOS (@lru_cache() é aplicado à função fibonacci() devolvida por @clock)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    print(fibonacci(6))


'''output:
[0.00000024s] fibonacci(0) -> 0
[0.00000024s] fibonacci(1) -> 1
[0.00001454s] fibonacci(2) -> 1
[0.00000072s] fibonacci(3) -> 2
[0.00002146s] fibonacci(4) -> 3
[0.00000072s] fibonacci(5) -> 5
[0.00002861s] fibonacci(6) -> 8
8
'''
# •→ Alto desempenho evidente: o tempo de execução cai para a metade e a função é chamada somente uma vez para cada valor de n
# Com o uso de functools.lru_cache_____________________________________________________________________________________

```

</details>
</br>


## **Pág. 243 à 245............Funções genéricas com dispatch simples**
<details>
<summary></summary>
Não temos sobrecarga de método nem de função em Python, não podendo criar variações de funções com assinaturas diferentes.</br>
→ Uma solução para isso seria utilizar uma função de despacho (dispatch), com uma cadeia de if/elif/elif para cada ocasião.</br>
→ O decorador functools.singledispatch permite tornar funções e classes genéricas para realizar uma "sobrecarga de método".</br>
</br>

Na verdade, singledispatch não foi concebido para replicar a sobrecarga de métodos no estilo Java em Python. Em vez disso, singledispatch foi projetado para facilitar a extensão modular de funcionalidades em Python. Com singledispatch, cada módulo pode registrar uma função especializada para lidar com um tipo específico de argumento, permitindo uma abordagem modular e flexível para estender o comportamento de funções em toda a aplicação. Isso significa que diferentes partes do código podem fornecer implementações especializadas para tipos específicos, promovendo a reusabilidade do código e mantendo uma estrutura modular e organizada.
</br>

Quando você decora uma função com @singledispatch e, em seguida, registra funções especializadas para tipos específicos com 
@funcao.register(tipo), você está dizendo que, para cada tipo registrado, uma função específica deve ser usada para lidar com 
esse tipo. Isso permite que você estenda o comportamento de uma função para novos tipos sem modificar sua implementação original.
</br>

#### **Exemplo: Depurando aplicações web, gerando visualizações em HTML para diferentes tipos de objetos**
```python
from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch  # singledispatch marca a função base que trata o tipo object
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)  # cada função especializada é decorada com @funcao_base.register(tipo)
def _(text):            #  o nome das funções especializadas é irrelevante; _ é uma boa opção para deixar isso claro
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)  # Para cada tipo adicional que vá receber um tratamento especial, registre uma nova funçlão. 'numbers.Integral' é uma superclasse virtual de inteiro
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)  # você pode empilhar diversos decoradores register para dar suporte a tipos diferentes com a mesma função
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


htmlize({1, 2, 3})  # por padrão a repr de um objeto com escape HTML é mostrada entre <pre></pre>
                    # output: '<pre>{1, 2, 3}</pre>'

htmlize(abs) # por padrão a repr de um objeto com escape HTML é mostrada entre <pre></pre>
             # output: '<pre>&lt;built-in function abs&gt;</pre>'

htmlize('Heimlich & Co.\n- a game')  # objetos string também têm escape HTML, mas são colocados entre <p></p> com quebras de linhas <br>
                                     # output: '<p>Heimlich &amp; Co.<br>\n- a game</p>'

htmlize(42)  # um int é mostrado em decimal e hexadecimal entre <pre></pre>
             # output: '<pre>42 (0x2a)</pre>'

print(htmlize(['alpha', 66, {3, 2, 1}]))  # cada item da lista é formado segundo o seu tipo e a sequência toda é representada como uma lista HTML
                                          '''output:
                                          <ul>
                                            <li><p>alpha</p></li>
                                            <li><pre>66 (0x42)</pre></li>
                                            <li><pre>{1, 2, 3}</pre></li>
                                          </ul>
                                          '''

```

</details>
</br>


## **Pág. 246 à 248............Decoradores Empilhados | Decoradores Parametrizados | Um decorador de registro parametrizado**
<details>
<summary></summary>

### Fábrica de Decoradores

***→ Uma fábrica de decoradores é uma função que encapsula o decorador tendo um argumento de tratamento/controlador responsável por determinar os critérios de funcionamento do decorador, como uma fábrica geradora de decoradores***

#### **Exemplo: Decorador comum com parâmetro simples (sem fábrica de decoradores)**
```python
def meu_decorador(funcao):
    def wrapper(*args, **kwargs):
        print("Tratamento normal")
        resultado = funcao(*args, **kwargs)
        return resultado
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função sendo executada")

minha_funcao()

```

#### **Exemplo: Fábrica de decoradores contendo seu parâmetro de tratamento/controlador**
```python
def fabrica_de_decoradores(parametro_de_tratamento):
    def meu_decorador(funcao):
        def wrapper(*args, **kwargs):
            if parametro_de_tratamento:
                # Lógica específica se o parâmetro de tratamento estiver ativado
                print("Tratamento especial ativado")
            else:
                print("Tratamento normal")
            resultado = funcao(*args, **kwargs)
            return resultado
        return wrapper
    return meu_decorador

# Uso da fábrica de decoradores para criar um decorador com tratamento especial
decorador_com_tratamento = fabrica_de_decoradores(parametro_de_tratamento=True)

@decorador_com_tratamento
def minha_funcao():
    print("Minha função sendo executada")

minha_funcao()
```
</br>

Em suma, uma fábrica de decoradores com argumento de tratamento/controlador pode ser útil em várias situações, proporcionando uma maneira flexível e dinâmica de criar decoradores adaptáveis.
</br>

**Circunstâncias aplicáveis:**

  - **Personalização Dinâmica:** Você pode usar uma fábrica de decoradores para criar decoradores personalizados com base em parâmetros específicos fornecidos durante a execução do programa. Isso permite ajustar dinamicamente o comportamento dos decoradores com base em diferentes circunstâncias.

  - **Modularidade e Reutilização:** Uma fábrica de decoradores permite encapsular a lógica de criação de decoradores em uma função separada, promovendo a reutilização e a modularidade do código. Isso facilita a criação de vários decoradores com comportamentos diferentes, compartilhando a mesma lógica de criação.

  - **Configuração Flexível:** Com uma fábrica de decoradores, você pode configurar o comportamento dos decoradores de maneira flexível, fornecendo diferentes argumentos de tratamento ou controladores. Isso permite uma maior adaptabilidade e personalização do comportamento dos decoradores de acordo com os requisitos específicos.

  - **Abstração de Complexidade:** Uma fábrica de decoradores pode abstrair a complexidade da criação de decoradores, especialmente quando a lógica de criação envolve múltiplos passos ou depende de várias condições. Isso torna o código mais limpo e fácil de entender, separando a criação de decoradores da lógica de negócios.

  - **Padrões de Projeto:** Uma fábrica de decoradores com argumento de tratamento/controlador pode ser útil na implementação de padrões de projeto, como o padrão Strategy, onde diferentes estratégias podem ser encapsuladas em decoradores e selecionadas dinamicamente com base em parâmetros específicos.


#### **Exemplo 1 do livro: Decorador comum com parâmetro simples (sem fábrica de decoradores)**
```python
registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func) 
    return func

@register
def f1():
    print('running f1()')


print('running main()')
print('registry ->', registry)
f1()

```

#### **Exemplo 2 do livro: Fábrica de decoradores contendo seu parâmetro de tratamento/controlador**
```python
registry = set()  # registry agora é um set, portanto adicionar e remover funções é mais rápido

def register(active=True):  # register aceita um argumento de tratamento/controlador nomeado opcional
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


## **Pág. 249 à 252............Decorador clock parametrizado**
<details>
<summary></summary>

```python
import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):  # 'clock' é a fábrica de decoradores parametrizada com seu parâmetro de tratamento/controlador
    def decorate(func):      # 'decorate' é o decorador
        def clocked(*_args): # função interna do decorador 
            t0 = time.time()
            _result = func(*_args)  # _result é o verdadeiro resultado da função decorada 'func' (recebida como argumento da subfunção 'clocked' do decorador 'decorate')
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)  # 'args' armazena o argumento da função interna 'clocked', enquanto 'args' é o str usado para exibição
            result = repr(_result)  # 'result' ´-e a exibição em str de _result para exibição
            print(fmt.format(**locals()))  # usar **locals() nesse caso permite que qualquer variável local da função interna 'clocked' seja referenciada em fmt
            return _result  # 'clocked' substituirá a função decorada, portanto deve devolver o que essa função devolve
        return clocked  # o decorador 'decorate' retorna a sua função interna 'clocked'
    return decorate  # a fábrica de decoradores devolve o decorador 'decorate', o qual tratou a função decorada 'func', através de sua função interna 'clocked', segundo seus critérios através do parâmetro de tratamento/controlador


'''↑↓ a versão da fábrica 'clock' em classe:

class clock:

    def __init__(self, fmt=DEFAULT_FMT):
        self.fmt = fmt

    def __call__(self, func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(self.fmt.format(**locals()))
            return _result
        return clocked

'''

if __name__ == '__main__':
    #Exemplo 1 _________________________________________________________________
    # → a fábrica de decoradores parametrizada 'clock()' é chamada sem argumentos, portanto o decorador 'decorate' usará o str de formatação default
    
    @clock()
    def snooze(seconds):
        time.sleep(seconds)


    for i in range(3):
        snooze(.123)

    #        ↓[{elapsed:0.8f}s] {name}({args}) -> {result}
    '''output: 
              [0.12445855s] snooze(0.123) -> None
              [0.12317610s] snooze(0.123) -> None
              [0.12319660s] snooze(0.123) -> None
    '''

    snooze(.1) # doctest: +ELLIPSIS
    #output:  [0.10391760s] snooze(0.1) -> None
    
    clock('{name}: {elapsed}')(time.sleep)(.2) # doctest: +ELLIPSIS
    #output:  sleep: 0.20324087142944336
    
    clock('{name}({args}) dt={elapsed:0.3f}s')(time.sleep)(.2)
    #output:  sleep(0.2) dt=0.201s


    #Exemplo 2 _________________________________________________________________
    # → a fábrica de decoradores parametrizada 'clock()' é chamada com argumento
    @clock('{name}: {elapsed}s') 
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)

    #        ↓{name}: {elapsed}s
    '''output: 
              snooze: 0.12327885627746582s
              snooze: 0.1231851577758789s
              snooze: 0.12329745292663574s
    '''

    snooze(.1) # doctest: +ELLIPSIS
    #output:  snooze: 0.10014104843139648s
    
    clock('{name}: {elapsed}')(time.sleep)(.2) # doctest: +ELLIPSIS
    #output:  sleep: 0.2003486156463623
    
    clock('{name}({args}) dt={elapsed:0.3f}s')(time.sleep)(.2)
    #output:  sleep(0.2) dt=0.200s
    
    #Exemplo 3 _________________________________________________________________
    # → a fábrica de decoradores parametrizada 'clock()' é chamada com argumento

    @clock('{name}({args}) dt={elapsed:0.3f}s')
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)
 
    #        ↓{name}: {elapsed}s
    '''output: 
              snooze(0.123) dt=0.123s
              snooze(0.123) dt=0.123s
              snooze(0.123) dt=0.123s
    '''

    snooze(.1) # doctest: +ELLIPSIS
    #output:  snooze(0.1) dt=0.100s
    
    clock('{name}: {elapsed}')(time.sleep)(.2) # doctest: +ELLIPSIS
    #output:  sleep: 0.20033049583435059
    
    clock('{name}({args}) dt={elapsed:0.3f}s')(time.sleep)(.2)
    #output:  sleep(0.2) dt=0.200s

```

</details>
</br>


## **Quando usar Decoradores e quando usar Classes em python**
Decidir entre o uso de decoradores e o uso de classes em Python depende das necessidades específicas do seu código, do contexto em que está trabalhando e das preferências pessoais. Aqui estão algumas considerações que podem ajudá-lo a decidir quando usar um decorador em vez de uma classe, e vice-versa:</br>

#### **Use Decoradores Quando:**
 - **Funcionalidades Adicionais:** Você quer adicionar funcionalidades extras a funções ou métodos existentes de forma transparente, sem modificar o código original. Os decoradores são úteis para aplicar lógicas de pré-processamento ou pós-processamento em funções, como logging, autenticação, controle de acesso, entre outros.

 - **Sintaxe Concisa:** Os decoradores podem fornecer uma maneira mais concisa de aplicar comportamentos a funções ou métodos, sem a necessidade de criar uma classe e instanciá-la.

 - **Reutilização Simples:** Se a lógica que você deseja aplicar é genérica o suficiente para ser reutilizada em várias funções ou métodos diferentes, os decoradores podem ser uma escolha melhor, pois podem ser aplicados a qualquer função ou método compatível.

#### **Use Classes Quando:**
 - **Estado e Comportamento Combinados:** Se a funcionalidade que você está implementando exige tanto estado quanto comportamento, as classes são uma escolha natural. As classes em Python permitem combinar dados (atributos) e comportamento (métodos) em um único objeto.

 - **Encapsulamento:** Se você precisa de controle mais granular sobre o acesso aos atributos e métodos, as classes oferecem suporte ao encapsulamento, permitindo que você defina atributos e métodos como públicos, privados ou protegidos.

 - **Herança e Polimorfismo:** Se você precisa de herança ou polimorfismo em sua estrutura, as classes em Python fornecem recursos robustos para isso. Você pode estender e especializar comportamentos de classes base em classes derivadas.

 - **Complexidade Maior:** Se a lógica que você está implementando é complexa o suficiente para justificar uma estrutura mais formal e orientada a objetos, as classes oferecem uma maneira mais organizada de modelar e manter essa complexidade.

***Em resumo:***</br>
*→ Decoradores são ótimos para adicionar funcionalidades a funções ou métodos existentes de forma concisa e genérica;*</br>
*→ Classes são mais adequadas quando você precisa combinar estado e comportamento, encapsular dados, usar herança e polimorfismo, ou lidar com lógica mais complexa e estruturada. A escolha entre decoradores e classes depende das necessidades específicas do seu projeto e das melhores práticas de design.*
