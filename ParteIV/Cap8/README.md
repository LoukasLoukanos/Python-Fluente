# Referências a objetos, mutabilidade e reciclagem

## **Pág. 258 à 262............Variáveis não são caixas | Identidade, igualdade e apelidos | Escolhendo entre == e is**
<details>
<summary></summary>

**As variáveis em Python são rótulos ou apelidos (alias) associados a objetos.**</br>
*→ Pense em variáveis como várias etiquetas que rotulam um único objeto, e não como caixas, das quais se pressupõe o encapsulamento de objetos distintos.*</br>
*→ a variável de referência é atribuida a um objeto e não o contrário, pois o objeto é criado antes da atribuição (o lado direito de uma atribuição sempre ocorre antes)*</br>

**Exemplo:**
```python
charles = {'name': 'Charles L. Dodgson', 'born': 1832} # charles é o primeiro rótulo ou apelido (alias) para o objeto
lewis = charles # temos o segundo alias (lewis) para o mesmo objeto

# 'is' compara a identidade (id) dos objetos, enquanto que '==' compara os seus valores
lewis is charles #output: True → identidades iguais
lewis == charles #output: True → valores iguais, equivalentes


id(charles), id(lewis)
#output: (4300473992, 4300473992)

lewis['balance'] = 950 # adicionar um item em lewis é o mesmo que adicionar em charles↓
print(charles)
#output: {'name': 'Charles L. Dodgson', 'balance': 950, 'born': 1832}

alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}

# 'is' compara a identidade (id) dos objetos, enquanto que '==' compara os seus valores
alex == charles #output: True → valores iguais, equivalentes
alex is charles #output: False → identidades diferentes

```

</details>
</br>


## **Pág. 263 à 264............A relativa imutabilidade de tuplas**
<details>
<summary></summary>

**Se os itens referenciados forem mutáveis, eles poderão mudar mesmo que a tupla em si não mude.**
*→ a imutabilidade das tuplas se refere às referências que ela armazena, ou seja, o que nunca muda em uma tupla é a identidade dos itens que ela contém, não necessariamente os ítens:*</br>

**Exemplo:**
```python
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
t1 == t2 #output: True    → valores iguais, equivalentes
t1 is t2 #output: False   → identidades diferentes

id(t1)     #output: 140521738555328
id(t1[-1]) #output: 4302515784

t1[-1].append(99) #mudança: (1, 2, [30, 40, 99]) 
#→ o item mutável list da tupla pode mudar, as referências que a tupla 
#armazena na memória não mudam. Nesse sesntido a tupla continua imutável.

t1 == t2 #output: False   → os valores entre as duas tuplas agora são diferentes
t1 is t2 #output: False   → as identidades das duas tuplas continuam diferentes

id(t1)     #output: 140521738555328  → o id da tupla permanece imutável mesmo após da mudança no seu objeto interna list
id(t1[-1]) #output: 4302515784       →↓      
'''→ o id da lista não mudou porque, sendo mutável, ela permanece como o mesmo objeto na memória após a mudança. 
Diferentemente dos objetos imutáveis, como as tuplas, que criam um novo objeto na memória quando são modificadas 
no escopo principal, i.e., exceto quando a mudança ocorrer em um objeto interno à tupla.'''

```

</details>
</br>


## **Pág. 264 à 267............Cópias são rasas por padrão | Cópias profundas e rasas de objetos quaisquer**
<details>
<summary></summary>

**CONTEXTUALIZAÇÃO:**
 - sequenciaEmbutida = ([], {})
 - escopo exterto: () ← objeto
 - escopos internos: [], {} ← objetos

**→ cópia rasa (shallow copy)** é a cópia apenas das referência dos objetos internos e não dos objetos em si.
Isso significa que, se você tiver um objeto composto (como uma lista que contém outras listas como elementos), 
uma cópia rasa criará uma nova lista, mas apenas copiará as referências para os elementos internos, em vez de 
criar novos objetos para esses elementos. Portanto, as modificações feitas nos elementos internos de uma cópia 
rasa serão refletidas tanto na cópia quanto no objeto original. [CÓPIAS SÃO RASAS POR PADRÃO].</br></br>

**→ cópia profunda (deep copy)** é a cópia de novos objetos para todos os objetos internos, em todos os níveis 
de profundidade. Isso garante que as modificações feitas na cópia não afetem o objeto original e vice-versa.</br></br>

