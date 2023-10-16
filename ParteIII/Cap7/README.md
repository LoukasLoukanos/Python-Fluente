## **Decoradores (decorators) de função e closures**
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

### ***Quando Python executa os decoradores:***
```python
#_________BEGIN REGISTRATION_________

registry = []  # registy armazenará referências a funções decoradas com @register.

def register(func):  # register recebe uma função como argumento.
    print('running register(%s)' % func)  # exibe a função que está sendo decorada, para demonstração.
    registry.append(func)  # inclui func e registry.
    return func  # devolve func: precisamos devolver uma funçõa; nesse caso, devolvemos a mesma função recebida como argumento.

@register  # f1 e f2 são decoradas com @register.
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():  # f3 não é decorada.
    print('running f3()')

def main():  # main exibe registry e então chama f1(), f2() e f3().
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__=='__main__':
    main()  # main() é chamado somente se registration.py executar como script.

#_________END REGISTRATION_________

'''
output:
running register(<function f1 at 0x000001A807A33B50>)
running register(<function f2 at 0x000001A807A33BE0>)
running main()
registry -> [<function f1 at 0x000001A807A33B50>, <function f2 at 0x000001A807A33BE0>]
running f1()
running f2()
running f3()
'''
```
