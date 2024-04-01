'''
O modo de passagem de parâmetro do Python é pela chamada por compartilhamento (call by sharing):
que quer dizer que cada parâmetro da função obtém uma cópia de cada referência nos argumentos,
ou seja, os parâmetros (abstrato → alias) na função tornam-se apelidos dos argumentos (concreto → objeto). 

Nisso, uma função pode alterar qualquer objeto mutável (seus valores) passado como argumento, 
mas não poderá mudar a identidade desses objetos. 
'''


# O problema começa ao passar números, listas e túplas para a função, pois os argumentos (concreto → objeto) passados 
# são afetados de modos diferentes ao receberem o tratamento aplicado por seus alias-parâmetros internamente na função:
def f(a, b): # os parâmetros 'a', 'b' são alias tratados localmente pela função para os argumentos que serão os objetos passados a ela
    a += b
    return a

x = 1
y = 2
f(x, y)
#retorno: 3 (alias a para o argumento x)
print(x, y)
#output: 1, 2 → 'x': tipo mutável; comportamento na função: imutável
#Conclusão: os parâtros tratados na função NÃO afetam o argumento

a = [1, 2]
b = [3, 4]
f(a, b)
#retorno: [1, 2, 3, 4]
print(a, b)
#output: [1, 2, 3, 4], [3, 4] → 'a': tipo mutável; comportamento na função: mutável 
#Conclusão: os parâtros tratados na função AFETAM o argumento

t = (10, 20)
u = (30, 40)
f(t, u)
#retorno: (10, 20, 30, 40)
print(t, u)
#output: (10, 20) (30, 40) → 't': tipo imutável; comportamento na função: imutável
#Conclusão: os parâtros tratados na função AFETAM o argumento


'''
Os bugs podem ser preocupantes quanto aos problemas existenes ao usarmos tipos mutáveis como default de parâmetros:

↓ Exemplo da péssima ideia de usar o tipo mutável list como default de parâmetro, 
  pois nos deparamos com um atributo do objeto-função, o list default:
'''
class HauntedBus:
    
    def __init__(self, passengers=[]): 
        ''' passagers→alias1; []→objeto. Esse é o argumento default criado diretamente, caso não seja 
        enviado argumento na chamada. A list default é um atributo do objeto-função que será afetada 
        caso tentemos criar outras listas default em futuras chamadas, pois apenas a primeira lista será 
        criada como atributo do objeto-função, recebendo mudanças no tratamento dessas futuras chamas.
        '''
        
        self.passengers = passengers  # passagers→alias2; self.passagers→alias3. Estamos tratando o parâmetro alias2 criado
 
    def pick(self, name):
        self.passengers.append(name)  
        # caso o arguemento seja default, estaremos mudando a list default, que é um atributo do objeto-função 
        # quer dizer, que se tentarmos criar outras listas default, estaremos submettidos à mudando da primeira lista apenas.

    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus(['Alice', 'Bill']) # não usamos list default como argumento
bus1.passengers #output: ['Alice', 'Bill']

bus1.pick('Charlie')
bus1.drop('Alice')
bus1.passengers #output: ['Bill', 'Charlie']

bus2 = HauntedBus()
bus2.pick('Carrie')
bus2.passengers #output: ['Carrie']

bus3 = HauntedBus()
bus3.passengers #output: ['Carrie']

bus3.pick('Dave')
bus2.passengers #output: ['Carrie', 'Dave']

bus2.passengers is bus3.passengers 
#output: True → O problema, pois bus2.passengers e bus3.passengers referenciam a mesma lista, a lista atributo do objeto-função, a list default...

bus1.passengers #output: ['Bill', 'Charlie'] → não foi afetado pois não bus1 não foi criado com list default


# Vamos inspecionar para uma prova induptável:
dir(HauntedBus.__init__)  # doctest: +ELLIPSIS
#output: ['__annotations__', '__call__', ..., '__defaults__', ...] → temos aqui o método especial __defaults__

# apenas os atributos defaults do objeto-função nos interessam:
HauntedBus.__init__.__defaults__
#output: (['Carrie', 'Dave'],) → aqui está a list default do objeto-função HuntedBus

HauntedBus.__init__.__defaults__[0] is bus2.passengers
#output: True → podemos concluir que bus2.passengers é um apelido associado ao primeiro elemento do atributo HauntedBus.__init__.__defaults__



#Problemas passando tipos mutáveis como argumento-lista para a mesma função, mas adaptada a qual pode criar cópia rasa:
class TwilightBus:

    def __init__(self, passengers=None, shallow_copy=False):
        if passengers is None: # quando não passamos argumento-lista para a função
            self.passengers = []  
       
        else: # quando passamos argumento-lista
            if shallow_copy == False: # por padrão(default), não cria uma cópia rasa, apenas um alias↓
                self.passengers = passengers  # Caso passememos a lista-argumento para a função, passagers é o alias2 usado para parâmetro; self.passagers, o alias3, e o argumento list passado é o alias1 do objeto list
                
            else: # se passamos o argumento shallow_copy==True → nesse caso cria uma cópia rasa
                self.passengers = list(passengers)
        
    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


#Caso sem gerar cópia rasa
basketball_team_A = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus1 = TwilightBus(basketball_team_A) #passando a lista como argumento para a função com shallow_copy=False padrão
bus1.drop('Tina')
bus1.drop('Pat')
basketball_team_A #output: ['Sue', 'Maya', 'Diana'] → afetou a lista original 
# → Problema: Sem criar cópia rasa na função para tratar o parâmetro, estamos alterando a lista original recebida como argumento 

#Caso gerando cópia rasa:
basketball_team_B = ['Luna', 'Tami', 'Julya', 'Let']
bus1 = TwilightBus(basketball_team_B, True) #passando a lista como argumento para a função com shallow_copy=True
bus1.drop('Tami')
bus1.drop('Let')
basketball_team_B #output: ['Luna', 'Tami', 'Julya', 'Let'] → não afetou a lista original
# → Solucição: Ao criar cópia rasa na função para tratar o parâmetro, estamos alterando a lista cópia rasa criada, não a original recebida como argumento