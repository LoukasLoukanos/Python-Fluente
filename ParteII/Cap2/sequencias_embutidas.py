
'''
╔═══════════════════════════════════════════════════════╦═════════════════════════════════╦════════════════════════════════╗
║................SEQUÊNCIAS EMBUTIDAS...................║..MUTÁVEIS("subclasse/herança")..║..IMUTÁVEIS("superclasse/pai")..║
╠═══════════════════════════════════════════════════════╬═════════════════════════════════╬════════════════════════════════╣
║SIMPLES (armazenam itens de um só tipo)................║..bytearray, array, memoryview...║............str, bytes..........║
╠═══════════════════════════════════════════════════════╬═════════════════════════════════╬════════════════════════════════╣
║CONTAINER (armazenam itens de tipos diferentes)........║...........list, deque...........║..............tuple.............║
╚═══════════════════════════════════════════════════════╩═════════════════════════════════╩════════════════════════════════╝

SIMPLES:
• Mais compactas, rápidas e fáceis de usar.
• Limitadas ao armazenamento de dados atômicos como números, caracteres e bytes.

CONTAINER:
• Mais flexíveis.
• Não recomendadas para armazenar objetos mutáveis.

→ Como um exemplo, o tipo mais básico de sequência é list, um container mutável.
'''
