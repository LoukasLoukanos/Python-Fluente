
'''
→ Esse é o comportamenteo típico de um decorador: 
  Substituir a função decorada por uma nova função que aceite os mesmos argumentos e devolva 
  o que a função decorada deveria devolver, além de fazer outros processamentos também.

  No exemplo, a função factorial retorna o seu resultado definido com incrementações feitas pelo decorador clock,
  ou seja, por ser decorada pelo decorador clock, factorial é utilizada para o retorno da subfunção do decorador, 
  que adiciona informações do tempo de execução da função decorada factorial juntamente com o retorno de factorial.
'''

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

