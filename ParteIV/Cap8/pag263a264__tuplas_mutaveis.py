'''
Se os itens referenciados forem mutáveis, eles poderão mudar mesmo que a tupla em si não mude.
→ a imutabilidade das tuplas se refere às referências que ela armazena, ou seja, o que nunca  
  muda em uma tupla é a identidade dos itens que ela contém, não necessariamente os ítens:
'''

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
