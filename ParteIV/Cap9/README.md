# Um objeto pythônico

## **Pág. 288 à 292............Representções de objetos | Retorno da classe Vector**
<details>
<summary></summary>

### Uso de alguns métodos especiais e suas funções embutidas

**Python tem duas maneiras-padrão de obter uma representação em string de qualquer objeto:**</br>
**• função embutida `repr()` → método especial `__repr__`:***Devolve uma string que representa o objeto como o **DESENVOLVEDOR** quer vê-lo.*</br>
**• função embutida `str()` → método especial `__str__`:***Devolve uma string que representa o objeto como o **USUÁRIO** quer vê-lo.*</br>

**Exemplo:**

```python
from array import array
import math

class Vector2d:
    typecode = 'd'  # atributo de classe para converter instâncias da classe para de bytes em __bytes__

    def __init__(self, x, y): # converte os argumentos para float ao serem passados como argumentos inválidos (int nesse caso), previnindo erros...
        self.x = float(x)
        self.y = float(y)

    def __iter__(self): # torna a classe um iterável, ou seja, um vetor (iterável → possibilita o desempacotamento, ex: x, y = my_obj
        return (i for i in (self.x, self.y))  

    def __repr__(self): # Devolve uma string que representa o objeto como o DESENVOLVEDOR quer vê-lo
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)  # cria uma string para o DESENVOLVEDOR interpolando os componentes com {!r} para obter sua repr; como a classe é iterável (graças a __iter__), *self alimenta format com os componentes x e y

    def __str__(self): # Devolve uma string que representa o objeto como o USUÁRIO quer vê-lo
        return str(tuple(self))  # a partir da classe iterável (graças a __iter__), cria uma tupla a ser exibida como um par ordenado para o USUÁRIO

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +  # para gerar bytes, convertemos o bytecode para bytes e concatenamos
                bytes(array(self.typecode, self)))  # bytes convertidos a partir de um array criado por iteração na instância

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)  # magnitude = hipotenusa do triângulo formado pelos componentes-catetos x e y

    def __bool__(self):
        return bool(abs(self))  # usa abs para retornar se há magnitude; 0.0 é False, valores diferentes de zero é True

# emprego de __init__
v1 = Vector2d(3, 4) # cria o objeto v1 iterável, ou seja, o vetor v1 (iterável → possibilita o desempacotamento, ex: x, y = my_obj)
print(v1.x, v1.y)  # os componentes do vetor podem ser acessados diretamente como atributos, sem chamadas à metodos getter
#output: 3.0 4.0

# emprego de __iter__
x, y = v1  # o objeto vetor v1 é herdou da classe a implementação para ser iterável (iterável → possibilita o desempacotamento, ex: x, y = my_obj)
x, y
#output: (3.0, 4.0)

# emprego de __repr__
v1  # __repr__ Devolve uma string que representa o objeto como o DESENVOLVEDOR quer vê-lo
#output:Vector2d(3.0, 4.0)

# emprego de __str__
print(v1)  #__str__ Devolve uma string que representa o objeto como o USUÁRIO quer vê-lo
#output:(3.0, 4.0)

# emprego de __bytes__
octets = bytes(v1)  # a função embutida bytes, usa o método especial __bytes__ para gerar uma representação binária
#return →  b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'

# emprego de __eq__
v1_clone = eval(repr(v1))  # a cópia v1_clone, de v1, mostra que repr é uma representação fiel da chamada ao seu construtor↓
v1 == v1_clone 
#return →  True

# emprego de __abs__
abs(v1)  # a função embutida abs, usa o método especial __abs__ para devolver a magnitude do vetor (magnitude = hipotenusa do triângulo formado pelos componentes-catetos x e y)
#return →  5.0

# emprego de __bool__
bool(v1), bool(Vector2d(0, 0))  # a função embutida bool, usa o método especial __bool__ para devolver False para vetores de magnitude zero ou True, caso contrário
#return →  (True, False)

```

</details>
</br>


## **Pág. 292 à 294............Um construtor alternativo(@classmethod) | classmethod versus staticmethod**
<details>
<summary></summary>

**Ambos `@classmethod` e `@staticmethod` são decoradores em Python usados para definir métodos que pertencem à classe, em vez de pertencer a instâncias individuais da classe. No entanto, eles têm propósitos ligeiramente diferentes:**</br></br>

