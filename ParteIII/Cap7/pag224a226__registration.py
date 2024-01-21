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
