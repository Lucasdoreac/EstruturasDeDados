"""
Exemplo de alocação dinâmica de memória em Python
Autor: Lucas Dórea Cardoso e Deivid Cerqueira - UDF Ciência da Computação
"""

import sys

def demonstracao_alocacao_dinamica():
    """
    Demonstração de alocação dinâmica de memória em Python.
    
    Em Python, a alocação de memória é principalmente dinâmica e gerenciada
    automaticamente pelo interpretador. Este exemplo demonstra como diferentes
    estruturas em Python usam alocação dinâmica.
    """
    print("Demonstração de Alocação Dinâmica em Python")
    print("-" * 50)
    
    # 1. Listas dinâmicas
    print("1. Listas dinâmicas:")
    lista = []
    print(f"Lista vazia - Tamanho: {len(lista)}, Memória aproximada: {sys.getsizeof(lista)} bytes")
    
    # Adicionando elementos dinamicamente
    for i in range(10):
        lista.append(i)
        print(f"Após adicionar {i}: Tamanho: {len(lista)}, Memória aproximada: {sys.getsizeof(lista)} bytes")
    
    print("\nObserve como a memória alocada para a lista cresce à medida que novos elementos são adicionados.")
    print("Python gerencia isso automaticamente, realocando memória conforme necessário.")
    
    # 2. Dicionários - Estrutura de dados dinâmica
    print("\n2. Dicionários dinâmicos:")
    dicionario = {}
    print(f"Dicionário vazio - Tamanho: {len(dicionario)}, Memória aproximada: {sys.getsizeof(dicionario)} bytes")
    
    for i in range(5):
        dicionario[f"chave_{i}"] = f"valor_{i}"
        print(f"Após adicionar item {i}: Tamanho: {len(dicionario)}, Memória aproximada: {sys.getsizeof(dicionario)} bytes")
    
    # 3. Criação dinâmica de objetos
    print("\n3. Criação dinâmica de objetos:")
    
    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade
    
    # Criando uma lista dinâmica de objetos
    pessoas = []
    nomes = ["Alice", "Bob", "Carlos", "Diana", "Eduardo"]
    
    for i, nome in enumerate(nomes):
        # Cria um novo objeto dinamicamente
        nova_pessoa = Pessoa(nome, 20 + i)
        pessoas.append(nova_pessoa)
        print(f"Adicionada pessoa: {nova_pessoa.nome}, {nova_pessoa.idade} anos")
    
    print(f"Lista contém {len(pessoas)} objetos Pessoa")
    
    # 4. Lista encadeada simples com alocação dinâmica
    print("\n4. Implementação de uma Lista Encadeada com alocação dinâmica:")
    
    class No:
        def __init__(self, valor):
            self.valor = valor
            self.proximo = None
    
    class ListaEncadeada:
        def __init__(self):
            self.cabeca = None
            self.tamanho = 0
        
        def adicionar(self, valor):
            novo_no = No(valor)  # Aloca dinamicamente um novo nó
            if not self.cabeca:
                self.cabeca = novo_no
            else:
                atual = self.cabeca
                while atual.proximo:
                    atual = atual.proximo
                atual.proximo = novo_no
            self.tamanho += 1
            print(f"Adicionado nó com valor: {valor}")
        
        def imprimir(self):
            if not self.cabeca:
                return "Lista vazia"
            
            valores = []
            atual = self.cabeca
            while atual:
                valores.append(str(atual.valor))
                atual = atual.proximo
            
            return " -> ".join(valores)
    
    # Demonstração da lista encadeada
    lista_enc = ListaEncadeada()
    print("Lista encadeada criada (vazia inicialmente)")
    
    # Adicionando elementos dinamicamente
    for i in range(1, 6):
        lista_enc.adicionar(i * 10)
    
    print(f"Lista encadeada: {lista_enc.imprimir()}")
    print(f"Tamanho da lista: {lista_enc.tamanho}")
    
    # 5. Removendo referências - demonstrando como o Python libera memória
    print("\n5. Demonstração de desalocação automática:")
    
    # Criando um objeto grande
    print("Criando uma lista grande...")
    lista_grande = list(range(1000000))
    print(f"Lista grande criada, tamanho aproximado: {sys.getsizeof(lista_grande)} bytes")
    
    # Removendo a referência
    print("Removendo a referência à lista grande...")
    lista_grande = None
    print("Referência removida. O coletor de lixo do Python liberará essa memória automaticamente")
    
    print("\nConclusão:")
    print("Em Python, a alocação e desalocação de memória são gerenciadas automaticamente")
    print("pelo interpretador e seu coletor de lixo. Diferente de linguagens como C/C++,")
    print("não é necessário alocar ou liberar memória explicitamente.")
    print("As estruturas de dados em Python crescem e diminuem dinamicamente conforme")
    print("necessário, facilitando o desenvolvimento mas potencialmente ocultando")
    print("detalhes importantes sobre gerenciamento de memória.")

if __name__ == "__main__":
    demonstracao_alocacao_dinamica()
