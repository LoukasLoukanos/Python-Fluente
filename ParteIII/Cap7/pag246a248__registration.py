''' → FÁBRICA DE DECORADORES ←
→ Uma fábrica de decoradores é uma função que encapsula o decorador tendo um argumento de tratamento/controlador 
  responsável por determinar os critérios de funcionamento do decorador, como uma fábrica geradora de decoradores 
'''

# Exemplo: Decorador comum com parâmetro simples (sem fábrica de decoradores)_________________________________________
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


# Exemplo: Fábrica de decoradores contendo seu parâmetro de tratamento/controlador____________________________________
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

'''
Em suma, Uma fábrica de decoradores com argumento de tratamento/controlador pode ser útil em várias situações, 
proporcionando uma maneira flexível e dinâmica de criar decoradores adaptáveis. 

Aqui estão algumas circunstâncias em que isso pode ser aplicado:

→ Personalização Dinâmica: 
Você pode usar uma fábrica de decoradores para criar decoradores personalizados com base em parâmetros 
específicos fornecidos durante a execução do programa. Isso permite ajustar dinamicamente o comportamento 
dos decoradores com base em diferentes circunstâncias.

→ Modularidade e Reutilização: 
Uma fábrica de decoradores permite encapsular a lógica de criação de decoradores em uma função separada, 
promovendo a reutilização e a modularidade do código. Isso facilita a criação de vários decoradores com 
comportamentos diferentes, compartilhando a mesma lógica de criação.

→ Configuração Flexível: 
Com uma fábrica de decoradores, você pode configurar o comportamento dos decoradores de maneira flexível, 
fornecendo diferentes argumentos de tratamento ou controladores. Isso permite uma maior adaptabilidade e 
personalização do comportamento dos decoradores de acordo com os requisitos específicos.

→ Abstração de Complexidade: 
Uma fábrica de decoradores pode abstrair a complexidade da criação de decoradores, especialmente quando a 
lógica de criação envolve múltiplos passos ou depende de várias condições. Isso torna o código mais limpo 
e fácil de entender, separando a criação de decoradores da lógica de negócios.

→ Padrões de Projeto: 
Uma fábrica de decoradores com argumento de tratamento/controlador pode ser útil na implementação de padrões 
de projeto, como o padrão Strategy, onde diferentes estratégias podem ser encapsuladas em decoradores e 
selecionadas dinamicamente com base em parâmetros específicos.
'''



# Exemplo 1 do livro: decorador comum com parâmetro simples (sem fábrica de decoradores)______________________________
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


# Exemplo 2 do livro: decorador com fábrica de decoradores contendo seu parâmetro de tratamento/controlador___________
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


