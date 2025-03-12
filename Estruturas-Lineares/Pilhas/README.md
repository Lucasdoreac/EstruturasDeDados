# Pilhas (Stacks)

## Definição

Uma pilha é uma estrutura de dados linear que segue o princípio LIFO (Last In, First Out), onde o último elemento inserido é o primeiro a ser removido. A analogia comum para entender uma pilha é uma pilha de pratos: o último prato colocado é o primeiro a ser retirado.

## Características Principais

1. **Princípio LIFO**: Last In, First Out (Último a Entrar, Primeiro a Sair).
2. **Acesso Restrito**: Elementos só podem ser inseridos e removidos pelo topo da pilha.
3. **Operações Básicas**: `push` (inserir) e `pop` (remover).
4. **Implementação**: Pode ser feita usando arrays ou listas encadeadas.

## Operações Básicas

### 1. Push (Empilhar)
- Insere um elemento no topo da pilha.
- Em uma implementação com array, isso envolve incrementar o índice do topo e inserir o elemento.
- Em uma implementação com lista encadeada, isso envolve criar um novo nó e fazê-lo apontar para o topo atual.

### 2. Pop (Desempilhar)
- Remove o elemento do topo da pilha.
- Em uma implementação com array, isso envolve obter o elemento do topo e decrementar o índice do topo.
- Em uma implementação com lista encadeada, isso envolve mover a referência do topo para o próximo nó.

### 3. Peek (Espiar)
- Retorna o elemento do topo da pilha sem removê-lo.
- Útil para examinar o próximo elemento a ser removido.

### 4. isEmpty (Está Vazia)
- Verifica se a pilha está vazia.
- Uma pilha vazia não tem elementos para remover.

### 5. isFull (Está Cheia)
- Verifica se a pilha está cheia.
- Relevante apenas para implementações com arrays de tamanho fixo.

### 6. Size (Tamanho)
- Retorna o número de elementos na pilha.

## Complexidade de Tempo

| Operação | Complexidade |
|----------|--------------|
| Push     | O(1)         |
| Pop      | O(1)         |
| Peek     | O(1)         |
| isEmpty  | O(1)         |
| isFull   | O(1)         |
| Size     | O(1)         |

## Implementações

### 1. Usando Array
- **Vantagens**: Simples, acesso rápido ao topo.
- **Desvantagens**: Tamanho fixo, possibilidade de estouro.
- **Considerações**: Precisa manter uma variável para rastrear o índice do topo.

### 2. Usando Lista Encadeada
- **Vantagens**: Tamanho dinâmico, sem limite de crescimento.
- **Desvantagens**: Overhead de memória para referências.
- **Considerações**: A inserção e remoção são feitas apenas em um extremo (a cabeça da lista).

## Aplicações

1. **Avaliação de Expressões**: Conversão infixa para pós-fixa, avaliação de expressões pós-fixas.
2. **Gerenciamento de Memória**: Rastreamento de chamadas de funções (call stack).
3. **Operações "Desfazer/Refazer"**: Em editores de texto e aplicativos de desenho.
4. **Navegação em Histórico**: Botões "Voltar" e "Avançar" em navegadores web.
5. **Verificação de Parênteses Balanceados**: Verificar se expressões têm parênteses devidamente balanceados.
6. **Algoritmos de Backtracking**: Como busca em profundidade (DFS) em grafos.
7. **Conversão de Números**: Convertendo entre diferentes bases numéricas.
8. **Algoritmos de Ordenação**: Como o QuickSort.

## Exemplo de Caso Real: Navegador Web

Os navegadores web usam pilhas para rastrear o histórico de navegação:

1. Cada vez que você visita uma nova página, o URL é empilhado na pilha de histórico.
2. Quando você clica no botão "Voltar", o navegador desempilha o URL atual e navega para o URL anterior na pilha.
3. Uma segunda pilha rastreia as páginas acessadas com o botão "Voltar" para habilitar o botão "Avançar".

## Limitações

1. **Acesso Restrito**: Não é possível acessar elementos no meio da pilha sem remover os elementos acima.
2. **Sem Busca Eficiente**: Para encontrar um elemento específico, pode ser necessário desempilhar vários elementos.
3. **Tamanho Fixo** (para implementações com arrays): Pode levar a estouro ou desperdício de espaço.

## Variações

1. **Pilha Dupla**: Uma estrutura que gerencia duas pilhas usando um único array.
2. **Pilha com Mínimo/Máximo**: Uma pilha que mantém controle do elemento mínimo/máximo em tempo constante.
3. **Pilha Circular**: Uma implementação que reutiliza espaço em um array quando elementos são desempilhados.

---

Por Lucas Dórea Cardoso e Deivid Cerqueira - UDF Ciência da Computação