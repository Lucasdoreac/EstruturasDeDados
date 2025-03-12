# Definição e Importância das Estruturas de Dados

## Estruturas de Dados Lineares vs. Não Lineares

### Estruturas Lineares
Nas estruturas de dados lineares, os elementos são organizados em sequência, onde cada elemento tem um predecessor e um sucessor (exceto o primeiro e o último elemento).

**Exemplos:**
1. **Listas**: Coleção ordenada de elementos do mesmo tipo.
2. **Pilhas**: Estrutura LIFO (Last In, First Out) onde o último elemento adicionado é o primeiro a ser removido.
3. **Filas**: Estrutura FIFO (First In, First Out) onde o primeiro elemento adicionado é o primeiro a ser removido.
4. **Arrays**: Estrutura que armazena elementos do mesmo tipo com índices numéricos.
5. **Listas Ligadas**: Coleção de nós onde cada nó contém um valor e uma referência para o próximo nó.

### Estruturas Não Lineares
Nas estruturas de dados não lineares, os elementos são organizados de forma não sequencial, onde um elemento pode estar conectado a vários outros elementos.

**Exemplos:**
1. **Árvores**: Estrutura hierárquica onde os elementos estão organizados em nós com um nó raiz.
   - Árvores Binárias: Cada nó tem no máximo dois filhos.
   - Árvores AVL: Árvores binárias de busca balanceadas.
   - Árvores B: Árvores balanceadas usadas em sistemas de banco de dados.

2. **Grafos**: Estrutura que consiste em um conjunto de vértices (nós) e um conjunto de arestas (ligações).
   - Grafos Direcionados: As arestas têm uma direção.
   - Grafos Não Direcionados: As arestas não têm direção.

3. **Tabelas Hash**: Estrutura que mapeia chaves para valores usando uma função hash.

## Impacto das Estruturas de Dados no Desempenho de Programas

A escolha da estrutura de dados correta é crucial para o desempenho de um programa. Abaixo, listamos os principais impactos:

### 1. Complexidade Temporal
A eficiência dos algoritmos é frequentemente medida pela notação Big O, que descreve o comportamento de um algoritmo em termos de seu tempo de execução em relação ao tamanho da entrada.

Diferentes estruturas de dados têm diferentes tempos de complexidade para operações comuns:

| Estrutura de Dados | Acesso | Busca | Inserção | Deleção |
|-------------------|--------|-------|---------|---------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Lista Ligada | O(n) | O(n) | O(1) | O(1) |
| Pilha | O(n) | O(n) | O(1) | O(1) |
| Fila | O(n) | O(n) | O(1) | O(1) |
| Tabela Hash | N/A | O(1)* | O(1)* | O(1)* |
| Árvore Binária | O(n) | O(n) | O(n) | O(n) |
| Árvore Binária de Busca | O(n) | O(n) | O(n) | O(n) |
| Árvore AVL | O(log n) | O(log n) | O(log n) | O(log n) |

*Complexidade média, pode ser O(n) no pior caso.

### 2. Complexidade Espacial
Além do tempo, também é importante considerar a quantidade de memória que uma estrutura de dados consome.

- **Arrays** têm um uso de memória fixo e eficiente, mas podem desperdiçar espaço se muitas posições ficarem vazias.
- **Listas Ligadas** usam mais memória devido às referências, mas são mais flexíveis em termos de alocação dinâmica.
- **Tabelas Hash** podem usar muita memória para evitar colisões.

### 3. Facilidade de Implementação
Estruturas mais simples como arrays são mais fáceis de implementar, enquanto estruturas como árvores AVL são mais complexas.

### 4. Adaptabilidade
Algumas estruturas são mais adaptáveis a mudanças nos requisitos:
- **Listas Ligadas** são boas para inserções e deleções frequentes.
- **Árvores Balanceadas** mantêm um bom desempenho mesmo com dados muito dinâmicos.

### 5. Casos de Uso Específicos
Algumas estruturas são especializadas para casos de uso específicos:
- **Pilhas** são excelentes para rastreamento de chamadas de função e avaliação de expressões.
- **Filas de Prioridade** são ideais para escalonamento de tarefas.
- **Tabelas Hash** são ótimas para dicionários e conjuntos.

A seleção da estrutura de dados correta pode significar a diferença entre um programa que executa em milissegundos e um que leva horas para completar a mesma tarefa.

---

Por Lucas Dórea Cardoso e Deivid Cerqueira - UDF Ciência da Computação