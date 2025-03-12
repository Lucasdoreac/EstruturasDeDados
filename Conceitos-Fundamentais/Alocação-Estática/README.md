# Alocação Estática de Memória

## Definição

A alocação estática de memória ocorre quando o espaço de memória para variáveis e estruturas de dados é reservado durante a compilação do programa, antes mesmo da execução. O tamanho e o tempo de vida dessas variáveis são determinados em tempo de compilação e permanecem fixos ao longo da execução do programa.

## Características Principais

1. **Tempo de Alocação**: Ocorre em tempo de compilação.
2. **Tamanho**: Fixo e determinado antes da execução do programa.
3. **Tempo de Vida**: Geralmente durante toda a execução do programa (variáveis globais) ou durante a execução do bloco em que são declaradas (variáveis locais).
4. **Localização**: Geralmente armazenadas na seção de dados ou na pilha do programa.
5. **Flexibilidade**: Baixa, pois o tamanho não pode ser alterado durante a execução.

## Tipos de Variáveis com Alocação Estática

1. **Variáveis Globais**: Declaradas fora de qualquer função, existem durante toda a execução do programa.
2. **Variáveis Locais Estáticas**: Declaradas dentro de funções com a palavra-chave `static`, mantêm seu valor entre chamadas de função.
3. **Arrays de Tamanho Fixo**: Declarados com tamanho constante durante a compilação.
4. **Estruturas de Dados de Tamanho Fixo**: Como structs e classes com campos de tamanho fixo.

## Vantagens

1. **Desempenho**: Acesso rápido, pois o compilador conhece a localização exata na memória.
2. **Segurança**: Menos propenso a erros como vazamentos de memória.
3. **Previsibilidade**: Comportamento mais previsível do programa, útil para sistemas embarcados e aplicações críticas.
4. **Eficiência**: Não há sobrecarga de alocação/desalocação em tempo de execução.

## Desvantagens

1. **Inflexibilidade**: Não pode ser redimensionado durante a execução.
2. **Desperdício de Memória**: Pode haver alocação de mais memória do que o necessário.
3. **Limitações**: Não é adequado para dados cujo tamanho só será conhecido durante a execução.

## Quando Usar

1. **Dados de Tamanho Fixo**: Quando o tamanho dos dados é conhecido e não mudará.
2. **Sistemas Embarcados**: Onde recursos são limitados e previsibilidade é crucial.
3. **Aplicações Críticas**: Onde tempo de resposta consistente é necessário.
4. **Estruturas de Tamanho Pequeno**: Quando o overhead de alocação dinâmica não compensa.

## Exemplo Simplificado

Em um programa que processa transações bancárias:
- Uma matriz estática para armazenar as últimas 100 transações é adequada se sempre estamos interessados apenas nas 100 mais recentes.
- Registros de clientes com um número fixo de campos (nome, endereço, etc.) podem ser armazenados em estruturas estáticas.

---

Por Lucas Dórea Cardoso e Deivid Cerqueira - UDF Ciência da Computação