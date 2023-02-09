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

'''cada item é um inteiro em range(256): 
Por exemplo, a=97, b=98, c=99, d=100, e=101, f=102, ..., \xc3=195, ..., \xa9=169, ...até256.
→ Obs: esses caracteres em utf-8 são representados por "índices", como em Unicode, e alguns até coicidem (a=97 em utf-8 e em Unicode). 
→ Nesse caso (em UTF-8) o par de bytes \xc3=195 + \xa9=169 representa o caractere "é". Já o valor \xc3=195 sozinho não representa um caractere válido.
→ "\xc3"=195 é o mesmo que "0xC3"=195 → '\x' e '0x' representam que está em hexadecimal, e 'C3' é o valor hexadecimal que é igual a 195 em deciaml)'''
print("cafe[0]: ", cafe[0]) #output: 99  → é o "índice" que representa "c" em utf-8 (o mesmo para Unicode)
print("cafe[1]: ", cafe[1]) #output: 97  → é o "índice" que representa "a" em utf-8 (o mesmo para Unicode)
print("cafe[2]: ", cafe[2]) #output: 102 → é o "índice" que representa "f" em utf-8 (o mesmo para Unicode)
print("cafe[3]: ", cafe[3]) #output: 195 → é o "índice" que representa o byte em hexadecimal "\xc3" ("0xC3") em utf-8 (em Unicode seria 'Á')
print("cafe[4]: ", cafe[4]) #output: 169 → é o "índice" que representa o byte em hexadecimal "\xc3" ("0xC3") em utf-8 (em Unicode seria '©')

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

print("cafe[-1:]: ", cafe_arr[-1:]) #output: bytearray(b'\xa9')


#____________________________________MÉTODO fromhex PARA SEQUÊNCIAS BINÁRIAS____________________________________

# CODIFICAÇÃO (de hex para bytes) usando o método fromhex que cria uma sequência binária 
# interpretando [pares] de dígitos hexadeximais [opcionalmente separados com espaços]:
f = bytes.fromhex('31 4B CE A9')

print("\ntipo f:", type(f), "\nvalor f:", f, "\ntamanho b:", len(f))
'''output:
    tipo f: <class 'bytes'>
    valor f: b'1K\xce\xa9'
    tamanho b: 4
'''

#DECODIFICAÇÃO (de bytes para str) usando a codificação UTF-8
f = f.decode('utf8')
print("\ntipo f:", type(f), "\nvalor em utf-8:", f, "\ntamanho b:", len(f))
'''output:
    tipo f: <class 'str'>
    valor f: 1KΩ
    tamanho b: 3
'''