*Em resumo, `@classmethod` é usado quando você precisa de acesso aos atributos de classe, enquanto `@staticmethod` é usado quando você precisa de um método independente da instância ou da classe.*

1. **`@classmethod`**:
   - Um método de classe recebe a classe como o primeiro argumento (por convenção chamado de `cls`).
   - Ele pode acessar e modificar os atributos de classe, mas não pode acessar os atributos da instância diretamente.
   - Geralmente usado quando o método precisa acessar ou modificar atributos de classe específicos.

2. **`@staticmethod`**:
   - Um método estático não recebe automaticamente nenhum argumento especial (nem a instância nem a classe).
   - Ele não pode acessar ou modificar os atributos da classe ou da instância.
   - É usado quando o método não precisa de acesso a atributos de classe ou de instância e pode ser definido de forma independente da classe.

**Exemplo:**

```python
class Demo:
    @classmethod
    def klassmeth(*args): # por convenção poderiamos usar `cls` no lugar de `*args` (*args, porém, possibilita usar qualquer número de argumentos posicionais)
        return args # retorna todos os argumentos posicionais `args` (inclui a classe enviada como parâmetro através do decorador @classmethod)

    @staticmethod
    def statmeth(*args):
        return args # também retorna todos os argumentos posicionais `args` (porém comportando-se como função simples)


Demo.klassmeth()
#output: (<class '__main__.Demo'>,)
Demo.klassmeth('spam')
#output: (<class '__main__.Demo'>, 'spam')

Demo.statmeth()
#output: ()
Demo.statmeth('spam')
#output: ('spam')

```

**"Portanto, `@classmethod` é muito útil, entretanto, `@staticmethod`, não muito" – Luciano Ramalho.**

### **(Amprimora Vector2d da pag288à292):**
**→ inclusão do método de classe `frombytes` e exemplo de seu uso**</br>
O decorador @classmethod indica que esse método é um método de classe, e não um método de instância. Isso significa que o método será associado à classe em vez de ser associado a instâncias individuais da classe. Isso permite que o método acesse e manipule dados da classe, em vez de dados de instância específicos.

