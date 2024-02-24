def f1(a):
    print(a)
    print(b)


from dis import dis
dis(f1)
# output:
  2           0 LOAD_GLOBAL              0 (print)              # Carrega a função global 'print'
              2 LOAD_FAST                0 (a)                  # Carrega 'a' como LOCAL (LOAD_FAST)
              4 CALL_FUNCTION            1                      # Chama a função 'print' com 1 argumento
              6 POP_TOP                                         # Remove o topo da pilha

  3           8 LOAD_GLOBAL              0 (print)              # Carrega a função global 'print'
             10 LOAD_GLOBAL              1 (b)                  # Carrega 'b' como GLOBAL (LOAD_GLOBAL)
             12 CALL_FUNCTION            1                      # Chama a função 'print' com 1 argumento
             14 POP_TOP                                         # Remove o topo da pilha
             16 LOAD_CONST               0 (None)               # Carrega a constante None
             18 RETURN_VALUE                                    # Retorna o valor


f1(3)
'''output:
3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in f1
NameError: name 'b' is not defined
'''

#———————————————————————————————————————————————————————————————————————————


def f1(a):
    print(a)
    print(b)


from dis import dis
dis(f1)
# output:
  2           0 LOAD_GLOBAL              0 (print)                          # Carrega a função global 'print'
              3 LOAD_FAST                0 (a)                              # Carrega 'a' como LOCAL (LOAD_FAST)
              6 CALL_FUNCTION            1 (1 positional, 0 keyword pair)   # Chama a função 'print' com 1 argumento
              9 POP_TOP                                                     # Remove o topo da pilha

  3          10 LOAD_GLOBAL              0 (print)                          # Carrega a função global 'print'
             13 LOAD_GLOBAL              1 (b)                              # Carrega 'b' como GLOBAL (LOAD_GLOBAL)
             16 CALL_FUNCTION            1 (1 positional, 0 keyword pair)   # Chama a função 'print' com 1 argumento
             19 POP_TOP                                                     # Remove o topo da pilha
             20 LOAD_CONST               0 (None)                           # Carrega a constante None
             23 RETURN_VALUE                                                # Retorna o valor


b = 6
f1(3)
'''output:
3
6
'''

#———————————————————————————————————————————————————————————————————————————


b = 6
def f2(a):
    #global b
    print(a)
    print(b)
    b = 9


from dis import dis
dis(f2)
# output:
  2           0 LOAD_GLOBAL              0 (print)                          # Carrega a função global 'print'
              3 LOAD_FAST                0 (a)                              # Carrega 'a' como LOCAL (LOAD_FAST)
              6 CALL_FUNCTION            1 (1 positional, 0 keyword pair)   # Chama a função 'print' com 1 argumento
              9 POP_TOP                                                     # Remove o topo da pilha

  3          10 LOAD_GLOBAL              0 (print)                          # Carrega a função global 'print'
             13 LOAD_FAST                1 (b)                              # Carrega 'b' como LOCAL (LOAD_FAST)
             16 CALL_FUNCTION            1 (1 positional, 0 keyword pair)   # Chama a função 'print' com 1 argumento
             19 POP_TOP                                                     # Remove o topo da pilha

  4          20 LOAD_CONST               1 (9)                              # Carrega a constante 9
             23 STORE_FAST               1 (b)                              # Armazena o valor constante 9 na variável local 'b' (STORE_FAST)
             26 LOAD_CONST               0 (None)                           # Carrega a constante None
             29 RETURN_VALUE                                                # Retorna o valor


f2(3)
'''output:
3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in f2
UnboundLocalError: local variable 'b' referenced before assignment
'''

#———————————————————————————————————————————————————————————————————————————


b = 6
def f2(a):
    global b
    print(a)
    print(b)
    b = 9


from dis import dis
dis(f3)
# output:
  3           0 LOAD_GLOBAL              0 (print)                          # Carrega a função global 'print'
              3 LOAD_FAST                0 (a)                              # Carrega 'a' como LOCAL (LOAD_FAST)
              6 CALL_FUNCTION            1 (1 positional, 0 keyword pair)   # Chama a função 'print' com 1 argumento
              9 POP_TOP                                                     # Remove o topo da pilha

  4          10 LOAD_GLOBAL              0 (print)                          # Carrega a função global 'print'
             13 LOAD_GLOBAL              1 (b)                              # Carrega 'b' como GLOBAL (LOAD_GLOBAL)
             16 CALL_FUNCTION            1 (1 positional, 0 keyword pair)   # Chama a função 'print' com 1 argumento
             19 POP_TOP                                                     # Remove o topo da pilha

  5          20 LOAD_CONST               1 (9)                              # Carrega a constante 9
             23 STORE_GLOBAL             1 (b)                              # Armazena o valor constante 9 na variável global 'b' (STORE_GLOBAL)
             26 LOAD_CONST               0 (None)                           # Carrega a constante None
             29 RETURN_VALUE                                                # Retorna o valor


f2(3)
'''output:
3
6
'''

#———————————————————————————————————————————————————————————————————————————


def f4(b):
    def f5(a):
        nonlocal b # b pertence a um escopo externo ao escopo atual, mas não é global
        print(a)
        print(b)
        b = 7
    return f5


from dis import dis
dis(f5)
# output:
  4           0 LOAD_GLOBAL              0 (print)                          # Carrega a função global 'print'
              2 LOAD_FAST                0 (a)                              # Carrega 'a' como LOCAL (LOAD_FAST)
              4 CALL_FUNCTION            1                                  # Chama a função 'print' com 1 argumento
              6 POP_TOP                                                     # Remove o topo da pilha

  5           8 LOAD_GLOBAL              0 (print)                          # Carrega a função global 'print'
             10 LOAD_DEREF               0 (b)                              # Carrega 'b' do escopo envolvente (nonlocal) (LOAD_DEREF)
             12 CALL_FUNCTION            1                                  # Chama a função 'print' com 1 argumento
             14 POP_TOP                                                     # Remove o topo da pilha

  6          16 LOAD_CONST               1 (7)                              # Carrega a constante 7
             18 STORE_DEREF              0 (b)                              # Armazena o valor constante 7 na variável envolvente 'b' (STORE_DEREF)
             20 LOAD_CONST               0 (None)                           # Carrega a constante None
             22 RETURN_VALUE                                                # Retorna o valor


f5 = f4(8)
f5(2)
'''output:
2
8
'''