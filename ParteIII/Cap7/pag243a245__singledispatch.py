# Depurando aplicações web: gerando visualizações em HTML para diferentes tipos de objetos

'''
Não temos sobrecarga de método nem de função em Python, não podendo criar variações de funções com assinaturas diferentes.
→ Uma solução para isso seria utilizar uma função de despacho (dispatch), com uma cadeia de if/elif/elif para cada ocasião.
→ O decorador functools.singledispatch permite tornar funções e classes genéricas para realizar uma "sobrecarga de método".

Na verdade, singledispatch não foi concebido para replicar a sobrecarga de métodos no estilo Java em Python. Em vez disso, 
singledispatch foi projetado para facilitar a extensão modular de funcionalidades em Python. Com singledispatch, cada módulo 
pode registrar uma função especializada para lidar com um tipo específico de argumento, permitindo uma abordagem modular e 
flexível para estender o comportamento de funções em toda a aplicação. Isso significa que diferentes partes do código podem 
fornecer implementações especializadas para tipos específicos, promovendo a reusabilidade do código e mantendo uma estrutura 
modular e organizada.

Quando você decora uma função com @singledispatch e, em seguida, registra funções especializadas para tipos específicos com 
@funcao.register(tipo), você está dizendo que, para cada tipo registrado, uma função específica deve ser usada para lidar com 
esse tipo. Isso permite que você estenda o comportamento de uma função para novos tipos sem modificar sua implementação original.
'''
from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch  # singledispatch marca a função base que trata o tipo object
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)  # cada função especializada é decorada com @funcao_base.register(tipo)
def _(text):            #  o nome das funções especializadas é irrelevante; _ é uma boa opção para deixar isso claro
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)  # Para cada tipo adicional que vá receber um tratamento especial, registre uma nova funçlão. 'numbers.Integral' é uma superclasse virtual de inteiro
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)  # você pode empilhar diversos decoradores register para dar suporte a tipos diferentes com a mesma função
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


htmlize({1, 2, 3})  # por padrão a repr de um objeto com escape HTML é mostrada entre <pre></pre>
                    # output: '<pre>{1, 2, 3}</pre>'

htmlize(abs) # por padrão a repr de um objeto com escape HTML é mostrada entre <pre></pre>
             # output: '<pre>&lt;built-in function abs&gt;</pre>'

htmlize('Heimlich & Co.\n- a game')  # objetos string também têm escape HTML, mas são colocados entre <p></p> com quebras de linhas <br>
                                     # output: '<p>Heimlich &amp; Co.<br>\n- a game</p>'

htmlize(42)  # um int é mostrado em decimal e hexadecimal entre <pre></pre>
             # output: '<pre>42 (0x2a)</pre>'

print(htmlize(['alpha', 66, {3, 2, 1}]))  # cada item da lista é formado segundo o seu tipo e a sequência toda é representada como uma lista HTML
                                          '''output:
                                          <ul>
                                            <li><p>alpha</p></li>
                                            <li><pre>66 (0x42)</pre></li>
                                            <li><pre>{1, 2, 3}</pre></li>
                                          </ul>
                                          '''

