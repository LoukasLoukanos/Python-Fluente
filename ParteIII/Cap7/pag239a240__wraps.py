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