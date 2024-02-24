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
    return decorate  # a fábrica de decoradores devolve o decorador 'decorate', o qual tratou a função decorada 'func', através de
                     # sua função interna 'clocked', segundo seus critérios através do parâmetro de tratamento/controlador


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
