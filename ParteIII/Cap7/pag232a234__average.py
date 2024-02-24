
'''
Para resumir: uma closure é uma função que preserva as associações com as variáveis livres existentes quando a função é definida, 
de modo que elas possam ser usadas posteriormente quando a função for chamada e o escopo de definição não estiver mais disponível.

→ Note que a única situação em que uma função pode precisar lidar com variáveis 
  externas que não sejam globais é quando ela está aninhada em outra função
'''


# Um exemplo sem Closure ____________________________________________

class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

# a classe Avarager cria instâncias que são invocáveis → _ _call_ _

avg = Averager()
avg(10)
# output: 10.0 → sem média

avg(11)
# output: 10.5 → média entre 10 e 11

avg(12)
# output: 11.0 → média entre 10 e 12



# Um exemplo de Closure ____________________________________________

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager

# a função make_averager devolve um objeto função averager → return


'''
'series' é uma variável livre (free variable) → termo técnico: indica que uma variável não tem uma associação no escopo local

A inspeção do objeto averager devolvido mostra como python mantém os nomes das variáveis
locais e livres no atributo _ _code_ _, que representa o corpo compilado da função
'''

avg2 = make_averager() # Criando uma instância da função make_averager


# Acessando variáveis locais da função interna (averager)
local_variables = avg2.__code__.co_varnames
print(local_variables)  # ('new_value', 'total')

# Acessando variáveis livres (free variables)
free_variables = avg2.__code__.co_freevars
print(free_variables)  # ('series',)

# Acessando o conteúdo das células (closure)
closure_contents = avg2.__closure__[0].cell_contents
print(closure_contents)  # []


avg2(10)
# output: 10.0 → sem média

avg2(11)
# output: 10.5 → média entre 10 e 11

avg2(12)
# output: 11.0 → média entre 10 e 12

# Acessando novamente o conteúdo das células após a modificação da closure
closure_contents_after_append = avg2.__closure__[0].cell_contents
print(closure_contents_after_append)  # [10, 11, 12]


'''
Se executar avg2.__closure__, obterá um objeto que representa as células de closure associadas à função avg2. 
O retorno é algo semelhante a (<cell at 0x107a44f78: list object at 0x107a91a48>,). 
Isso significa que há uma célula na closure, e essa célula está referenciando um objeto do tipo lista.

Para entender mais sobre o conteúdo específico dessa célula, podemos acessar o conteúdo da célula usando 
avg2.__closure__[0].cell_contents. Nesse caso, o conteúdo da célula seria o objeto da lista que a função 
está "lembrando". Se você adicionou valores à lista através da função avg2, o conteúdo da célula refletirá 
essas alterações.
'''


