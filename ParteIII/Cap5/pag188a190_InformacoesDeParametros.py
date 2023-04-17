'''
ACESSO À INFORMAÇÕES DE OBJETOS E PARÂMETROS DE FUNÇÕES (INTROSPECÇÃO)

Introspecção é a capacidade de uma linguagem como Python de examinar seu próprio código e as informações associadas a ele em tempo de execução.
O módulo ♦inspect, nativo do Python, é útil para depurar código e obter informações sobre como os objetos Python estão sendo usados em tempo de 
execução, pois permite obter informações detalhadas sobre um objeto Python, como suas propriedades, métodos e docstrings, podendo ser útil para 
obter a lista de métodos e atributos de uma classe ou, até mesmo, para verificar se uma função é assíncrona. Ou seja, o módulo ♦inspect é uma 
ferramenta poderosíssima e avançada de Introspecção, nativa do python e para o python.
O modelo de dados de Python, com a ajuda do módulo ♦inspect, expõe o mesmo mecanismo usado pelo interpretador para associar argumentos a parâmetros 
formais em chamadas de função. Frameworks e ferramentas como IDEs podem usar essas informações para validar códigos. Outro recurso de Python 3, as 
anotações de função, expandem os possíveis usos disso.

Alguns dos métodos disponíveis no módulo ♦inspect (existem muitos outros métodos úteis de inspect para realizar operações de introspecção em objetos Python):
•getmembers(obj[, predicate]): retorna uma lista de tuplas que representam os membros de um objeto, incluindo métodos, atributos e outros membros.
•signature(obj): retorna a assinatura de uma função, método ou callable como um objeto Signature.
•isfunction(obj): retorna True se o objeto passado for uma função, ou False caso contrário.
•ismethod(obj): retorna True se o objeto passado for um método, ou False caso contrário.
•isclass(obj): retorna True se o objeto passado for uma classe, ou False caso contrário.
•isgenerator(obj): retorna True se o objeto passado for um generator, ou False caso contrário.
•isasyncgen(obj): retorna True se o objeto passado for um async generator, ou False caso contrário.
•isroutine(obj): retorna True se o objeto passado for uma função, método ou callable, ou False caso contrário.
•getsource(obj): retorna o código-fonte de um objeto, como uma string.
•getfile(obj): retorna o nome do arquivo em que um objeto foi definido.
•getmodule(obj[, _filename]): retorna o módulo em que um objeto foi definido.
•getmembers(module[, predicate]): retorna uma lista de tuplas que representam os membros de um módulo, incluindo funções, classes e outros membros.
•getdoc(obj): retorna a documentação de um objeto, como uma string.
'''


# _________________________________________________________________________________
def clip(text, max_len=80):
    '''
    Exempo de função para ser usada com o módulo ♦inspect:
    Encurta um texto para um comprimento máximo especificado. Se o texto fornecido for mais longo do que o comprimento máximo 
    especificado, a função encontra o último espaço antes ou depois da posição máxima permitida e encurta o texto até esse ponto. 
    Se não houver espaços no texto, a função simplesmente encurta o texto para o comprimento máximo permitido.
    '''
    end = None # Inicializa a variável 'end' como 'None'
    
    if len(text) > max_len: # Verifica se o comprimento do texto é maior do que o comprimento máximo permitido
        space_before = text.rfind(' ', 0, max_len) # Procura a posição do último espaço no texto antes da posição máxima permitida
        if space_before >= 0: # Se a posição do último espaço antes da posição máxima permitida for encontrada, atribui essa posição à variável 'end'
            end = space_before
        else: # Caso contrário, procura a posição do último espaço após a posição máxima permitida
            space_after = text.rfind(' ', max_len)
            if space_after >= 0: # Se a posição do último espaço após a posição máxima permitida for encontrada, atribui essa posição à variável 'end'
                end = space_after
    if end is None: # Se a variável 'end' não foi atribuída uma posição, significa que não há espaços no texto para encurtar
        end = len(text) # Define a posição final como o comprimento total do texto
    return text[:end].rstrip() # Retorna o texto encurtado até a posição final e remove quaisquer espaços em branco adicionais do final da string
   
   
# Exemplos de uso apenas da função:
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
# ACESSANDO INFORMAÇÕES DA FUNÇÃO clip() (INTROSPECÇÃO), MAS SEM O USO DE ♦inspect:

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


# _________________________________________________________________________________________________________
# ACESSANDO INFORMAÇÕES DA FUNÇÃO clip() (INTROSPECÇÃO), COM O USO DA FUNÇÃO •signature do MÓDULO ♦inspect:
'''
Algumas das funções que podem ser usadas com o objeto Signature:
→ parameters: retorna uma lista com os objetos Parameter do objeto Signature, que contêm informações sobre cada um dos parâmetros da função.
→ bind: permite ligar os argumentos passados para a função aos parâmetros da assinatura da função. Essa função pode levantar exceções se houver erros de ligação.
→ bind_partial: semelhante à função bind(), mas permite ligar apenas alguns dos argumentos da função aos parâmetros da assinatura. Os argumentos não passados serão substituídos pelos seus valores padrão.
→ return_annotation: retorna a anotação de retorno da função, se houver.
'''
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

    
# ______________________________________________________________________________________________________________________________________________________
# ACESSANDO INFORMAÇÕES DA FUNÇÃO tag() (INTROSPECÇÃO) do módulo pag186e187_ArgsPosicionaisNomeados, COM O USO DA FUNÇÃO •signature do MÓDULO ♦inspect:
import pag186e187_ArgsPosicionaisNomeados
import inspect

sig = inspect.signature(pag186e187_ArgsPosicionaisNomeados.tag) # Obtém a assinatura da função tag do exemplo

my_tag = {'name': 'ing', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'Framed'}
bound_args = sig.bind(**my_tag) # Passa um dict com os argumentos para .bind()

bound_args # Um objeto inspect.BoundArguments é produzido ↓
#output: <inspect.BoundArguments object at 0x..>

# Faz uma iteração pelos itens em bound_args.arguments, que é um OrderedDict, para exibir os nomes e os valores dos argumentos ↓ 
for name, value in bound_args.arguments.items():
    print(name, '=', value)
    '''output:
    name = img
    cls = framed
    attrs = {'title': 'Sunset Boulevard', 'src': 'sunset.jpg"}
    '''

del my_tag['name'] # Remove o argumento obrigatório name de my_tag.

bound_args = sig.bind(**my_tag) # Chamar sig.bind(**my_tag) gera um TypeError que reclama do parâmetro name ausente.
'''output:
Traceback (most recent call last):
TypeError: 'name' paraneter lacking default value
'''
