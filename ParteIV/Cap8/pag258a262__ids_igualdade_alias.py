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
