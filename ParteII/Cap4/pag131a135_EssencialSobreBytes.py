#___________________________CODIFICAÇÃO (ENCODING) E DECODIFICAÇÃO (DECODING)___________________________
s = 'café' #str café

print("\ntipo s:", type(s), "\nvalor s:", s, "\ntamanho s:", len(s))
'''
    tipo s: <class 'str'> 
    valor s: café
    tamanho s: 4
'''

#CODIFICAÇÃO (de str para bytes) usando a codificação UTF-8
b = s.encode('utf8')

print("\ntipo b:", type(b), "\nvalor b:", b, "\ntamanho b:", len(b))
'''output:
    tipo b: <class 'bytes'>
    valor b: b'caf\xc3\xa9'   →   (literais do tipo bytes começam com um prefixo b)
    tamanho b: 5   →   (o objeto bytes na variável b tem cinco bytes pois o codepoint do caractere "é" é codificado com dois bytes em UTF-8)
'''

#DECODIFICAÇÃO (de bytes para str) usando a codificação UTF-8
b.decode('utf8')


#____________________________________SEQUÊNCIA COMO BYTES E COMO BYTEARRAY____________________________________
#_________SEQUÊNCIA COMO BYTES_________
cafe =  bytes('café', encoding='utf8') #bytes podem ser construído a partir de uma str, dada uma CODIFICAÇÃO
print("\ntipo cafe:", type(cafe), "\nvalor cafe:", cafe, "\ntamanho cafe:", len(cafe), "\n")
'''output:
    tipo cafe: <class 'bytes'>
    valor cafe: b'caf\xc3\xa9'
    tamanho cafe: 5
'''

#cada item é um inteiro em range(256):
print("cafe[0]: ", cafe[0]) #output: 99
print("cafe[1]: ", cafe[1]) #output: 97
print("cafe[2]: ", cafe[2]) #output: 102
print("cafe[3]: ", cafe[3]) #output: 195
print("cafe[4]: ", cafe[4]) #output: 169

#fatias de bytes também são bytes — mesmo as fatias com um único byte:
print("cafe[:0]: ", cafe[:0]) #output: b''   →   (literais do tipo bytes começam com um prefixo b)
print("cafe[:1]: ", cafe[:1]) #output: b'c'
print("cafe[:2]: ", cafe[:2]) #output: b'ca'
print("cafe[:3]: ", cafe[:3]) #output: b'caf'
print("cafe[:4]: ", cafe[:4]) #output: b'caf\xc3'
print("cafe[:5]: ", cafe[:5]) #output: b'caf\xc3\xa9'


#_________SEQUÊNCIA COMO BYTEARRAY_________
#não existe uma sintaxe literal para bytearray: eles são mostrados como bytearray(), com um literal bytes como argumento:
cafe_arr = bytearray(cafe)
print("\ntipo cafe_arr:", type(cafe_arr), "\nvalor cafe_arr:", cafe_arr, "\ntamanho cafe_arr:", len(cafe_arr), "\n")
'''output:
    tipo cafe: <class 'bytearray'>
    valor cafe: b'caf\xc3\xa9'
    tamanho cafe: 5
'''

#cada item é um inteiro em range(256):
print("cafe_arr[0]: ", cafe_arr[0]) #output: 99
print("cafe_arr[1]: ", cafe_arr[1]) #output: 97
print("cafe_arr[2]: ", cafe_arr[2]) #output: 102
print("cafe_arr[3]: ", cafe_arr[3]) #output: 195
print("cafe_arr[4]: ", cafe_arr[4]) #output: 169

#fatias de bytearray também são bytearray — mesmo as fatias com um único bytearray:
print("cafe_arr[:0]: ", cafe_arr[:0]) #output: bytearray''   →   (literais do tipo bytes começam com um prefixo bytearray)
print("cafe_arr[:1]: ", cafe_arr[:1]) #output: bytearray'c'
print("cafe_arr[:2]: ", cafe_arr[:2]) #output: bytearray'ca'
print("cafe_arr[:3]: ", cafe_arr[:3]) #output: bytearray'caf'
print("cafe_arr[:4]: ", cafe_arr[:4]) #output: bytearray'caf\xc3'
print("cafe_arr[:5]: ", cafe_arr[:5]) #output: bytearray'caf\xc3\xa9'

print("cafe[-1:]: ", cafe_arr[-1:]) #output: b'caf\xc3\xa9'