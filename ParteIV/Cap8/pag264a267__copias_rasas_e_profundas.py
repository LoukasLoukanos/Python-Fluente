'''
CONTEXTUALIZAÇÃO:
sequenciaEmbutida = ([], {})
escopo exterto: () ← objeto
escopos internos: [], {} ← objetos

→ cópia rasa (shallow copy) é a cópia apenas das referência dos objetos internos e não dos objetos em si.
Isso significa que, se você tiver um objeto composto (como uma lista que contém outras listas como elementos), 
uma cópia rasa criará uma nova lista, mas apenas copiará as referências para os elementos internos, em vez de 
criar novos objetos para esses elementos. Portanto, as modificações feitas nos elementos internos de uma cópia 
rasa serão refletidas tanto na cópia quanto no objeto original. [CÓPIAS SÃO RASAS POR PADRÃO].

→ cópia profunda (deep copy) é a cópia de novos objetos para todos os objetos internos, em todos os níveis 
de profundidade. Isso garante que as modificações feitas na cópia não afetem o objeto original e vice-versa.

rasa (shallow copy):
    ♦ cópia do objeto externo com outro id
    ♦ cópia das referências dos objetos internos (compartilhamento de objetos internos)
    → Problema 1: modificações feitas no escopo externo original da sequência embutida NÃO serão refletidas na cópia
    → Problema 2: modificações feitas em escopos internos (exceto imutáveis) da sequência original SERÃO refletidas na cópia
    → Problema 3: modificações feitas em escopos internos e mutáveis da cópia SERÃO refletidas na sequência embutida original
    → Problema 4: modificações feitas em escopos internos e imutáveis da cópia NÃO serão refletidas na sequência original
    
cópia profunda (deep copy):
    ♦ cópia do objeto externo com outro id
    ♦ cópia dos objetos internos com outros ids (não o compartilhamento de referências na memória)
    → Solução geral: modificações feitas na cópia não afetem o objeto original e vice-versa
'''

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
