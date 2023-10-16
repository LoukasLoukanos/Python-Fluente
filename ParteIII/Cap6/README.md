## **Padrões de Projeto**
Em Python, existem duas abordagens principais para escrever código estruturado e reutilizável que podem determinar quando se deve usar funções e quando usar classes, a escolha depende do problema e das necessidades do código:

### ***Padrão de Projeto Baseado em Função (Strategy pattern function-based implementation):***
Se concentram em funções independentes e reutilizáveis (é mais modular e reutilizável).

  - Exemplo simples:
    ```python
    def saudacao(nome):
        return "Olá, " + nome + "!"

    def despedida(nome):
        return "Tchau, " + nome + "!"

    def processar_saudacao(funcao_saudacao, nome):
        return funcao_saudacao(nome)

    nome_pessoa = "Maria"
    print(processar_saudacao(saudacao, nome_pessoa))
    print(processar_saudacao(despedida, nome_pessoa))

    ```

  - Exemplo avançado:
    ```python
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    def calcular(operacao, a, b):
        return operacao(a, b)

    resultado = calcular(somar, 5, 3)
    print(resultado)

    resultado = calcular(subtrair, 10, 7)
    print(resultado)

    ```

### ***Padrão de Projeto Clássico Baseado em Classe (Strategy pattern clássic implementation):***
Encapsulam dados e comportamentos em um único objeto (é mais voltada para a criação de objetos).

  - Exemplo simples:
    ```python
    class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    retangulo1 = Retangulo(5, 3)
    print(retangulo1.calcular_area())

    ```

  - Exemplo avançado:
    ```python
    class Animal:
        def fazer_som(self):
            pass
          
    class Cachorro(Animal):
        def fazer_som(self):
            print("Au au!")

    class Gato(Animal):
        def fazer_som(self):
            print("Miau!")

    animais = [Cachorro(), Gato()]

    for animal in animais:
        animal.fazer_som()

    ```

<hr>

*Existem outros padrões de programação em Python além dos baseados em função e em classe. Alguns exemplos incluem:*

#### ***Programação Orientada a Eventos:***
Nesse padrão, o programa é composto por uma série de eventos que ocorrem em resposta a ações do usuário ou do sistema. A biblioteca padrão de Python oferece suporte para a programação orientada a eventos através do módulo "asyncio":

  - Exemplo simples:
    ```python
    from tkinter import Tk, Button

    def botao_clicado():
        print("Botão foi clicado!")

    janela = Tk()
    botao = Button(janela, text="Clique aqui", command=botao_clicado)
    botao.pack()
    janela.mainloop()

    ```

  - Exemplo avançado:
    ```python
    import tkinter as tk

    class Aplicacao(tk.Tk):
        def __init__(self):
            super().__init__()
            self.botao = tk.Button(self, text="Clique aqui")
            self.botao.bind("<Button-1>", self.botao_clicado)
            self.botao.pack()

        def botao_clicado(self, event):
            print("Botão foi clicado!")

    app = Aplicacao()
    app.mainloop()

    ```

#### ***Programação Funcional:*** 
Nesse padrão, as funções são tratadas como valores e podem ser passadas como argumentos para outras funções. Python suporta programação funcional através de recursos como funções lambda, map(), filter() e reduce().

  - Exemplo simples:
    ```python
    numeros = [1, 2, 3, 4, 5]

    dobro = list(map(lambda x: x * 2, numeros))
    print(dobro)

    soma = reduce(lambda x, y: x + y, numeros)
    print(soma)

    ```

  - Exemplo avançado:
    ```python
    from functools import reduce

    numeros = [1, 2, 3, 4, 5]

    dobro_pares = list(filter(lambda x: x % 2 == 0, map(lambda x: x * 2, numeros)))
    print(dobro_pares)

    soma = reduce(lambda x, y: x + y, numeros, 0)
    print(soma)

    ```

#### ***Programação Reativa:***
Esse padrão é semelhante à programação orientada a eventos, mas em vez de lidar com eventos de forma imperativa, ele utiliza fluxos de dados reativos. A biblioteca "RxPY" fornece suporte para programação reativa em Python.

  - Exemplo simples:
    ```python
    import rx

    def observer(evento):
        print("Evento recebido:", evento)

    observavel = rx.from_iterable([1, 2, 3, 4, 5])
    observavel.subscribe(observer)

    ```

  - Exemplo avançado:
    ```python
    import rx
    from rx.subject import Subject
    
    subject = Subject()
    
    def observer1(evento):
        print("Observer 1:", evento)
    
    def observer2(evento):
        print("Observer 2:", evento)
    
    subject.subscribe(observer1)
    subject.on_next("Evento 1")
    subject.subscribe(observer2)
    subject.on_next("Evento 2")
    
    ```

#### ***Programação Assíncrona:***
Esse padrão é baseado no uso de corrotinas, que são funções que podem ser pausadas e retomadas posteriormente. A programação assíncrona permite que múltiplas tarefas sejam executadas simultaneamente, o que pode melhorar o desempenho de aplicativos. Python suporta programação assíncrona através do módulo "asyncio".

  - Exemplo simples:
    ```python
    import asyncio

    async def tarefa_demorada():
        print("Iniciando tarefa...")
        await asyncio.sleep(2)
        print("Tarefa concluída!")

    async def main():
        print("Executando tarefa assíncrona...")
        await tarefa_demorada()
        print("Tarefa assíncrona concluída!")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

    ```

  - Exemplo avançado:
    ```python
    import asyncio
    
    async def tarefa_demorada():
        print("Iniciando tarefa...")
        await asyncio.sleep(2)
        print("Tarefa concluída!")
        return "Resultado da tarefa"
    
    async def main():
        print("Executando tarefa assíncrona...")
        resultado = await tarefa_demorada()
        print("Tarefa assíncrona concluída! Resultado:", resultado)
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    
    ```

#### ***Padrão Command:***

O padrão de projeto Command é um padrão comportamental que encapsula uma solicitação como um objeto, permitindo que você parametrize clientes com diferentes solicitações, enfileire ou registre solicitações e implemente operações desfazer. Em Python, o padrão Command pode ser implementado da seguinte maneira:

1. Crie uma classe abstrata chamada Command que define a interface para todos os comandos concretos:
    ```python
    from abc import ABC, abstractmethod
    
    class Command(ABC):
        @abstractmethod
        def execute(self):
            pass
    ```
    
2. Implemente as classes concretas de comandos, que herdam da classe Command e implementam o método execute():
    ```python
    class ComandoConcreto1(Command):
        def execute(self):
            # Lógica específica do comando 1
            pass
    
    class ComandoConcreto2(Command):
        def execute(self):
            # Lógica específica do comando 2
            pass
    ```

3. Crie uma classe chamada Invoker que invoca os comandos:
    ```python
    class Invoker:
        def __init__(self):
            self._comando = None
    
        def set_comando(self, comando):
            self._comando = comando
    
        def executar_comando(self):
            self._comando.execute()
    ```

4. Utilize o padrão Command criando instâncias dos comandos e configurando o invocador:
    ```python
    comando1 = ComandoConcreto1()
    comando2 = ComandoConcreto2()
    
    invocador = Invoker()
    invocador.set_comando(comando1)
    invocador.executar_comando()
    
    invocador.set_comando(comando2)
    invocador.executar_comando()
    ```

Dessa forma, você pode criar diferentes comandos e configurá-los no invocador para que eles sejam executados quando necessário. O padrão Command ajuda a separar o objeto que emite o comando do objeto que o executa, permitindo maior flexibilidade e extensibilidade no design do seu código.