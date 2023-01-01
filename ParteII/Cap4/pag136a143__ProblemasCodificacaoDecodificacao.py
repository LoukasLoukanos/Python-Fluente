city = 'São Paulo'

city.encode('utf_8') # a codificação não acarreta em erro
city.encode('utf_16') # a codificação não acarreta em erro
city.encode('iso8859_1') # a codificação não acarreta em erro

city.encode('cp437')
'''a codificação acarreta em erro no caractere 'ã':
output:
    ...line 12, in encode return codecs.charmap_encode(input,errors,encoding_map) UnicodeEncodeError: 
    'charmap' codec can't encode character '\xe3' in position 1: character maps to <undefined>...
'''

#tratando erros_________________________________________
city.encode('cp437', errors='ignore') # errors='ignore' → ignora os erros ('ã', nesse caso)
# output: b'So Paulo'

city.encode('cp437', errors='replace') # errors='replace' → substitui os erros por '?'
# output: b'S?o Paulo'

city.encode('cp437', errors='xmlcharrefreplace') # errors='xmlcharrefreplace' → substitui os erros por entidades xml correspondentes
# output: b'S&#227;o Paulo'
