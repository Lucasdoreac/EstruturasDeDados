# Filas (Queues)

## Definição

Uma fila é uma estrutura de dados linear que segue o princípio FIFO (First In, First Out), onde o primeiro elemento inserido é o primeiro a ser removido. A analogia comum para entender uma fila é uma fila de pessoas esperando em um caixa de banco: a primeira pessoa a entrar na fila é a primeira a ser atendida.

## Características Principais

1. **Princípio FIFO**: First In, First Out (Primeiro a Entrar, Primeiro a Sair).
2. **Acesso Restrito**: Elementos são inseridos no final (traseira) e removidos do início (frente).
3. **Operações Básicas**: `enqueue` (enfileirar) e `dequeue` (desenfileirar).
4. **Implementação**: Pode ser feita usando arrays ou listas encadeadas.

## Operações Básicas

### 1. Enqueue (Enfileirar)
- Insere um elemento no final da fila.
- Em uma implementação com array, isso envolve incrementar o índice da traseira e inserir o elemento.
- Em uma implementação com lista encadeada, isso envolve criar um novo nó e fazê-lo ser o próximo nó do último nó atual.

### 2. Dequeue (Desenfileirar)
- Remove o elemento do início da fila.
- Em uma implementação com array, isso envolve obter o elemento da frente e incrementar o índice da frente.
- Em uma implementação com lista encadeada, isso envolve mover a referência da frente para o próximo nó.

### 3. Front/Peek (Frente/Espiar)
- Retorna o elemento do início da fila sem removê-lo.
- Útil para examinar o próximo elemento a ser removido.

### 4. isEmpty (Está Vazia)
- Verifica se a fila está vazia.
- Uma fila vazia não tem elementos para remover.

### 5. isFull (Está Cheia)
- Verifica se a fila está cheia.
- Relevante apenas para implementações com arrays de tamanho fixo.

### 6. Size (Tamanho)
- Retorna o número de elementos na fila.

## Complexidade de Tempo

| Operação | Complexidade |
|----------|--------------|
| Enqueue  | O(1)         |
| Dequeue  | O(1)         |
| Front/Peek | O(1)       |
| isEmpty  | O(1)         |
| isFull   | O(1)         |
| Size     | O(1)         |

## Implementações

### 1. Usando Array
- **Vantagens**: Simples, acesso rápido à frente e à traseira.
- **Desvantagens**: Tamanho fixo, possibilidade de desperdício de espaço.
- **Considerações**: Pode usar uma implementação circular para otimizar o uso do espaço.

### 2. Usando Lista Encadeada
- **Vantagens**: Tamanho dinâmico, sem limite de crescimento.
- **Desvantagens**: Overhead de memória para referências.
- **Considerações**: Manter referências tanto para a frente quanto para a traseira da lista para operações eficientes.

### 3. Fila Circular
- **Vantagens**: Uso eficiente do espaço em implementações com array.
- **Desvantagens**: Lógica mais complexa.
- **Considerações**: Usando aritmética modular para lidar com a circularidade.

## Aplicações

1. **Escalonamento de Processos**: Em sistemas operacionais para gerenciar processos prontos para execução.
2. **Gerenciamento de Impressão**: Para controlar a ordem das tarefas de impressão.
3. **Buffer em Transferências de Dados**: Para gerenciar dados que chegam mais rápido do que podem ser processados.
4. **Algoritmos de Busca em Largura (BFS)**: Em grafos para explorar todos os vértices a uma determinada distância antes de avançar.
5. **Gerenciamento de Atendimento**: Em call centers, sistemas de suporte ao cliente.
6. **Cache de Dados**: Implementação de estruturas como LRU cache (Least Recently Used).
7. **Simulação de Eventos Discretos**: Para modelar sistemas baseados em eventos.
8. **Agendamento de Tarefas**: Em sistemas distribuídos como Kafka ou RabbitMQ.

## Exemplo de Caso Real: Sistema de Atendimento

Em um sistema de atendimento ao cliente:

1. Os clientes entram na fila de atendimento na ordem de chegada.
2. O próximo cliente a ser atendido é sempre o que está esperando há mais tempo.
3. Novos clientes sempre entram no final da fila.

## Variações

### 1. Fila de Prioridade (Priority Queue)
- Os elementos são ordenados com base em uma prioridade atribuída.
- O elemento de maior prioridade é retirado primeiro, independentemente da ordem de inserção.
- Implementado frequentemente usando heaps.

### 2. Deque (Double-ended Queue)
- Permite inserções e remoções em ambas as extremidades (início e fim).
- Combina propriedades de pilhas e filas.

### 3. Fila Circular
- Implementação otimizada usando um array onde o final "envolve" de volta ao início.
- Evita a necessidade de reorganizar os elementos após as operações de dequeue.

### 4. Fila Bloqueante (Blocking Queue)
- Usada em computação concorrente.
- Operações de enqueue e dequeue são bloqueadas quando a fila está cheia ou vazia, respectivamente.

## Limitações

1. **Acesso Restrito**: Não é possível acessar elementos no meio da fila sem remover os elementos na frente.
2. **Sem Busca Eficiente**: Para encontrar um elemento específico, pode ser necessário desenfileirar vários elementos.
3. **Tamanho Fixo** (para implementações com arrays): Pode levar a estouro ou desperdício de espaço.

---

Por Lucas Dórea Cardoso e Deivid Cerqueira - UDF Ciência da Computação