```python
from array import array
import math


class Vector2d: # Vector2d (pag288à292) aprimorado
    typecode = 'd'  # atributo de classe para converter instâncias da classe para de bytes em __bytes__

    def __init__(self, x, y): # converte os argumentos para float ao serem passados como argumentos inválidos (int nesse caso), previnindo erros...
        self.x = float(x)
        self.y = float(y)

    def __iter__(self): # torna a classe um iterável, ou seja, um vetor (iterável → possibilita o desempacotamento, ex: x, y = my_obj
        return (i for i in (self.x, self.y))  

    def __repr__(self): # Devolve uma string que representa o objeto como o DESENVOLVEDOR quer vê-lo
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)  # cria uma string para o DESENVOLVEDOR interpolando os componentes com {!r} para obter sua repr; como a classe é iterável (graças a __iter__), *self alimenta format com os componentes x e y

    def __str__(self): # Devolve uma string que representa o objeto como o USUÁRIO quer vê-lo
        return str(tuple(self))  # a partir da classe iterável (graças a __iter__), cria uma tupla a ser exibida como um par ordenado para o USUÁRIO

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +  # para gerar bytes, convertemos o bytecode para bytes e concatenamos
                bytes(array(self.typecode, self)))  # bytes convertidos a partir de um array criado por iteração na instância

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)  # magnitude = hipotenusa do triângulo formado pelos componentes-catetos x e y

    def __bool__(self):
        return bool(abs(self))  # usa abs para retornar se há magnitude; 0.0 é False, valores diferentes de zero é True
    

    #begin:↓=======INCLUSÃO DO MÉTODO DE CLASSE frombytes=================================================
    """O decorador @classmethod indica que esse método é um método de classe, e não um método 
    de instância. Isso significa que o método será associado à classe em vez de ser associado 
    a instâncias individuais da classe. Isso permite que o método acesse e manipule dados da 
    classe, em vez de dados de instância específicos.
    """
    @classmethod # o decorador classmethod define que o método frozembytes será um método de classe
    def frombytes(cls, octets):  # não há argumento self, em vez disso a própria classe é passada como cls
        typecode = chr(octets[0])  # lê o typecode no primeiro byte
        memv = memoryview(octets[1:]).cast(typecode)  # cria uma memoryview a partir da sequência binária octets e usa o typecode para fazer o cast dos dados →obs: sobre "Memory Views", ver pág.78...
        return cls(*memv)  # desempacota a memoryview resultante do cast, produzindo o par de argumentos necessário ao construtor.
    
    #end:↑=======INCLUSÃO DO MÉTODO DE CLASSE frombytes=================================================

# emprego de __init__
v1 = Vector2d(3, 4) # cria o objeto v1 iterável, ou seja, o vetor v1 (iterável → possibilita o desempacotamento, ex: x, y = my_obj)
print(v1.x, v1.y)  # os componentes do vetor podem ser acessados diretamente como atributos, sem chamadas à metodos getter
#output: 3.0 4.0

# emprego de __iter__
x, y = v1  # o objeto vetor v1 é herdou da classe a implementação para ser iterável (iterável → possibilita o desempacotamento, ex: x, y = my_obj)
x, y
#output: (3.0, 4.0)

# emprego de __repr__
v1  # __repr__ Devolve uma string que representa o objeto como o DESENVOLVEDOR quer vê-lo
#output:Vector2d(3.0, 4.0)

# emprego de __str__
print(v1)  #__str__ Devolve uma string que representa o objeto como o USUÁRIO quer vê-lo
#output:(3.0, 4.0)

# emprego de __bytes__
octets = bytes(v1)  # a função embutida bytes, usa o método especial __bytes__ para gerar uma representação binária
#return →  b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'


#begin:↓=======EXEMPLO DE USO DO MÉTODO DE CLASSE frombytes=====================
v1_clone = Vector2d.frombytes(bytes(v1))

# emprego de __repr__
v1_clone  # __repr__ Devolve uma string que representa o objeto como o DESENVOLVEDOR quer vê-lo
#output:Vector2d(3.0, 4.0)

# emprego de __eq__
v1 == v1_clone 
#return →  True

#end:↑=======EXEMPLO DE USO DO MÉTODO DE CLASSE frombytes=====================


# emprego de __abs__
abs(v1)  # a função embutida abs, usa o método especial __abs__ para devolver a magnitude do vetor (magnitude = hipotenusa do triângulo formado pelos componentes-catetos x e y)
#return →  5.0

# emprego de __bool__
bool(v1), bool(Vector2d(0, 0))  # a função embutida bool, usa o método especial __bool__ para devolver False para vetores de magnitude zero ou True, caso contrário
#return →  (True, False)

```

</details>
</br>


## **Pág. 295 à 298............Apresentações formatadas**
<details>
<summary></summary>

**• função embutida `format()` → método especial `__format__`:**</br>
*→ `format_spec` é um especificador de formatação que é*</br>
 - o segundo argumento em `format(my_obj, format_spec)`:
 - o que estiver após os dois-pontos em um campo de substituição delimitado por `{field_name:format_spec}` em uma string de formatação usada com `str.format()`. *→ sintaxe:* `'str {field_name:format_spec} str'.format(field_name=obj)` 

```python
brl = 1/5.03 # conversão de moeda: BRL = USD
#output: 0.19880715705765407554671968190855

format(brl, '0.4f') # o segundo argumento em format(brl, '0.4f') é o format_spec
#output: 0.1988

'1 BRL = {rate:0.2f} USD'.format(rate=brl) #
#output: 1 BRL = 0.19 USD

```

*A notação básica é `{:}`, mas ela pode ser estendida para incluir especificadores de conversão, com as flags `!s`, `!r` e `!a`:*
 - `{:}:` Este é o campo de substituição básico. Os valores são convertidos em strings usando o método str().
 - `!s:` Este especificador de conversão é usado para formatar o valor como uma string usando str().
 - `!r:` Este especificador de conversão é usado para formatar o valor como uma representação de string, normalmente retornada pelo método repr().
 - `!a:` Este especificador de conversão é usado para formatar o valor como uma representação de string segura para ASCII, normalmente retornada pelo método ascii().

*`format`, dentre outros códigos de Mililinguagem de Especificação de Formatação, aceita: `b` para saída em base 2, `x` para saída em base 16, f para float, % para porcentagem:*

```python
formate(42, 'b')
#output: '101010'

format(2/3, '.1%')
#output: '66.6%'
```

### **(Amprimora Vector2d da pag292à293):**
**→ Implementação do método especial `__format__` e uso da sua função embutida `format()`**</br>

