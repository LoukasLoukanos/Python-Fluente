
'''
♦ PARÂMETROS POSICIONAIS → são argumentos de uma função que são passados na ordem em que foram definidos na assinatura da função. Esses argumentos são obrigatórios.
♦ OPERADOR * → Permite que argumentos adicionais sejam passados para uma função como PARÂMETROS POSICIONAIS. É usado para coletar um número variável de argumentos em uma tupla.

♦ PARÂMETROS NOMEADOS → são argumentos de uma função que são passados explicitamente pelo nome →"agr=nome". Esses argumentos são opcionais e podem ser omitidos.
♦ OPERADOR ** → Permite que argumentos adicionais sejam passados para uma função como PARÂMETROS NOMEADOS. É usado para coletar um número variável de argumentos em um dicionário.
'''

def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)
    

# Um único argumento posicional produz uma tag vazia com esse nome:
tag('br')  # PARÂMETRO POSICIONAL
#output: '<br />'

# Qualquer quantidade de argumentos após o primeiro é capturada por *content como uma tuple:
tag('p', 'hello') # OPERADOR * em *content para PARÂMETRO POSICIONAL
#output: '<p>hello</p>'

tag('p', 'hello', 'world') # OPERADOR * em *content para PARÂMETROS POSICIONAIS
'''output: <p>hello</p>
           <p>world</p>
'''

# Argumentos nomeados não explicitamente nomeados na assinatura de tag são capturados por **attrs como um dict:
tag('p', 'hello', id=33)  # OPERADOR * em **attrs para PARÂMETRO NOMEADO
#output: '<p id="33">hello</p>'

# O parámetro cls pode ser passado somente como um argumento nomeado:
tag('p', 'hello', 'world', cls='sidebar') # PARÂMETROS POSICIONAIS e PARÂMETRO NOMEADO
'''output: <p class="sidebar">hello</p>
           <p class="sidebar">world</p>
'''

# Mesmo o primeiro argumento posicional pode ser passado como um argumento nomeado quando tag é chamada.
tag(content='testing', name="img")  # PARÂMETROS POSICIONAIS (ao passar o PARÂMETRO NOMEADO 'name' como segundo argumento, devemos passa-lo como NOMEADO)
#output: '<img content="testing" />'

# Passar um dict como argumento com ** faz todos os seus itens serem passados como argumentos separados, que são então associados aos PARÂMETROS NOMEADOS, com o restante capturado por **attrs:
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
tag(**my_tag) 
#output: '<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'
