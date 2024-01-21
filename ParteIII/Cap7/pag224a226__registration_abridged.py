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
