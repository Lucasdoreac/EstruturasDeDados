"""
Implementação de Pilhas em Python
Autor: Lucas Dórea Cardoso e Deivid Cerqueira - UDF Ciência da Computação
"""

class PilhaArray:
    """
    Implementação de uma pilha usando um array (lista em Python).
    A pilha segue o princípio LIFO (Last In, First Out).
    """
    def __init__(self, capacidade=10):
        """
        Inicializa uma pilha vazia com a capacidade especificada.
        
        Args:
            capacidade (int, opcional): Capacidade máxima da pilha. Padrão é 10.
        """
        self.capacidade = capacidade
        self.array = [None] * capacidade
        self.topo = -1  # Índice do topo da pilha (-1 indica pilha vazia)
    
    def esta_vazia(self):
        """
        Verifica se a pilha está vazia.
        
        Returns:
            bool: True se a pilha estiver vazia, False caso contrário.
        """
        return self.topo == -1
    
    def esta_cheia(self):
        """
        Verifica se a pilha está cheia.
        
        Returns:
            bool: True se a pilha estiver cheia, False caso contrário.
        """
        return self.topo == self.capacidade - 1
    
    def tamanho(self):
        """
        Retorna o número de elementos na pilha.
        
        Returns:
            int: Número de elementos na pilha.
        """
        return self.topo + 1
    
    def empilhar(self, item):
        """
        Insere um elemento no topo da pilha.
        
        Args:
            item: O elemento a ser inserido.
        
        Raises:
            Exception: Se a pilha estiver cheia.
        """
        if self.esta_cheia():
            raise Exception("Erro: Pilha cheia")
        
        self.topo += 1
        self.array[self.topo] = item
    
    def desempilhar(self):
        """
        Remove e retorna o elemento do topo da pilha.
        
        Returns:
            O elemento removido do topo.
        
        Raises:
            Exception: Se a pilha estiver vazia.
        """
        if self.esta_vazia():
            raise Exception("Erro: Pilha vazia")
        
        item = self.array[self.topo]
        self.array[self.topo] = None  # Remove a referência para ajudar o GC
        self.topo -= 1
        return item
    
    def topo_pilha(self):
        """
        Retorna o elemento do topo da pilha sem removê-lo.
        
        Returns:
            O elemento do topo da pilha.
        
        Raises:
            Exception: Se a pilha estiver vazia.
        """
        if self.esta_vazia():
            raise Exception("Erro: Pilha vazia")
        
        return self.array[self.topo]
    
    def __str__(self):
        """
        Retorna uma representação em string da pilha.
        
        Returns:
            str: Uma representação da pilha.
        """
        if self.esta_vazia():
            return "Pilha vazia"
        
        elementos = [str(self.array[i]) for i in range(self.topo + 1)]
        return "Topo -> " + " -> ".join(reversed(elementos))


class No:
    """
    Classe que representa um nó na implementação da pilha como lista encadeada.
    """
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class PilhaEncadeada:
    """
    Implementação de uma pilha usando uma lista encadeada.
    A pilha segue o princípio LIFO (Last In, First Out).
    """
    def __init__(self):
        """
        Inicializa uma pilha vazia.
        """
        self.topo = None  # Referência para o nó no topo da pilha
        self._tamanho = 0  # Contador para o tamanho da pilha
    
    def esta_vazia(self):
        """
        Verifica se a pilha está vazia.
        
        Returns:
            bool: True se a pilha estiver vazia, False caso contrário.
        """
        return self.topo is None
    
    def tamanho(self):
        """
        Retorna o número de elementos na pilha.
        
        Returns:
            int: Número de elementos na pilha.
        """
        return self._tamanho
    
    def empilhar(self, item):
        """
        Insere um elemento no topo da pilha.
        
        Args:
            item: O elemento a ser inserido.
        """
        novo_no = No(item)
        novo_no.proximo = self.topo
        self.topo = novo_no
        self._tamanho += 1
    
    def desempilhar(self):
        """
        Remove e retorna o elemento do topo da pilha.
        
        Returns:
            O elemento removido do topo.
        
        Raises:
            Exception: Se a pilha estiver vazia.
        """
        if self.esta_vazia():
            raise Exception("Erro: Pilha vazia")
        
        item = self.topo.valor
        self.topo = self.topo.proximo
        self._tamanho -= 1
        return item
    
    def topo_pilha(self):
        """
        Retorna o elemento do topo da pilha sem removê-lo.
        
        Returns:
            O elemento do topo da pilha.
        
        Raises:
            Exception: Se a pilha estiver vazia.
        """
        if self.esta_vazia():
            raise Exception("Erro: Pilha vazia")
        
        return self.topo.valor
    
    def __str__(self):
        """
        Retorna uma representação em string da pilha.
        
        Returns:
            str: Uma representação da pilha.
        """
        if self.esta_vazia():
            return "Pilha vazia"
        
        elementos = []
        atual = self.topo
        
        while atual is not None:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        
        return "Topo -> " + " -> ".join(elementos)


