''' ANOTAÇÕES DE FUNÇÃO: 
  As anotações de função em Python são utilizadas para especificar o tipo de dado esperado para cada parâmetro da função, bem como 
  o tipo de dado que é retornado pela função. Ou seja, anotações ajudam a documentar o tipo de entrada e saída esperado pela função 
  de maneira semelhante à assinatura de métodos em Java. As anotações de função em Python são opcionais e não afetam o comportamento 
  da função em si, a única coisa que python faz com as anotações, é armazená-las no atributo __annotations__, que é um dict.

As anotações de função são especificadas colocando o nome do parâmetro seguido de dois pontos e, em seguida, o tipo esperado. 
Por exemplo, uma função que recebe dois números inteiros e retorna outro número inteiro pode ser escrita da seguinte forma:
'''
def soma(a: int, b: int) -> int:
    # → anotação a: int indica que o primeiro parâmetro da função soma deve ser um inteiro
    # → anotação b: int indica que o segundo parâmetro também deve ser um inteiro
    # → anotação -> int indica que a função retorna um inteiro.
    return a + b

print(soma.__annotations__)
# output: {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}



def clip(text:str, max_len:'int > 0'=80) -> str:  # Função clip do exemplo pag188a190_InformacoesDeParametros.py declarada com anotações
   
    # Encurta um texto para um comprimento máximo especificado...
    
    end = None

    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()

print(clip.__annotations__)
# output: {'text': <class 'str'>, 'max_len': 'int > 0', 'return': <class 'str'>}

# podemos usar signature para inspecionar melhor
from inspect import signature
sig = signature(clip)
print(sig.return_annotation) # return_annotation é um atributo do objeto Signature 'sig' que mostra o tipo da anotação de retorno
#output: <class 'str'>

for param in sig.parameters.values(): # parameters é um dicionario do objeto Signature 'sig'
    note = repr(param.annotation).ljust(13)
    print(note, ':', param.name, '=', param.default)
    '''output:    
    <class 'str'> : text = <class 'inspect._empty'>
    'int > 0'     : max_len = 80
    '''
