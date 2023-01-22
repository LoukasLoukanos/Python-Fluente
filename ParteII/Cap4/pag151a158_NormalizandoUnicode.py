# Normalizando Unicode para comparações mais seguras:

from unicodedata import normalize
'''
 O primeiro argumento de normalize suporta quatro trings: 
    'NFC' → compõe de modo equivalente... Gera a menor string equivalente aos códigos Unicode
    'NFD' → decompõe de modo equivalente... Expande os caracteres compostos em caracteres básicos, separando os caracteres combinados
    'NFKC' → compõe de modo compatível ... A letra k representa 'compatibility' (compatibilidade), portanto não promete equivalência
    'NFKD' → decompõe de modo compatível... A letra k representa 'compatibility' (compatibilidade), portanto não promete equivalência
 obs: normalize não formata (NORMALIZA), portanto NFKC e NFKD podem distorcer informações.
'''

# exemplos________________________________________________________________________________________________

# Usando (NFC) → "Compõe de modo equivalente":
cof = 'cafe\u0301'
cof = normalize('NFC', cof)
    # output: café

# Usando (NFD) → "Decompõe de modo equivalente":
cof = normalize('NFD', cof)
    # output: cafe\u0301


# Usando (NFKC) → "Compõe de modo compatível"
half = '⅛'
half = normalize('NFKC', half)
    #output: 1/2 → a função normalize não sabe nada sobre formatação, por isso essa saída

# Usando (NFKD) → "Decompõe de modo compatível"
half = normalize('NFKD', half)
    #output: ⅛ → a função normalize não sabe nada sobre formatação, por isso essa saída



# exemplos com funções______________________________________________________________________________________
def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)

def fold_equal(str1, str2):
    # casefold() faz a conversão do texto em letras minúsculas, com algumas transformações adicionais.
    return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold())


# Usando (NFC) → "Compõe":_________________________________
s1 = 'café'
s2 = 'cafe\u0301'
s1 == s2 #output: False

nfc_equal(s1, s2) #output: True → (pois (s1=café) == (s2 composto por NFC))

nfc_equal('A', 'a') #output: False → (não há o que gerar de nova string equivalente, pois 'a' não é a composição de 'A', ou vice-versa, em Unicode)


# Usando (NFC) → "Compõe":_________________________________
s3 = 'Straße'
s4 = 'strasse'
s3 == s4 #output: False

nfc_equal(s3, s4) #output: False → (não há o que gerar de nova string equivalente, pois 'ß' não é a composição de 'ss(minúsculo)', ou vice-versa, em Unicode)

fold_equal(s3, s4) #output: True → (pois casefold() faz a conversão do texto em letras minúsculas, com algumas transformações adicionais – nesse caso 'ß' virou 'ss' –)

fold_equal(s1, s2) #output: True 

fold_equal('A', 'a') #output: True → (pois casefold() converteu 'A' em 'a')
