## **Padrões de Projeto**
Em Python, existem duas abordagens principais para escrever código estruturado e reutilizável que podem determinar quando se deve usar funções e quando usar classes, a escolha depende do problema e das necessidades do código: 

### ***Padrão de Projeto Baseado em Função (Strategy pattern function-based implementation):***
  - Se concentram em funções independentes e reutilizáveis (é mais modular e reutilizável).

### ***Padrão de Projeto Clássico Baseado em Classe (Strategy pattern clássic implementation):***
  - Encapsulam dados e comportamentos em um único objeto (é mais voltada para a criação de objetos).

<hr>

*Existem outros padrões de programação em Python além dos baseados em função e em classe. Alguns exemplos incluem:*

#### ***Programação Orientada a Eventos:***
 - Nesse padrão, o programa é composto por uma série de eventos que ocorrem em resposta a ações do usuário ou do sistema. A biblioteca padrão de Python oferece suporte para a programação orientada a eventos através do módulo "asyncio".

#### ***Programação Funcional:*** 
 - Nesse padrão, as funções são tratadas como valores e podem ser passadas como argumentos para outras funções. Python suporta programação funcional através de recursos como funções lambda, map(), filter() e reduce().

#### ***Programação Reativa:***
 - Esse padrão é semelhante à programação orientada a eventos, mas em vez de lidar com eventos de forma imperativa, ele utiliza fluxos de dados reativos. A biblioteca "RxPY" fornece suporte para programação reativa em Python.

#### ***Programação Assíncrona:***
 - Esse padrão é baseado no uso de corrotinas, que são funções que podem ser pausadas e retomadas posteriormente. A programação assíncrona permite que múltiplas tarefas sejam executadas simultaneamente, o que pode melhorar o desempenho de aplicativos. Python suporta programação assíncrona através do módulo "asyncio".