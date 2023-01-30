#Normalizando Unicode: comparações mais seguras_______________________________________________________________________________________________________________________________________

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




#Normalização Extrema: removendo acentos_______________________________________________________________________________________________________________________________________
import unicodedata
import string

#_________________________________________________________________________________
#FUNÇÃO PARA REMOVER TODAS AS MARCAS COMBINADAS
def shave_marks(txt):
    """Remove todas as marcas de diacríticos(acentos, cedolhas, etc)"""
    norm_txt = unicodedata.normalize('NFD', txt)  # Usando (NFD) → "Decompõe de modo equivalente"
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))  # filtra todas as marcas combinadas
    return unicodedata.normalize('NFC', shaved)  # Usando (NFC) → "Compõe de modo equivalente"
#_________________________________________________________________________________



#_________________________________________________________________________________
#FUNÇÃO PARA REMOVER MARCAS COMBINADAS DE CARACTERES LATINOS
def shave_marks_latin(txt):
    """Remove todas as marcas de diacríticos(acentos, cedolhas, etc) dos caracteres-base latinos"""
    norm_txt = unicodedata.normalize('NFD', txt)  # Usando (NFD) → "Decompõe de modo equivalente"
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base: # pula as marcas combinadas quando o caractere for latino
            continue  # ignora diacríticos(acentos, cedolhas, etc) em caracteres-base latinos
        keepers.append(c) # caso contrário mantém o caractere atual
        # se não é um caractere combinado, é um novo caractere base
        if not unicodedata.combining(c): # declara o novo caractere-base e determina se é latino
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved) # recompõe todos os caracteres
#_________________________________________________________________________________



#_________________________________________________________________________________
#FUNÇÃO PARA TRANSFORMAR ALGUNS SÍMBOLOS TIPOGRÁFICOS OCIDENTAIS EM ASCII 
single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""",  # Cria tabela de mapeamento para substituição de caractere para caractere.
                           """'f"*^<''""---~>""")

multi_map = str.maketrans({  # Cria tabela de mapeamento para substituição de caractere para string
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})

multi_map.update(single_map)  # Combina as tabelas de mapeamento.


def dewinize(txt):
    """Replace Win1252 symbols with ASCII chars or sequences"""
    return txt.translate(multi_map)  # dewinize não afeta texto ASCII ou latin1, somente os acréscimos da Microsoft ao latini em cp1252.


def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))     # Aplica dewintze e remove marcas de diacríticos. 
    no_marks = no_marks.replace('ß', 'ss')          # Substitui Eszett por "ss" (não estamos usando case fold nesse caso, pois queremos preservar a diferença entre letras maiúsculas e minúsculas).
    return unicodedata.normalize('NFKC', no_marks)  # Aplica a normalização NFKC para compor caracteres com seus códigos de compatibilidade Unicode.
#_________________________________________________________________________________



# Exemplos: Manipulando uma string com simbolos em `cp1252`:________________________
order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'

shave_marks(order)
#output: '“Herr Voß: • ½ cup of Œtker™ caffe latte • bowl of acai.”'

shave_marks_latin(order)
#output: '“Herr Voß: • ½ cup of Œtker™ caffe latte • bowl of acai.”'

dewinize(order)
#output: '"Herr Voß: - ½ cup of OEtker(TM) caffè latte - bowl of açaí."'

asciize(order)
#output: '"Herr Voss: - 1⁄2 cup of OEtker(TM) caffe latte - bowl of acai."'



# Exemplos: Manipulando uma string com caracteres acentuados gregos e latinos:_________
greek = 'Ζέφυρος, Zéfiro'

shave_marks(greek)
#output: 'Ζεφυρος, Zefiro'

shave_marks_latin(greek)
#output: 'Ζέφυρος, Zefiro'

dewinize(greek)
#output: 'Ζέφυρος, Zéfiro'

asciize(greek)
#output: 'Ζέφυρος, Zefiro'