```python
from array import array
import math

class Vector2d:  # aprimoramento do Vector2d da pag292à293 (→ o qual foi aprimorado de pag288a292)
    typecode = 'd'  # atributo de classe para converter instâncias da classe para de bytes em __bytes__

    def __init__(self, x, y): # converte os argumentos para float ao serem passados como argumentos inválidos (int nesse caso), previnindo erros...
        self.x = float(x)
        self.y = float(y)

    def __iter__(self): # torna a classe um iterável, ou seja, um vetor (iterável → possibilita o desempacotamento, ex: x, y = my_obj
        return (i for i in (self.x, self.y))  

    def __repr__(self): # Devolve uma string que representa o objeto como o DESENVOLVEDOR quer vê-lo
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)  # cria uma string para o DESENVOLVEDOR interpolando os componentes com {!r} para obter sua repr; como a classe é iterável (graças a __iter__), *self alimenta format com os componentes x e y

    def __str__(self): # Devolve uma string que representa o objeto como o USUÁRIO quer vê-lo
        return str(tuple(self))  # a partir da classe iterável (graças a __iter__), cria uma tupla a ser exibida como um par ordenado para o USUÁRIO

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +  # para gerar bytes, convertemos o bytecode para bytes e concatenamos
                bytes(array(self.typecode, self)))  # bytes convertidos a partir de um array criado por iteração na instância

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self): # ♦coordenadas retângulares (será usado em else em __format__ ↓)
        return math.hypot(self.x, self.y)  # magnitude = hipotenusa do triângulo formado pelos componentes-catetos x e y

    def __bool__(self):
        return bool(abs(self))  # usa abs para retornar se há magnitude; 0.0 é False, valores diferentes de zero é True
    

    #begin:↓=======INCLUSÃO DO MÉTODO ESPECIAL __format__=================================================
    def angle(self): # ♦coordenadas polares (será usado em if em __format__ ↓)
        return math.atan2(self.y, self.x) # ângulo da magnitude (= hipotenusa, em __abs__↑)

    def __format__(self, fmt_spec=''): #sintaxe: format(obj, especificadorDeFormatação)   →ou→   'str {field_name:especificadorDeFormatação} str'.format(field_name=obj)
        # caso a formatação terminar com 'p': use ♦coordenadas polares (angle):
        if fmt_spec.endswith('p'): 
            fmt_spec = fmt_spec[:-1] # remove o sufixo 'p' de fmt_spec
            coords = (abs(self), self.angle()) # cria tuple de coordenadas polares: (magnitude, angle)
            outer_fmt = '<{}, {}>' # configura a formatação exterma delimitada por sinais de menor e de maior
        
        # caso a formatação não terminar com 'p': use ♦coordenadas retângulares (__abs__):
        else:
            coords = self # usa componentes de x, y de self para coordenadas retangulares
            outer_fmt = '({}, {})' # configura a formatação externa com parênteses
        
        components = (format(c, fmt_spec) for c in coords) # gera iterável com componentes como srings formatadas
        return outer_fmt.format(*components) # insere strings formatadas na formatação externa
    
    #begin:↑=======INCLUSÃO DO MÉTODO ESPECIAL __format__=================================================

    
    """O decorador @classmethod indica que esse método é um método de classe, e não um método de instância. Isso significa que o método será associado à classe 
    em vez de ser associado a instâncias individuais da classe. Isso permite que o método acesse e manipule dados da classe, em vez de dados de instância específicos."""
    @classmethod # o decorador classmethod define que o método frozembytes será um método de classe
    def frombytes(cls, octets):  # não há argumento self, em vez disso a própria classe é passada como cls
        typecode = chr(octets[0])  # lê o typecode no primeiro byte
        memv = memoryview(octets[1:]).cast(typecode)  # cria uma memoryview a partir da sequência binária octets e usa o typecode para fazer o cast dos dados →obs: sobre "Memory Views", ver pág.78...
        return cls(*memv)  # desempacota a memoryview resultante do cast, produzindo o par de argumentos necessário ao construtor.


# emprego de __init__
v1 = Vector2d(3, 4) # cria o objeto v1 iterável, ou seja, o vetor v1 (iterável → possibilita o desempacotamento, ex: x, y = my_obj)
print(v1.x, v1.y)  # os componentes do vetor podem ser acessados diretamente como atributos, sem chamadas à metodos getter
#output: 3.0 4.0

# emprego de __iter__
x, y = v1  # o objeto vetor v1 é herdou da classe a implementação para ser iterável (iterável → possibilita o desempacotamento, ex: x, y = my_obj)
x, y
#output: (3.0, 4.0)

# emprego de __repr__
v1  # __repr__ Devolve uma string que representa o objeto como o DESENVOLVEDOR quer vê-lo
#output:Vector2d(3.0, 4.0)

# emprego de __str__
print(v1)  #__str__ Devolve uma string que representa o objeto como o USUÁRIO quer vê-lo
#output:(3.0, 4.0)

# emprego de __bytes__
octets = bytes(v1)  # a função embutida bytes, usa o método especial __bytes__ para gerar uma representação binária
#return →  b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'

v1_clone = Vector2d.frombytes(bytes(v1))

# emprego de __repr__
v1_clone  # __repr__ Devolve uma string que representa o objeto como o DESENVOLVEDOR quer vê-lo
#output:Vector2d(3.0, 4.0)

# emprego de __eq__
v1 == v1_clone 
#return →  True

# emprego de __abs__
abs(v1)  # a função embutida abs, usa o método especial __abs__ para devolver a magnitude do vetor (magnitude = hipotenusa do triângulo formado pelos componentes-catetos x e y)
#return →  5.0

# emprego de __bool__
bool(v1), bool(Vector2d(0, 0))  # a função embutida bool, usa o método especial __bool__ para devolver False para vetores de magnitude zero ou True, caso contrário
#return →  (True, False)


#begin:↓=======EXEMPLO DE USO DO MÉTODO ESPECIAL __format__=====================

#Teste da função embutida format() com ♦coordenadas cartesianas:
format(v1) # a formatação é default: format(v1, fmt_spec=''), portanto não termina com 'p': → entra em else de __format__
#return →  '(3.0, 4.0)'
format(v1, '.2f') # a formatação não termina com 'p': → entra em else de __format__
#return →  '(3.00, 4.00)'
format(v1, '.3e') # a formatação não termina com 'p': → entra em else de __format__
#return →  '(3.000e+00, 4.000e+00)'


#Teste do método angle():
Vector2d(0, 0).angle()
#return →  0.0
Vector2d(1, 0).angle()
#return →  0.0
epsilon = 10**-8
abs(Vector2d(0, 1).angle() - math.pi/2) < epsilon
#return →  True
abs(Vector2d(1, 1).angle() - math.pi/4) < epsilon
#return →  True


#Teste da função embutida format() com ♦coordenadas polares:
format(Vector2d(1, 1), 'p')  # a formatação termina com 'p': → entra em if de __format__
#return →  '<1.414213..., 0.785398...>'
format(Vector2d(1, 1), '.3ep') # a formatação termina com 'p': → entra em if de __format__
#return →  '<1.414e+00, 7.854e-01>'
format(Vector2d(1, 1), '0.5fp') # a formatação termina com 'p': → entra em if de __format__
#return →  '<1.41421, 0.78540>'

#begin:↑=======EXEMPLO DE USO DO MÉTODO ESPECIAL __format__=====================

```