# Exemplo de uso - Verificação de expressões com parênteses balanceados
def verificar_parenteses(expressao):
    """
    Verifica se uma expressão tem parênteses, colchetes e chaves balanceados.
    
    Args:
        expressao (str): A expressão a ser verificada.
    
    Returns:
        bool: True se os parênteses estiverem balanceados, False caso contrário.
    """
    pilha = PilhaEncadeada()
    
    # Dicionário com os pares de abertura e fechamento
    pares = {')': '(', ']': '[', '}': '{'}
    
    for char in expressao:
        # Se for um símbolo de abertura, empilha
        if char in '([{':
            pilha.empilhar(char)
        
        # Se for um símbolo de fechamento
        elif char in ')]}':
            # Se a pilha estiver vazia, não há correspondência
            if pilha.esta_vazia():
                return False
            
            # Desempilha e verifica se corresponde ao símbolo de fechamento
            topo = pilha.desempilhar()
            if topo != pares[char]:
                return False
    
    # A expressão está balanceada se a pilha estiver vazia ao final
    return pilha.esta_vazia()


# Exemplo de uso - Conversão de decimal para binário
def decimal_para_binario(numero):
    """
    Converte um número decimal para binário usando uma pilha.
    
    Args:
        numero (int): O número decimal a ser convertido.
    
    Returns:
        str: A representação binária do número.
    """
    if numero == 0:
        return "0"
    
    pilha = PilhaArray()
    
    while numero > 0:
        resto = numero % 2
        pilha.empilhar(resto)
        numero //= 2
    
    # Desempilha para formar o número binário
    binario = ""
    while not pilha.esta_vazia():
        binario += str(pilha.desempilhar())
    
    return binario


# Demonstração das implementações
if __name__ == "__main__":
    print("Demonstração da Pilha com Array:")
    pilha_array = PilhaArray(5)
    
    print("Empilhando elementos...")
    for i in range(1, 6):
        pilha_array.empilhar(i)
        print(f"Após empilhar {i}: {pilha_array}")
    
    print("\nDesempilhando elementos...")
    while not pilha_array.esta_vazia():
        item = pilha_array.desempilhar()
        print(f"Desempilhado: {item}, Pilha atual: {pilha_array}")
    
    print("\nDemonstração da Pilha com Lista Encadeada:")
    pilha_encadeada = PilhaEncadeada()
    
    print("Empilhando elementos...")
    for i in range(1, 6):
        pilha_encadeada.empilhar(i)
        print(f"Após empilhar {i}: {pilha_encadeada}")
    
    print("\nDesempilhando elementos...")
    while not pilha_encadeada.esta_vazia():
        item = pilha_encadeada.desempilhar()
        print(f"Desempilhado: {item}, Pilha atual: {pilha_encadeada}")
    
    print("\nExemplo: Verificação de parênteses balanceados")
    expressoes = [
        "(1 + 2) * 3",
        "[(1 + 2) * (3 - 4)]",
        "{[()]}",
        "((1 + 2)",
        "(1 + 2))",
        "[(])"
    ]
    
    for expr in expressoes:
        resultado = "balanceada" if verificar_parenteses(expr) else "desbalanceada"
        print(f"A expressão '{expr}' está {resultado}")
    
    print("\nExemplo: Conversão de decimal para binário")
    numeros = [0, 2, 5, 10, 42, 255]
    
    for num in numeros:
        binario = decimal_para_binario(num)
        print(f"Decimal: {num} -> Binário: {binario}")
