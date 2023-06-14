## **Decoradores (decorators) de função e closures**
Um decorador é basicamente uma função (função decoradora) que recebe outra função como parâmetro (chamada de função decorada) que, por sua vez, poderá ser modificada por uma terceira função (uma subfunção da decoradora). Decoradores de função em python permitem "marcar" funções modificando o seu comportamento.

### ***Exemplo simples da sintaxe: ***
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
