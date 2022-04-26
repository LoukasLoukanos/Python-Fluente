import timeit

'''
 Teste de velocidade que compara a listcomp(list comprehensions) com map/filter e lambda.
 As listcomps fazem tudo que as funções map e filter fazem, sem os contorcionismos exigidos
 pelo limitado lambda, além disso, a execução ocorre em menos tempo.
'''

TIMES = 100000 # ← more/less

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))

clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')
