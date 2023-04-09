"""
 Encurta um texto para um comprimento máximo especificado. Se o texto fornecido for mais longo do que o comprimento máximo 
 especificado, a função encontra o último espaço antes ou depois da posição máxima permitida e encurta o texto até esse ponto. 
 Se não houver espaços no texto, a função simplesmente encurta o texto para o comprimento máximo permitido.
"""

def clip(text, max_len=80):
    # Inicializa a variável 'end' como 'None'
    end = None
    # Verifica se o comprimento do texto é maior do que o comprimento máximo permitido
    if len(text) > max_len:
        # Procura a posição do último espaço no texto antes da posição máxima permitida
        space_before = text.rfind(' ', 0, max_len)
        # Se a posição do último espaço antes da posição máxima permitida for encontrada, atribui essa posição à variável 'end'
        if space_before >= 0:
            end = space_before
        # Caso contrário, procura a posição do último espaço após a posição máxima permitida
        else:
            space_after = text.rfind(' ', max_len)
            # Se a posição do último espaço após a posição máxima permitida for encontrada, atribui essa posição à variável 'end'
            if space_after >= 0:
                end = space_after
    # Se a variável 'end' não foi atribuída uma posição, significa que não há espaços no texto para encurtar
    if end is None:  
        # Define a posição final como o comprimento total do texto
        end = len(text)
    # Retorna o texto encurtado até a posição final e remove quaisquer espaços em branco adicionais do final da string
    return text[:end].rstrip()


# _________________________________________________________________________________
# Exemplos de uso da função:

clip('banana ', 6)
#output: 'banana'

clip('banana ', 7)
#output: 'banana'

clip('banana ', 5)
#output: 'banana'

clip('banana split', 6)
#output: 'banana'

clip('banana split', 7)
#output: 'banana'

clip('banana split', 10)
#output: 'banana'

clip('banana split', 11)
#output: 'banana'

clip('banana split', 12)
#output: 'banana split'


# _________________________________________________________________________________
# Acessando algumas informações sobre a própria função:

# 'clip.defaults' retorna uma tupla que contém os valores padrão dos parâmetros da função 'clip'. Nesse caso, o valor padrão para o parâmetro 'max_len' é 80.
clip.__defaults__
#output: (80,)

# 'clip.code' retorna um objeto de código que contém várias informações sobre a função 'clip', incluindo seu bytecode (a sequência de instruções em Python que implementam a função) e outras informações sobre como a função foi definida.
clip.__code__  # doctest: +ELLIPSIS
#output: <code object clip at 0x...>

#'clip.code.co_varnames' retorna uma tupla contendo os nomes de todas as variáveis locais e argumentos posicionais na função 'clip'.
clip.__code__.co_varnames
#output: ('text', 'max_len', 'end', 'space_before', 'space_after')

#'clip.code.co_argcount' retorna o número total de argumentos que a função 'clip' aceita. Nesse caso, a função aceita dois argumentos: 'text' e 'max_len'.
clip.__code__.co_argcount
#output: 2


# _________________________________________________________________________________
# Usando o módulo 'inspect' para obter informações sobre a assinatura da função 'clip':
from inspect import signature

# 'sig = signature(clip)' cria um objeto Signature que representa a assinatura da função 'clip', incluindo o número e o nome de seus parâmetros.
sig = signature(clip)

# 'sig' imprime a assinatura da função 'clip', que mostra o nome da função, seus parâmetros e seus valores padrão, se houver.
sig
#output: <inspect.Signature object at 0x...>

# 'str(sig)' retorna a representação em forma de string da assinatura da função 'clip'.
str(sig)
#output: '(text, max_len=80)'

# O loop 'for name, param in sig.parameters.items():' itera através dos parâmetros da função 'clip' e extrai informações sobre cada um deles.
for name, param in sig.parameters.items():
    #imprime o tipo de cada parâmetro (posicional ou com palavra-chave), seu nome e seu valor padrão, se houver.
    print(param.kind, ':', name, '=', param.default)
    """output:
    POSITIONAL_OR_KEYWORD : text = <class 'inspect._empty'>
    POSITIONAL_OR_KEYWORD : max_len = 80
    """