</details>
</br>


## **Pág. 298 à 304............Um Vector2d hashable**
<details>
<summary></summary>

### **(Amprimora Vector2d da pag295à298):**
**→ Inclusão dos atributos `x` e `y` privados (`__x, __y`), decorador `@property` e método especial `__hash__`, tornando a classe hashable + Exemplo de uso**</br>

```python
from array import array
import math

class Vector2d: # aprimoramento do Vector2d da pag295a298 (→ o qual foi aprimorado de pag292à293, aprimorado de pag288a292)
    typecode = 'd'

    """
    Tornar os atributos x e y privados usando dois underscores (__) é uma prática comum para garantir que eles não sejam acessados 
    diretamente fora da classe. Isso é útil não apenas para controlar o acesso aos dados, mas também para tornar a classe hashable.

    Quando uma classe é usada como chave em um conjunto (set) em Python (set → {key:value} → hash[key]=value), ela precisa ser hashable. 
    Para que uma classe seja considerada hashable, ela deve implementar os métodos __hash__() e __eq__(). Se os atributos da classe 
    forem mutáveis, como listas, conjuntos ou dicionários, a classe não poderá ser hashable.

    Ao tornar os atributos x e y privados e controlar o acesso a eles por meio de métodos getters (@property), você pode garantir 
    que esses atributos não sejam modificados fora da classe de uma maneira que comprometa a hashability da instância da classe.
    """
    def __init__(self, x, y):
        self.__x = float(x) # usando dois underscores __ na frente, deixa o atributo x privado
        self.__y = float(y) # atributo y é privado (atributos privados precisam de método getter para acesso)

    """ 
    o decorador @property a seguir é necessário para expor os atributos x e y privados (__x e __y):
    1.→ Os atributos __x e __y são definidos como privados usando dois underscores (__). Isso significa 
    que eles não podem ser acessados diretamente de fora da classe. Portanto, os métodos getter x e y, marcados 
    com @property, são necessários para permitir o acesso controlado a esses atributos de fora da classe.
    2.→ Ao usar métodos getter para acessar os atributos, você pode adicionar lógica adicional, como 
    validações de entrada ou cálculos, se necessário, antes de retornar os valores. Isso garante 
    que o acesso aos atributos seja feito de maneira segura e consistente.
    3.→ Os métodos getter x e y servem como a interface pública para acessar os atributos __x e __y. Usar o decorador 
    @property os marca como propriedades da classe, tornando sua utilização mais intuitiva para os usuários da classe.
    """
    @property
    def x(self):  # Método getter para acessar o atributo privado x.
        return self.__x  # Retorna o valor do atributo privado x.

    @property
    def y(self):  # Método getter para acessar o atributo privado y.
        return self.__y  # Retorna o valor do atributo privado y.

    def __iter__(self): # torna a classe um iterável, ou seja, um vetor (iterável → possibilita o desempacotamento, ex: x, y = my_obj
        return (i for i in (self.x, self.y))  

    def __repr__(self): # Devolve uma string que representa o objeto como o DESENVOLVEDOR quer vê-lo
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)  # cria uma string para o DESENVOLVEDOR interpolando os componentes com {!r} para obter sua repr; como a classe é iterável (graças a __iter__), *self alimenta format com os componentes x e y

    def __str__(self): # Devolve uma string que representa o objeto como o USUÁRIO quer vê-lo
        return str(tuple(self))  # a partir da classe iterável (graças a __iter__), cria uma tupla a ser exibida como um par ordenado para o USUÁRIO

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +  # para gerar bytes, convertemos o bytecode para bytes e concatenamos
                bytes(array(self.typecode, self)))  # bytes convertidos a partir de um array criado por iteração na instância

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __abs__(self): # ♦coordenadas retângulares (será usado em else em __format__ ↓)
        return math.hypot(self.x, self.y)  # magnitude = hipotenusa do triângulo formado pelos componentes-catetos x e y

    def __bool__(self):
        return bool(abs(self))  # usa abs para retornar se há magnitude; 0.0 é False, valores diferentes de zero é True

    def angle(self): # ♦coordenadas polares (será usado em if em __format__ ↓)
        return math.atan2(self.y, self.x) # ângulo da magnitude (= hipotenusa, em __abs__↑)

    def __format__(self, fmt_spec=''): #sintaxe: format(obj, especificadorDeFormatação)   →ou→   'str {field_name:especificadorDeFormatação} str'.format(field_name=obj)
        # caso a formatação terminar com 'p': use ♦coordenadas polares (angle):
        if fmt_spec.endswith('p'): 
            fmt_spec = fmt_spec[:-1] # remove o sufixo 'p' de fmt_spec
            coords = (abs(self), self.angle()) # cria tuple de coordenadas polares: (magnitude, angle)
            outer_fmt = '<{}, {}>' # configura a formatação exterma delimitada por sinais de menor e de maior
        
        # caso a formatação não terminar com 'p': use ♦coordenadas retângulares (__abs__):
        else:
            coords = self # usa componentes de x, y de self para coordenadas retangulares
            outer_fmt = '({}, {})' # configura a formatação externa com parênteses
        
        components = (format(c, fmt_spec) for c in coords) # gera iterável com componentes como srings formatadas
        return outer_fmt.format(*components) # insere strings formatadas na formatação externa
    
    """
    O decorador @classmethod abaixo indica que esse método é um método de classe, e não um método de instância. Isso significa que o método será associado à classe 
    em vez de ser associado a instâncias individuais da classe. Isso permite que o método acesse e manipule dados da classe, em vez de dados de instância específicos.
    """
    @classmethod # o decorador classmethod define que o método frozembytes será um método de classe
    def frombytes(cls, octets):  # não há argumento self, em vez disso a própria classe é passada como cls
        typecode = chr(octets[0])  # lê o typecode no primeiro byte
        memv = memoryview(octets[1:]).cast(typecode)  # cria uma memoryview a partir da sequência binária octets e usa o typecode para fazer o cast dos dados →obs: sobre "Memory Views", ver pág.78...
        return cls(*memv)  # desempacota a memoryview resultante do cast, produzindo o par de argumentos necessário ao construtor.



# emprego de __init__
v1 = Vector2d(3, 4) # cria o objeto v1 iterável, ou seja, o vetor v1 (iterável → possibilita o desempacotamento, ex: x, y = my_obj)
print(v1.x, v1.y)  # os componentes do vetor podem ser acessados diretamente como atributos, sem chamadas à metodos getter
#output: 3.0 4.0


# emprego de __iter__
x, y = v1  # o objeto vetor v1 é herdou da classe a implementação para ser iterável (iterável → possibilita o desempacotamento, ex: x, y = my_obj)
x, y
#output: (3.0, 4.0)


# emprego de __repr__
v1  # __repr__ Devolve uma string que representa o objeto como o DESENVOLVEDOR quer vê-lo
#output: Vector2d(3.0, 4.0)


# emprego de __str__
print(v1)  #__str__ Devolve uma string que representa o objeto como o USUÁRIO quer vê-lo
#output: (3.0, 4.0)


# emprego de __bytes__
octets = bytes(v1)  # a função embutida bytes, usa o método especial __bytes__ para gerar uma representação binária
##output: b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'


# teste de frombytes()
v1_clone = Vector2d.frombytes(bytes(v1))


# emprego de __eq__
v1 == v1_clone 
##output: True


#Testes de x e y, somente como leitura:
v1.x, v1.y
#output: (3.0, 4.0)
v1.x = 123
'''output:
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
'''


# emprego de __hash__
v1 = Vector2d(3, 4)
v2 = Vector2d(3.1, 4.2)
hash(v1), hash(v2)
#return →  (7, 384307168202284039)
len(set([v1, v2])) # por ser hashable suporta conjunto (set → {key:value} → hash[key]=value)
#output: 2


# emprego de __abs__
abs(v1)  # a função embutida abs, usa o método especial __abs__ para devolver a magnitude do vetor (magnitude = hipotenusa do triângulo formado pelos componentes-catetos x e y)
#output: 5.0


# emprego de __bool__
bool(v1), bool(Vector2d(0, 0))  # a função embutida bool, usa o método especial __bool__ para devolver False para vetores de magnitude zero ou True, caso contrário
#output: (True, False)


# teste de angle()
Vector2d(0, 0).angle()
#output: 0.0
Vector2d(1, 0).angle()
#output: 0.0
epsilon = 10**-8
abs(Vector2d(0, 1).angle() - math.pi/2) < epsilon
#output: True
abs(Vector2d(1, 1).angle() - math.pi/4) < epsilon
#output: True


# emprego de __format__
#Teste da função embutida format() com ♦coordenadas cartesianas:
format(v1) # a formatação é default: format(v1, fmt_spec=''), portanto não termina com 'p': → entra em else de __format__
#output: '(3.0, 4.0)'
format(v1, '.2f') # a formatação não termina com 'p': → entra em else de __format__
#output: '(3.00, 4.00)'
format(v1, '.3e') # a formatação não termina com 'p': → entra em else de __format__
#output: '(3.000e+00, 4.000e+00)'

#Teste da função embutida format() com ♦coordenadas polares:
format(Vector2d(1, 1), 'p')  # a formatação termina com 'p': → entra em if de __format__
#output: '<1.414213..., 0.785398...>'
format(Vector2d(1, 1), '.3ep') # a formatação termina com 'p': → entra em if de __format__
#output: '<1.414e+00, 7.854e-01>'
format(Vector2d(1, 1), '0.5fp') # a formatação termina com 'p': → entra em if de __format__
#output: '<1.41421, 0.78540>'

```

</details>
</br>


## **Pág. xxx à yyy............Nome | Nome**
<details>
<summary></summary>

**Destaque**</br>
*→ explicação*</br>

**Exemplo:**

```python
#code
```

</details>
</br>


## **Pág. xxx à yyy............Nome | Nome**
<details>
<summary></summary>

**Destaque**</br>
*→ explicação*</br>

**Exemplo:**

```python
#code
```

</details>
</br>