## Python Fluente

Este livro não é uma referência exaustiva de A a Z para Python. A ênfase da obra está
nos recursos da linguagem exclusivos do Python ou que não se encontram em muitas
outras linguagens populares. Este também, em sua maior parte, é um livro sobre o
núcleo da linguagem e algumas de suas bibliotecas. Raramente é falado sobre os pacotes
que não estejam na biblioteca-padrão, apesar de o índice de pacotes do Python (PyPI)
atualmente listar mais de 60 mil bibliotecas e muitas delas serem extremamente úteis.

### Sumário
</br>
**Prefácio ............................................................................................................................ 17**</br>
</br>
**Parte I ■ Prólogo................................................................................................ 27**</br>
</br>
**Capítulo 1 ■ Modelo de dados do Python............................................................................28**</br>
Um baralho pythônico ....................................................................................29</br>
Como os métodos especiais são usados............................................................33</br>
Emulando tipos numéricos.........................................................................34</br>
Representação em string.............................................................................36</br>
Operadores aritméticos..............................................................................37</br>
Valor booleano de um tipo definido pelo usuário ........................................37</br>
Visão geral dos métodos especiais ...................................................................38</br>
Por que len não é um método?.........................................................................39</br>
Resumo do capítulo ........................................................................................40</br>
Leituras complementares................................................................................. 41</br>
</br>
**Parte II ■ Estruturas de dados............................................................................. 43**</br>
</br>
**Capítulo 2 ■ Uma coleção de sequências.............................................................................44**</br>
Visão geral das sequências embutidas..............................................................45</br>
List comprehensions e expressões geradoras ....................................................46</br>
List comprehensions e legibilidade..............................................................46</br>
Comparação entre listcomps e map/filter ....................................................48</br>
Produtos cartesianos..................................................................................49</br>
Expressões geradoras .................................................................................50</br>
Tuplas não são apenas listas imutáveis.............................................................52</br>
Tuplas como registros.................................................................................52</br>
Desempacotamento de tuplas.....................................................................53</br>
Desempacotamento de tuplas aninhadas.....................................................55</br>
Tuplas nomeadas........................................................................................56</br>
Tuplas como listas imutáveis.......................................................................58</br>
Fatiamento .....................................................................................................59</br>
Por que as fatias e os intervalos excluem o último item ................................59</br>
Objetos slice...............................................................................................60</br>
Fatiamento multidimensional e reticências..................................................62</br>
Atribuição de valores a fatias......................................................................62</br>
Usando + e * com sequências...........................................................................63</br>
Criando listas de listas ...............................................................................64</br>
Atribuições combinadas e sequências..............................................................65</br>
O enigma da atribuição +=.........................................................................67</br>
list.sort e a função embutida sorted .................................................................69</br>
Administrando sequências ordenadas com bisect.............................................71</br>
Pesquisando com bisect..............................................................................71</br>
Inserção com bisect.insort.......................................................................... 74</br>
Quando uma lista não é a resposta .................................................................. 75</br>
Arrays........................................................................................................ 75</br>
Memory Views...........................................................................................78</br>
NumPy e SciPy ..........................................................................................80</br>
Deques e outras filas ..................................................................................82</br>
Resumo do capítulo ........................................................................................86</br>
Leituras complementares.................................................................................87</br>
</br>
**Capítulo 3 ■ Dicionários e conjuntos...................................................................................93**</br>
Tipos genéricos de mapeamento......................................................................94</br>
dict comprehensions .......................................................................................96</br>
Visão geral dos métodos comuns a mapeamentos.............................................97</br>
Tratando chaves ausentes com setdefault ....................................................98</br>
Mapeamentos com consulta de chave flexível................................................. 101</br>
defaultdict: outra abordagem para chaves ausentes.................................... 101</br>
Método __missing__ .............................................................................. 102</br>
Variações de dict........................................................................................... 105</br>
Criando subclasses de UserDict..................................................................... 106</br>
Mapeamentos imutáveis................................................................................ 108</br>
Teoria dos conjuntos..................................................................................... 109</br>
Literais de set........................................................................................... 111</br>
Set comprehensions.................................................................................. 113</br>
Operações de conjuntos ........................................................................... 113</br>
Por dentro de dict e set.................................................................................. 116</br>
Um experimento para testar o desempenho .............................................. 116</br>
Tabelas hash em dicionários..................................................................... 118</br>
Consequências práticas de como os dicionários funcionam ....................... 121</br>
Como os conjuntos funcionam – consequências práticas...........................125</br>
Resumo do capítulo ......................................................................................125</br>
Leituras complementares...............................................................................126</br>
</br>
**Capítulo 4 ■ Texto versus bytes........................................................................................ 129**</br>
Falhas de caracteres ......................................................................................130</br>
O essencial sobre bytes ................................................................................. 131</br>
Structs e memory views............................................................................134</br>
Codificadores/decodificadores básicos........................................................... 135</br>
Entendendo os problemas de codificação/decodificação ................................. 137</br>
Lidando com UnicodeEncodeError........................................................... 138</br>
Lidando com UnicodeDecodeError........................................................... 139</br>
SyntaxError ao carregar módulos com codificação inesperada................... 140</br>
Como descobrir a codificação de uma sequência de bytes.......................... 142</br>
BOM: um gremlin útil.............................................................................. 142</br>
Lidando com arquivos-texto.......................................................................... 144</br>
Defaults de codificação: um hospício ........................................................ 147</br>
Normalizando Unicode para comparações mais seguras ................................ 150</br>
Case folding............................................................................................. 153</br>
Funções utilitárias para comparações normalizadas.................................. 154</br>
“Normalização” extrema: removendo acentos........................................... 155</br>
Ordenação de texto Unicode ......................................................................... 159</br>
Ordenação com o Unicode Collation Algorithm ....................................... 161</br>
Base de dados Unicode.................................................................................. 161</br>
APIs de modo dual para str e bytes................................................................ 163</br>
str versus bytes em expressões regulares................................................... 163</br>
str versus bytes em funções de os.............................................................. 165</br>
Resumo do capítulo ...................................................................................... 167</br>
Leituras complementares............................................................................... 169</br>
</br>
**Parte III ■ Funções como objetos .......................................................................174**</br>
</br>
**Capítulo 5 ■ Funções de primeira classe............................................................................ 175**</br>
Tratando uma função como um objeto .......................................................... 176</br>
Funções de ordem superior............................................................................ 177</br>
Substitutos modernos para map, filter e reduce ......................................... 178</br>
Funções anônimas ........................................................................................ 180</br>
As sete variações de objetos invocáveis .......................................................... 181</br>
Tipos invocáveis definidos pelo usuário ......................................................... 182</br>
Introspecção de função ................................................................................. 183</br>
De parâmetros posicionais a parâmetros exclusivamente nomeados ............... 185</br>
Obtendo informações sobre parâmetros ........................................................ 187</br>
Anotações de função..................................................................................... 192</br>
Pacotes para programação funcional.............................................................. 194</br>
Módulo operator...................................................................................... 194</br>
Congelando argumentos com functools.partial ......................................... 198</br>
Resumo do capítulo ......................................................................................200</br>
Leituras complementares............................................................................... 201</br>
</br>
**Capítulo 6 ■ Padrões de projeto com funções de primeira classe........................................ 205**</br>
Estudo de caso: refatorando Strategy .............................................................206</br>
Strategy clássico.......................................................................................206</br>
Strategy orientado a função ...................................................................... 210</br>
Escolhendo a melhor estratégia: abordagem simples.................................. 213</br>
Encontrando estratégias em um módulo ................................................... 214</br>
Command .................................................................................................... 216</br>
Resumo do capítulo ...................................................................................... 218</br>
Leituras complementares............................................................................... 219</br>
</br>
**Capítulo 7 ■ Decoradores de função e closures.................................................................. 222**</br>
Básico sobre decoradores...............................................................................223</br>
Quando Python executa os decoradores ........................................................ 224</br>
Padrão Strategy melhorado com decorador ....................................................226</br>
Regras para escopo de variáveis.....................................................................228</br>
Closures .......................................................................................................232</br>
Declaração nonlocal......................................................................................235</br>
Implementando um decorador simples ..........................................................237</br>
Funcionamento ........................................................................................238</br>
Decoradores da biblioteca-padrão.................................................................. 240</br>
Memoização com functools.lru_cache ...................................................... 240</br>
Funções genéricas com dispatch simples................................................... 243</br>
Decoradores empilhados............................................................................... 246</br>
Decoradores parametrizados......................................................................... 247</br>
Um decorador de registro parametrizado .................................................. 247</br>
Decorador clock parametrizado................................................................ 249</br>
Resumo do capítulo ......................................................................................252</br>
Leituras complementares...............................................................................253</br>
</br>
**Parte IV ■ Práticas de orientação a objetos ....................................................... 257**</br>
</br>
**Capítulo 8 ■ Referências a objetos, mutabilidade e reciclagem ......................................... 258**</br>
Variáveis não são caixas................................................................................ 259</br>
Identidade, igualdade e apelidos....................................................................260</br>
Escolhendo entre == e is .......................................................................... 262</br>
A relativa imutabilidade das tuplas ...........................................................263</br>
Cópias são rasas por padrão ..........................................................................264</br>
Cópias profundas e rasas de objetos quaisquer..........................................267</br>
Parâmetros de função como referências .........................................................268</br>
Tipos mutáveis como default de parâmetros: péssima ideia........................ 270</br>
Programação defensiva com parâmetros mutáveis ..................................... 272</br>
del e coleta de lixo......................................................................................... 274</br>
Referências fracas.......................................................................................... 276</br>
Esquete com WeakValueDictionary .......................................................... 277</br>
Limitações das referências fracas .............................................................. 279</br>
Truques de Python com imutáveis.................................................................280</br>
Resumo do capítulo ......................................................................................282</br>
Leituras complementares...............................................................................283</br>
</br>
**Capítulo 9 ■ Um objeto pythônico ....................................................................................288**</br>
Representações de objetos.............................................................................289</br>
Retorno da classe Vector ...............................................................................289</br>
Um construtor alternativo .............................................................................292</br>
classmethod versus staticmethod................................................................... 293</br>
Apresentações formatadas............................................................................. 295</br>
Um Vector2d hashable ..................................................................................298</br>
Atributos privados e “protegidos” em Python.................................................304</br>
Economizando espaço com o atributo de classe __slots__ ............................307</br>
Os problemas com __slots__ ...................................................................309</br>
Sobrescrita de atributos de classe................................................................... 310</br>
Resumo do capítulo ...................................................................................... 312</br>
Leituras complementares............................................................................... 313</br>
</br>
**Capítulo 10 ■ Hackeando e fatiando sequências................................................................ 318**</br>
Vector: um tipo de sequência definido pelo usuário........................................ 319</br>
Vector tomada #1: compatível com Vector2d ................................................. 319</br>
Protocolos e duck typing ............................................................................... 322</br>
Vector tomada #2: uma sequência que permite fatiamento.............................323</br>
Como funciona o fatiamento .................................................................... 324</br>
Um __getitem__ que considera fatias....................................................... 327</br>
Vector tomada #3: acesso dinâmico a atributos ............................................. 328</br>
Vector tomada #4: hashing e um == mais rápido........................................... 332</br>
Vector tomada #5: formatação ...................................................................... 338</br>
Resumo do capítulo ...................................................................................... 345</br>
Leituras complementares............................................................................... 347</br>
</br>
**Capítulo 11 ■ Interfaces: de protocolos a ABCs.................................................................. 352**</br>
Interfaces e protocolos na cultura de Python.................................................. 353</br>
Python curte sequências................................................................................ 355</br>
Monkey-patching para implementar um protocolo em tempo de execução...... 357</br>
Aves aquáticas de Alex Martelli..................................................................... 359</br>
Criando subclasses de uma ABC ...................................................................365</br>
ABCs da biblioteca-padrão............................................................................367</br>
ABCs em collections.abc ..........................................................................367</br>
A torre numérica de ABCs........................................................................ 369</br>
Definindo e usando uma ABC....................................................................... 370</br>
Detalhes de sintaxe das ABCs................................................................... 374</br>
Herdando da ABC Tombola ..................................................................... 375</br>
Uma subclasse virtual de Tombola............................................................ 378</br>
Como as subclasses de Tombola foram testadas............................................. 381</br>
Uso de register na prática ..............................................................................384</br>
Gansos podem se comportar como patos.......................................................385</br>
Resumo do capítulo ......................................................................................386</br>
Leituras complementares............................................................................... 389</br>
</br>
**Capítulo 12 ■ Herança: para o bem ou para o mal ............................................................. 395**</br>
Artimanhas da criação de subclasses de tipos embutidos ............................... 396</br>
Herança múltipla e ordem de resolução de métodos....................................... 399</br>
Herança múltipla no mundo real ...................................................................404</br>
Lidando com herança múltipla ......................................................................407</br>
1. Faça a distinção entre herança de interface e herança de implementação 407</br>
2. Deixe as interfaces explícitas com ABCs ...............................................407</br>
3. Use mixins para reutilização de código .................................................407</br>
4. Explicite as mixins pelo nome...............................................................408</br>
5. Uma ABC também pode ser uma mixin; o contrário não é verdade........408</br>
6. Não herde de mais de uma classe concreta ............................................408</br>
7. Ofereça classes agregadas aos usuários..................................................409</br>
8. “Prefira composição de objetos à herança de classe.” .............................409</br>
Tkinter: o bom, o ruim e o feio................................................................. 410</br>
Um exemplo moderno: mixins em views genéricas de Django ........................ 411</br>
Resumo do capítulo ...................................................................................... 414</br>
Leituras complementares............................................................................... 415</br>
</br>
**Capítulo 13 ■ Sobrecarga de operadores: o jeito certo....................................................... 419**</br>
Básico da sobrecarga de operadores............................................................... 420</br>
Operadores unários ...................................................................................... 420</br>
Sobrecarregando + para soma de vetores .......................................................423</br>
Sobrecarregando * para multiplicação por escalar........................................... 429</br>
Operadores de comparação rica..................................................................... 433</br>
Operadores de atribuição combinada ............................................................ 438</br>
Resumo do capítulo ......................................................................................443</br>
Leituras complementares...............................................................................444</br>
</br>
**Parte V ■ Controle de fluxo............................................................................... 449**</br>
</br>
**Capítulo 14 ■ Iteráveis, iteradores e geradores................................................................. 450**</br>
Sentence tomada #1: uma sequência de palavras............................................ 451</br>
Por que sequências são iteráveis: a função iter ........................................... 453</br>
Iteráveis versus iteradores.............................................................................. 455</br>
Sentence tomada #2: um iterador clássico...................................................... 459</br>
Fazer de Sentence um iterador: péssima ideia ............................................460</br>
Sentence tomada #3: uma função geradora.................................................... 461</br>
Como funciona uma função geradora .......................................................462</br>
Sentence tomada #4: uma implementação lazy ..............................................466</br>
Sentence tomada #5: uma expressão geradora ...............................................467</br>
Expressões geradoras: quando usá-las ...........................................................469</br>
Outro exemplo: gerador de progressão aritmética .......................................... 470</br>
Progressão aritmética com itertools .......................................................... 473</br>
Funções geradoras na biblioteca-padrão......................................................... 474</br>
Nova sintaxe em Python 3.3: yield from.........................................................485</br>
Funções de redução de iteráveis.....................................................................486</br>
Uma visão mais detalhada da função iter.......................................................488</br>
Estudo de caso: geradores em um utilitário para conversão de banco de dados...............489</br>
Geradores como corrotinas ........................................................................... 491</br>
Resumo do capítulo ......................................................................................492</br>
Leituras complementares............................................................................... 493</br>
</br>
**Capítulo 15 ■ Gerenciadores de contexto e blocos else...................................................... 499**</br>
Faça isso, então aquilo: blocos else além de if.................................................500</br>
Gerenciadores de contexto e blocos with ....................................................... 502</br>
Utilitários de contextlib ................................................................................ 507</br>
Usando @contextmanager............................................................................508</br>
Resumo do capítulo ...................................................................................... 512</br>
Leituras complementares............................................................................... 512</br>
</br>
**Capítulo 16 ■ Corrotinas .................................................................................................. 515**</br>
Como as corrotinas evoluíram a partir de geradores....................................... 516</br>
Comportamento básico de um gerador usado como corrotina ........................ 517</br>
Exemplo: corrotina para calcular uma média cumulativa ............................... 520</br>
Decoradores para preparação de corrotinas.................................................... 522</br>
Término de corrotinas e tratamento de exceção ............................................. 524</br>
Devolvendo um valor a partir de uma corrotina ............................................. 528</br>
Usando yield from......................................................................................... 530</br>
O significado de yield from............................................................................ 536</br>
Caso de uso: corrotinas para uma simulação de eventos discretos .................. 543</br>
Sobre simulações de eventos discretos....................................................... 543</br>
A simulação da frota de táxis....................................................................544</br>
Resumo do capítulo ...................................................................................... 552</br>
Leituras complementares............................................................................... 554</br>
</br>
**Capítulo 17 ■ Concorrência com futures............................................................................560**</br>
Exemplo: downloads da Web em três estilos..................................................560</br>
Um script para download sequencial ........................................................563</br>
Fazendo download com concurrent.futures .............................................. 565</br>
Onde estão os futures? .............................................................................566</br>
E/S bloqueante e a GIL.................................................................................. 570</br>
Iniciando processos com concurrent.futures.................................................. 571</br>
Fazendo experimentos com Executor.map..................................................... 573</br>
Downloads com exibição de progresso e tratamento de erros ......................... 576</br>
Tratamento de erros nos exemplos da série flags2 ..................................... 581</br>
Usando futures.as_completed ..................................................................584</br>
Alternativas com threading e multiprocessing ........................................... 587</br>
Resumo do capítulo ...................................................................................... 587</br>
Leituras complementares...............................................................................588</br>
</br>
**Capítulo 18 ■ Concorrência com asyncio ........................................................................... 594**</br>
Thread versus corrotina: uma comparação .................................................... 596</br>
asyncio.Future: não bloqueante por design ...............................................603</br>
yield from com futures, tasks e corrotinas.................................................604</br>
Fazendo download com asyncio e aiohttp......................................................605</br>
Dando voltas em chamadas bloqueantes........................................................ 610</br>
Melhorando o script para download com asyncio ......................................... 612</br>
Usando asyncio.as_completed.................................................................. 613</br>
Usando um executor para evitar bloqueio do loop de eventos.................... 619</br>
De callbacks a futures e corrotinas ................................................................ 620</br>
Fazendo várias requisições para cada download........................................623</br>
Escrevendo servidores com asyncio .............................................................. 626</br>
Um servidor TCP com asyncio ................................................................. 627</br>
Um servidor web com aiohttp .................................................................. 632</br>
Clientes mais inteligentes para melhorar a concorrência ............................636</br>
Resumo do capítulo ...................................................................................... 637</br>
Leituras complementares...............................................................................638</br>
</br>
**Parte VI ■ Metaprogramação ........................................................................... 643**</br>
**Capítulo 19 ■ Atributos dinâmicos e propriedades ............................................................644**</br>
Processando dados com atributos dinâmicos................................................. 645</br>
Explorando dados JSON ou similares com atributos dinâmicos................. 647</br>
O problema do nome de atributo inválido ................................................. 651</br>
Criação flexível de objetos com __new__.................................................. 652</br>
Reestruturando o feed da OSCON com shelve ..........................................654</br>
Recuperação de registros relacionados usando propriedades...................... 658</br>
Usando uma propriedade para validação de atributo......................................665</br>
LineItem tomada #1: classe para um item de um pedido ...........................665</br>
LineItem tomada #2: uma propriedade com validação ..............................666</br>
Uma visão apropriada das propriedades.........................................................667</br>
Propriedades encobrem atributos de instância........................................... 669</br>
Documentação de propriedades................................................................672</br>
Implementando uma fábrica de propriedades.................................................673</br>
Tratando a remoção de atributos ................................................................... 676</br>
Atributos e funções essenciais para tratamento de atributos...........................677</br>
Atributos especiais que afetam o tratamento de atributos..........................677</br>
Funções embutidas para tratamento de atributos ...................................... 678</br>
Métodos especiais para tratamento de atributos........................................ 679</br>
Resumo do capítulo ...................................................................................... 681</br>
Leituras complementares............................................................................... 681</br>
</br>
**Capítulo 20 ■ Descritores de atributos..............................................................................687**</br>
Exemplo de descritor: validação de atributos .................................................687</br>
LineItem tomada #3: um descritor simples ...............................................688</br>
LineItem tomada #4: nomes automáticos para atributos de armazenagem. 693</br>
LineItem tomada #5: um novo tipo descritor ............................................700</br>
Descritores dominantes e não dominantes..................................................... 703</br>
Descritor dominante ................................................................................ 705</br>
Descritor dominante sem __get__............................................................ 706</br>
Descritor não dominante .......................................................................... 707</br>
Sobrescrevendo um descritor na classe...................................................... 709</br>
Métodos são descritores................................................................................ 709</br>
Dicas para uso de descritores ........................................................................ 712</br>
Docstring de descritores e controle de remoção.............................................. 714</br>
Resumo do capítulo ...................................................................................... 715</br>
Leituras complementares............................................................................... 716</br>
</br>
**Capítulo 21 ■ Metaprogramação com classes.................................................................... 718**</br>
Uma fábrica de classes .................................................................................. 719</br>
Um decorador de classe para personalizar descritores ....................................722</br>
O que acontece quando: tempo de importação versus tempo de execução.......725</br>
Exercícios dos instantes de avaliação ........................................................726</br>
Básico sobre metaclasses...............................................................................730</br>
Exercício do instante de avaliação de metaclasses...................................... 732</br>
Uma metaclasse para personalizar descritores................................................736</br>
Método especial __prepare__ de metaclasse..................................................738</br>
Classes como objetos .................................................................................... 741</br>
Resumo do capítulo ...................................................................................... 742</br>
Leituras complementares............................................................................... 743</br>
Posfácio.......................................................................................................................... 747</br>
Leituras complementares............................................................................... 749</br>
</br>
**Apêndice A ■ Scripts auxiliares......................................................................................... 751**</br>
Capítulo 3: teste de desempenho do operador in ............................................ 751</br>
Capítulo 3: comparar padrões de bits de hashes............................................. 754</br>
Capítulo 9: uso de RAM com e sem __slots__............................................... 754</br>
Capítulo 14: script isis2json.py para conversão de banco de dados.................. 755</br>
Capítulo 16: simulação de eventos discretos para a frota de táxis.................... 761</br>
Capítulo 17: Exemplos com criptografia......................................................... 766</br>
Capítulo 17: exemplos de cliente HTTP para flags2........................................ 769</br>
Capítulo 19: Scripts e testes para agenda da OSCON..................................... 775</br>
Jargão de Python ............................................................................................................ 781</br>
Sobre o autor .................................................................................................................. 798</br>
Colofão ........................................................................................................................... 799</br>
