'''
Ao tentar refazer a associação em count = count + 1 no corpo da função, foi criado implicitamente a variável local count. 
Nesse caso count deixou de ser uma variável livre, sendo assim, não salva na closure, causando o erro de referenciamento.
'''

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total/count

    return averager

avg = make_averager()
avg(10)
'''output:
Traceback (most recent call last):
  File "main.py", line 13, in <module>
    avg(10)
  File "main.py", line 6, in averager
    count += 1
UnboundLocalError: local variable 'count' referenced before assignment
'''


# Com declaração nonlocal______________________________________

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total/count

    return averager

avg = make_averager()
avg(10)
#output: 10.0