**cópia rasa (shallow copy):**</br>
    ♦ cópia do objeto externo com outro id</br>
    ♦ cópia das referências dos objetos internos (compartilhamento de objetos internos)</br>
    → Problema 1: modificações feitas no escopo externo original da sequência embutida NÃO serão refletidas na cópia</br>
    → Problema 2: modificações feitas em escopos internos (exceto imutáveis) da sequência original SERÃO refletidas na cópia</br>
    → Problema 3: modificações feitas em escopos internos e mutáveis da cópia SERÃO refletidas na sequência embutida original</br>
    → Problema 4: modificações feitas em escopos internos e imutáveis da cópia NÃO serão refletidas na sequência original</br></br>
    
**cópia profunda (deep copy):**</br>
    ♦ cópia do objeto externo com outro id</br>
    ♦ cópia dos objetos internos com outros ids (não o compartilhamento de referências na memória)</br>
    → Solução geral: modificações feitas na cópia não afetem o objeto original e vice-versa</br>

**Exemplo:**
```python
l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1) # a maneira mais fácil de criar uma cópia rasa é usando o contrutor do próprio tipo → list(l1)

l1.append(100)   
#l1: [3, [66, 55, 44], (7, 8, 9), 100]   → Problema 1
#l2: [3, [66, 55, 44], (7, 8, 9)]        → Problema 1

l1[1].remove(55) 
#l1: [3, [66, 44], (7, 8, 9)]   → Problema 2
#l2: [3, [66, 44], (7, 8, 9)]   → Problema 2 

l2[1] += [33, 22]
#l1: [3, [66, 44, 33, 22], (7, 8, 9), 100]   → Problema 3
#l2: [3, [66, 44, 33, 22], (7, 8, 9), 100]   → Problema 3 

l2[2] += (10, 11)
#l2: [3, [66, 44, 33, 22], (7, 8, 9), 100]   → Problema 4
#l2: [3, [66, 44, 33, 22], (7, 8, 9, 10, 11)]   → Problema 4



# Classe para exemplo de de uso de cópia profunda:
class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers) #cópia rasa

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


import copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)     # cópia rasa
bus3 = copy.deepcopy(bus1) # cópia profunda

bus1.drop('Bill') # modifica bus1 → a cópia rasa bus2 recebe a mudaça; a cópia profunda bus3 não.↓

bus1.passengers # ['Alice', 'Claire', 'David']
bus2.passengers # ['Alice', 'Claire', 'David'] → cópia rasa
bus3.passengers # ['Alice', 'Bill', 'Claire', 'David'] → cópia profunda

```

</details>
</br>


## **Pág. 268 à 274............Parâmetros de função como referências | Tipos mutáveis como default de parâmetros: péssima idéia | Programação defensiva con parâmetros mutáveis**
<details>
<summary></summary>

O modo de passagem de parâmetro do Python é pela **chamada por compartilhamento (call by sharing)**:</br>
que quer dizer que cada parâmetro da função obtém uma cópia de cada referência nos argumentos, ou seja, os parâmetros (abstrato → alias) na função tornam-se apelidos dos argumentos (concreto → objeto).</br>

Nisso, uma função pode alterar qualquer objeto mutável (seus valores) passado como argumento, mas não poderá mudar a identidade desses objetos.</br>

*O problema começa ao passar números, listas e túplas para a função, pois os argumentos (concreto → objeto) passados são afetados de modos diferentes ao receberem o tratamento aplicado por seus alias-parâmetros internamente na função:*
```python
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

```
</br>

**Os bugs podem ser preocupantes quanto aos problemas existenes ao usarmos tipos mutáveis como default de parâmetros:**</br>

*↓ Exemplo da péssima ideia de usar o tipo mutável list como default de parâmetro, pois nos deparamos com um atributo do objeto-função, o list default:*
```python
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

```
</br>

*Problemas passando tipos mutáveis como argumento-lista para a mesma função, mas adaptada a qual pode criar cópia rasa:*
```python
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
```

</details>
</br>


## **Pág. 274 à 280............del e coleta de lixo | Referências fracas | Esquete com WeakValueDictionary | Limitações das referências fracas**
<details>
<summary></summary>

