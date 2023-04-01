# Assim como as instâncias de uma classe comum definida pelo usuário, uma função usa o atributo_dict_para armazenar os atributos de usuário atribuídos a ela.

class C: pass # Cria uma classe vazia definida pelo usuário. 

obj = C() # Cria uma instância dessa classe. 

def func(): pass # Cria uma função vazia. 


# Gera uma lista ordenada de atributos existentes em uma função vazia:
sorted(set(dir(func)))
# output: ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


# Gera uma lista ordenada de atributos existentes em uma instância de uma classe vazia:
sorted(set(dir(obj)))
# output: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']


# Usando a diferença entre conjuntos, gera uma lista ordenada de atributos existentes em uma função, mas não em uma instância de uma classe vazia:
sorted(set(dir(func)) - set(dir(obj)))
# output: ['__annotations__', '__builtins__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
