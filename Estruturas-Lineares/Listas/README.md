# Listas

## Definição

Uma lista é uma estrutura de dados linear que armazena uma coleção ordenada de elementos. Cada elemento na lista possui uma posição específica, determinada pelo seu índice. Os elementos podem ser de diversos tipos, dependendo da implementação e da linguagem de programação.

## Tipos de Listas

### 1. Lista Sequencial (Array)
- **Implementação**: Elementos armazenados contiguamente na memória.
- **Acesso**: Acesso direto aos elementos via índice (O(1)).
- **Característica**: Tamanho geralmente fixo ou expandido através de realocação.

### 2. Lista Ligada (Linked List)
- **Implementação**: Elementos dispersos na memória, conectados por referências (ponteiros).
- **Tipos**:
  - **Lista Simplesmente Ligada**: Cada nó aponta apenas para o próximo.
  - **Lista Duplamente Ligada**: Cada nó aponta para o próximo e para o anterior.
  - **Lista Circular**: O último nó aponta para o primeiro.
- **Acesso**: Sequencial, começando pela cabeça da lista (O(n)).
- **Característica**: Tamanho dinâmico, facilidade de inserção e remoção.

## Operações Básicas

### 1. Inserção
- **No início**: Adicionar um elemento na primeira posição da lista.
- **No final**: Adicionar um elemento na última posição da lista.
- **Em posição arbitrária**: Adicionar um elemento em uma posição específica da lista.

### 2. Remoção
- **Do início**: Remover o primeiro elemento da lista.
- **Do final**: Remover o último elemento da lista.
- **De posição arbitrária**: Remover um elemento de uma posição específica da lista.

### 3. Acesso
- **Por índice**: Acessar o elemento na posição específica da lista.
- **Sequencial**: Percorrer a lista do início ao fim.

### 4. Busca
- **Por valor**: Encontrar a posição de um elemento específico na lista.
- **Por condição**: Encontrar elementos que satisfaçam uma condição específica.

### 5. Atualização
- **Por índice**: Modificar o valor do elemento em uma posição específica.

## Complexidade de Tempo

### Lista Sequencial (Array)
| Operação | Complexidade |
|----------|--------------|
| Acesso | O(1) |
| Inserção no início | O(n) |
| Inserção no final | O(1)* |
| Inserção em posição arbitrária | O(n) |
| Remoção do início | O(n) |
| Remoção do final | O(1) |
| Remoção de posição arbitrária | O(n) |
| Busca | O(n) |

*Assumindo que há espaço disponível. Se o array precisar ser redimensionado, a complexidade será O(n).

### Lista Ligada
| Operação | Complexidade (Lista Simples) | Complexidade (Lista Dupla) |
|----------|------------------------------|----------------------------|
| Acesso | O(n) | O(n) |
| Inserção no início | O(1) | O(1) |
| Inserção no final | O(n)* | O(1)* |
| Inserção em posição arbitrária | O(n) | O(n) |
| Remoção do início | O(1) | O(1) |
| Remoção do final | O(n) | O(1) |
| Remoção de posição arbitrária | O(n) | O(n) |
| Busca | O(n) | O(n) |

*Assumindo que não temos uma referência para o final da lista. Com uma referência, a inserção no final pode ser O(1).

## Vantagens e Desvantagens

### Listas Sequenciais (Arrays)
**Vantagens**:
- Acesso rápido aos elementos por índice.
- Utilização eficiente da memória cache devido à localidade espacial.
- Implementação simples.

**Desvantagens**:
- Tamanho fixo em muitas implementações.
- Inserção e remoção podem ser custosas devido à necessidade de deslocamento de elementos.
- Desperdício de memória se alocada mais memória do que o necessário.

### Listas Ligadas
**Vantagens**:
- Tamanho dinâmico.
- Inserção e remoção eficientes no início (e no final, para listas duplamente ligadas).
- Sem desperdício de memória para elementos não utilizados.

**Desvantagens**:
- Acesso sequencial aos elementos (não é possível acesso direto por índice).
- Maior consumo de memória devido às referências adicionais.
- Menor eficiência na utilização da memória cache.

## Aplicações Comuns

1. **Implementação de outras estruturas**: Pilhas, filas, deques, etc.
2. **Manipulação de dados dinâmicos**: Quando o tamanho dos dados pode mudar frequentemente.
3. **Implementação de algoritmos**: Como algoritmos de ordenação e busca.
4. **Gerenciamento de memória**: Para controle de blocos livres e alocados.
5. **Histórico de navegação**: Em navegadores da web.
6. **Listas de reprodução**: Em aplicativos de mídia.

---

Por Lucas Dórea Cardoso e Deivid Cerqueira - UDF Ciência da Computação