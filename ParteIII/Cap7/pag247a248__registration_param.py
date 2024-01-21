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