### del e coleta de lixo para Alias, Referência Fraca (weakref) e Variável Global

**Alias:**</br>
O comando del apaga nomes(alias), e não objetos diretamente. Ou seja, para que o objeto seja apagado, é necessário que o alias seja o último.</br>
Cada objeto mantém um contador para o número de referências a ele. Assim que refcount atinge zero, o objeto é destruído.</br>
É complicado e quase desnecessário implementar _ _ del _ _, apesar de alguns iniciantes em Python gastarem tempo nisso.</br>
```python
import weakref
s1 = {1, 2, 3}
s2 = s1

def bye():
    print("The bug is on the table")

ender = weakref.finalize(s1, bye)
ender.alive
#output: True

del s1 # deleta a referência(alias) s1 ao objeto '{1, 2, 3}' → restou a refência s2 ao mesmo objeto '{1, 2, 3}', ainda que s1 tenha sido deletada
ender.alive
#output: True

s2 = 'spam' # ao reassociar s2 a outro objeto ('spam'), s2 não é mais alias de '{1, 2, 3}'. Nisso, o objeto '{1, 2, 3}' é extinguido.
#output: The bug is on the table
ender.alive
#output: False

#Portanto, fica claro que del não deleta diretamente objetos, estes porém são deletados indiretamentes por ficarem sem referências (alias) ao usar del para deletá-las.

```

**Referência Fraca (weakref):**
Uma referência fraca é um invocável que devolve o objeto referenciado ou None se o referente não existir.</br>
A presença de referências é o que mantém um objeto vivo na memória.</br>
Uma referência fraca não impede que o objeto referente seja destruido pelo coletor de lixo, caso o alias usado como referência seja deletado.</br>
```python
import weakref
a_set = {0, 1}
wref = weakref.ref(a_set) # referência fraca 'wref' criada
wref #output: <weakref at 0x000002721F51E8E0; to 'set' at 0x000002721F9392A0>
wref() #output: {0, 1}
wref() is None #output: False → wref não é none, é alias fraca de a_set
del a_set # deletando o primeiro alias, suas referências fracas não impedirão a destruição consequente do objeto.
wref() is None #output: True → wref agora é none, pois a referência a_set, foi deletada, deletando por consequência, suas referêcias fracas...

```

**Variável Global:**
Uma Variável Global só desaparecerá ao deletar explicitamente seu alias</br>
```python

"""
SET   : Pode ter referência fraca (pode ser Alvo ou Referente de weakref)
DICT  : Apelas Subclasse pode ter referência fraca (A Subclasse pode ser Alvo ou Referente de weakref)
LIST  : Apelas Subclasse pode ter referência fraca (A Subclasse pode ser Alvo ou Referente de weakref)
TUPLE : Não pode ter referência fraca (NÃO pode ser Alvo ou Referente de weakref)
INT   : Não pode ter referência fraca (NÃO pode ser Alvo ou Referente de weakref)
"""

class Cheese:

    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind

  
import weakref
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog: # o alias cheese do alias catalog, é uma variável global ↓
    stock[cheese.kind] = cheese

sorted(stock.keys()) # chaves de stock[]
#output: ['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']

del catalog # ao deletar o alias catalog, ainda temos a chave ['Parmesan'], de stock[]↓
sorted(stock.keys())
#output: ['Parmesan']

#a variável global cheese só desaparecerá ao deletar explicitamente seu alias↓↓↓
del cheese
sorted(stock.keys())
#output: []

```

</details>
</br>


## **Pág. 280 à 281............Truques de Python com imutáveis**
<details>
<summary></summary>

### Internalização (interning)

**É uma técnica de otimização usada para o compartilhamento de strings e números inteiros para evitar duplicação desnecessária de objetos**
```python
t1 = (1, 2, 3)
t2 = tuple(t1) #alias de t1
t2 is t1
#output: True

t3 = t1[:] #alias de t1
t3 is t1
#output: True

#t1 = (1, 2, 3) ↑...
t4 = (1, 2, 3)
t4 is t1
#output: False

s1 = 'ABC'
s2 = 'ABC' # Internalização (interning) ...↓
s2 is s1
#output: True → Surpresa!!! Porém Python não internaliza todas as strings ou todos os inteiros, os critérios que ele para isso são detalhes de implementação não documentados.

```

</details>
