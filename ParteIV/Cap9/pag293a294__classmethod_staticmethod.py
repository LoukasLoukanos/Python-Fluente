
"""
Ambos `@classmethod` e `@staticmethod` são decoradores em Python usados para definir métodos que pertencem à classe, em vez de pertencer a instâncias individuais da classe. No entanto, eles têm propósitos ligeiramente diferentes:</br></br>

Em resumo, `@classmethod` é usado quando você precisa de acesso aos atributos de classe, enquanto `@staticmethod` é usado quando você precisa de um método independente da instância ou da classe.

1. `@classmethod`:
   - Um método de classe recebe a classe como o primeiro argumento (por convenção chamado de `cls`).
   - Ele pode acessar e modificar os atributos de classe, mas não pode acessar os atributos da instância diretamente.
   - Geralmente usado quando o método precisa acessar ou modificar atributos de classe específicos.

2. `@staticmethod`:
   - Um método estático não recebe automaticamente nenhum argumento especial (nem a instância nem a classe).
   - Ele não pode acessar ou modificar os atributos da classe ou da instância.
   - É usado quando o método não precisa de acesso a atributos de classe ou de instância e pode ser definido de forma independente da classe.
"""

class Demo:
    @classmethod
    def klassmeth(*args): # por convenção poderiamos usar `cls` no lugar de `*args` (*args, porém, possibilita usar qualquer número de argumentos posicionais)
        return args # retorna todos os argumentos posicionais `args` (inclui a classe enviada como parâmetro através do decorador @classmethod)

    @staticmethod
    def statmeth(*args):
        return args # também retorna todos os argumentos posicionais `args` (porém comportando-se como função simples)


Demo.klassmeth()
#output: (<class '__main__.Demo'>,)
Demo.klassmeth('spam')
#output: (<class '__main__.Demo'>, 'spam')

Demo.statmeth()
#output: ()
Demo.statmeth('spam')
#output: ('spam')


#"Portanto, `@classmethod` é muito útil, entretanto, `@staticmethod`, não muito" – Luciano Ramalho.
