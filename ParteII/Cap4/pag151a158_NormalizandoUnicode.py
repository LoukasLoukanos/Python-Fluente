# Normalizando Unicode para comparações mais seguras:

from unicodedata import normalize
# O primeiro argumento de normalize suporta quatro trings: 
# 'NFC' → compõe os códigos Unicode de modo a gerar a menor string equivalente
# 'NFD' → decompõe expandindo os caracteres compostos em caracteres básicos, e separa os caracteres combinados
# 'NFKC' → a letra k representa 'compatibility' (compatibilidade)
# 'NFKD' → a letra k representa 'compatibility' (compatibilidade)

def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)

def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold()) # casefold() não leva em conta as diferenças entre as letras minúsculas e maiúsculas (case-insensitive)


# Usando (NFC), com case-sensitive :

s1 = 'café'
s2 = 'cafe\u0301'
s1 == s2
    #output: False
nfc_equal(s1, s2)
    #output: True → pois (s1=cafe) == (s2)
nfc_equal('A', 'a')
    #output: False → (não há o que gerar de nova string equivalente, pois 'a' não é a composição de 'A', ou vice-versa, em Unicode)

# Usando (NFC) com case-insensitive:

s3 = 'Straße'
s4 = 'strasse'
s3 == s4
    #output: False
nfc_equal(s3, s4)
    #output: False → (não há o que gerar de nova string equivalente, pois 'ß' não é a composição de 'ss(minúsculo)', ou vice-versa, em Unicode)

fold_equal(s3, s4)
    #output: True → pois (casefold() não leva em conta as diferenças entre as letras minúsculas e maiúsculas (case-insensitive))
fold_equal(s1, s2)
    #output: True
fold_equal('A', 'a')
    #output: True