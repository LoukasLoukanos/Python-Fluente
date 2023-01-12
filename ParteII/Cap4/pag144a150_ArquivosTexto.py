import os
print(os.stat('cafe.txt').st_size) # os.stat devolve a informação de que o arquivo contém 5 bytes; UTF-8 codifica 'e' com 2 bytes: 0xc3 e Oxa9.
#output: 5



fp = open('cafe.txt', 'w', encoding='utf-8') # Por padrão, open opera em modo texto e devolve um objeto TextIOkrapper.
print(fp)
#output: <_io.TextIOWrapper name='cafe.txt' mode='w' encoding='utf-8'> 

print(fp.write('café')) # O método write em um TextI0Wrapper devolve o número de caracteres Unicode escritos
#output: 4

fp.close()



fp2 = open('cafe.txt') # Abrir um arquivo-texto sem uma codificação explícita devolve um TextIOHrapper com a codificação definida com um default conforme a localidade.
print(fp2)
#output: <to.TextIOwrapper name='cafe.txt' node='r' encoding='cp1252'>

print(fp2.encoding) # Um objeto TextIOWrapper tem um atributo de codificação que você pode inspecionar: cp1252 nesse caso.
#output: 'cp1252'

print(fp2.read()) # Na codificação cp1252 do Windows, o byte 0xc3 é um "A" (A com til) e Oxa9 é o símbolo de copyright.
#output: 'cafÃ©

fp2.close()



fp3 = open('cafe.txt', encoding='utf-8') # Abre o mesmo arquivo com a codificação correta.
print(fp3)
#output: <to.TextIOWrapper name='cafe.txt' node='r' encoding="utf-8">

print(fp3.read()) # O resultado esperado: os mesmos quatro caracteres Unicode para 'café'.
#output: 'café'

fp3.close()



fp4 = open('cafe.txt', 'rb') # A flag 'rb' abre um arquivo para leitura em modo binário.
print(fp4)
#output: <to.BufferedReader name='cafe.txt'>   → (O objeto devolvido é um BufferedReader, e não um TextIOWrapper.)

print(fp4.read()) # Leitura que retorna bytes, conforme esperado.
#output: b'caf\xc3\xa9'
 
fp4.close()