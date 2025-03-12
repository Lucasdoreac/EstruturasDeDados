"""
Exemplo de comparação de performance entre diferentes estruturas de dados
Autor: Lucas Dórea Cardoso e Deivid Cerqueira - UDF Ciência da Computação
"""

import time
import random

def busca_lista(lista, elemento):
    """Busca linear em uma lista não ordenada"""
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def busca_lista_ordenada(lista, elemento):
    """Busca binária em uma lista ordenada"""
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] > elemento:
            fim = meio - 1
        else:
            inicio = meio + 1
    return -1

def busca_dicionario(dicionario, chave):
    """Busca em um dicionário (implementado como tabela hash)"""
    return dicionario.get(chave, -1)

def main():
    # Tamanho dos dados
    tamanho = 10000
    
    # Criando as estruturas de dados
    print(f"Criando estruturas de dados com {tamanho} elementos...")
    
    # Lista não ordenada
    lista_nao_ordenada = list(range(tamanho))
    random.shuffle(lista_nao_ordenada)
    
    # Lista ordenada
    lista_ordenada = list(range(tamanho))
    
    # Dicionário (tabela hash)
    dicionario = {i: i for i in range(tamanho)}
    
    # Elementos para buscar (existentes e não existentes)
    elementos_existentes = [random.randint(0, tamanho-1) for _ in range(1000)]
    elementos_nao_existentes = [random.randint(tamanho, tamanho*2) for _ in range(1000)]
    todos_elementos = elementos_existentes + elementos_nao_existentes
    
    # Teste de busca em lista não ordenada
    print("\nBusca em lista não ordenada:")
    inicio = time.time()
    for elemento in todos_elementos:
        busca_lista(lista_nao_ordenada, elemento)
    fim = time.time()
    print(f"Tempo total: {fim - inicio:.6f} segundos")
    print(f"Tempo médio por busca: {(fim - inicio) / len(todos_elementos):.6f} segundos")
    print(f"Complexidade: O(n) - busca linear")
    
    # Teste de busca em lista ordenada
    print("\nBusca em lista ordenada (busca binária):")
    inicio = time.time()
    for elemento in todos_elementos:
        busca_lista_ordenada(lista_ordenada, elemento)
    fim = time.time()
    print(f"Tempo total: {fim - inicio:.6f} segundos")
    print(f"Tempo médio por busca: {(fim - inicio) / len(todos_elementos):.6f} segundos")
    print(f"Complexidade: O(log n) - busca binária")
    
    # Teste de busca em dicionário
    print("\nBusca em dicionário (tabela hash):")
    inicio = time.time()
    for elemento in todos_elementos:
        busca_dicionario(dicionario, elemento)
    fim = time.time()
    print(f"Tempo total: {fim - inicio:.6f} segundos")
    print(f"Tempo médio por busca: {(fim - inicio) / len(todos_elementos):.6f} segundos")
    print(f"Complexidade: O(1) - acesso direto (caso médio)")
    
    print("\nComparação de performance:")
    print("1. Lista não ordenada - Mais lenta para buscas (O(n))")
    print("2. Lista ordenada - Velocidade intermediária (O(log n))")
    print("3. Dicionário - Mais rápido para buscas (O(1) no caso médio)")
    print("\nEste exemplo demonstra como a escolha da estrutura de dados correta")
    print("pode ter um impacto significativo no desempenho do programa.")

if __name__ == "__main__":
    main()
