"""
Implementação de Filas em Python
Autor: Lucas Dórea Cardoso e Deivid Cerqueira - UDF Ciência da Computação
"""

class FilaArray:
    """
    Implementação de uma fila usando um array (lista em Python).
    A fila segue o princípio FIFO (First In, First Out).
    """
    def __init__(self, capacidade=10):
        """
        Inicializa uma fila vazia com a capacidade especificada.
        
        Args:
            capacidade (int, opcional): Capacidade máxima da fila. Padrão é 10.
        """
        self.capacidade = capacidade
        self.array = [None] * capacidade
        self.frente = 0  # Índice do primeiro elemento
        self.traseira = -1  # Índice do último elemento
        self._tamanho = 0  # Número de elementos na fila
    
    def esta_vazia(self):
        """
        Verifica se a fila está vazia.
        
        Returns:
            bool: True se a fila estiver vazia, False caso contrário.
        """
        return self._tamanho == 0
    
    def esta_cheia(self):
        """
        Verifica se a fila está cheia.
        
        Returns:
            bool: True se a fila estiver cheia, False caso contrário.
        """
        return self._tamanho == self.capacidade
    
    def tamanho(self):
        """
        Retorna o número de elementos na fila.
        
        Returns:
            int: Número de elementos na fila.
        """
        return self._tamanho
    
    def enfileirar(self, item):
        """
        Insere um elemento no final da fila.
        
        Args:
            item: O elemento a ser inserido.
        
        Raises:
            Exception: Se a fila estiver cheia.
        """
        if self.esta_cheia():
            raise Exception("Erro: Fila cheia")
        
        # Incrementa o índice traseiro de forma circular
        self.traseira = (self.traseira + 1) % self.capacidade
        self.array[self.traseira] = item
        self._tamanho += 1
    
    def desenfileirar(self):
        """
        Remove e retorna o elemento do início da fila.
        
        Returns:
            O elemento removido do início.
        
        Raises:
            Exception: Se a fila estiver vazia.
        """
        if self.esta_vazia():
            raise Exception("Erro: Fila vazia")
        
        item = self.array[self.frente]
        self.array[self.frente] = None  # Remove a referência para ajudar o GC
        
        # Incrementa o índice frontal de forma circular
        self.frente = (self.frente + 1) % self.capacidade
        self._tamanho -= 1
        return item
    
    def frente_fila(self):
        """
        Retorna o elemento do início da fila sem removê-lo.
        
        Returns:
            O elemento do início da fila.
        
        Raises:
            Exception: Se a fila estiver vazia.
        """
        if self.esta_vazia():
            raise Exception("Erro: Fila vazia")
        
        return self.array[self.frente]
    
    def __str__(self):
        """
        Retorna uma representação em string da fila.
        
        Returns:
            str: Uma representação da fila.
        """
        if self.esta_vazia():
            return "Fila vazia"
        
        elementos = []
        idx = self.frente
        for _ in range(self._tamanho):
            elementos.append(str(self.array[idx]))
            idx = (idx + 1) % self.capacidade
        
        return "Frente -> " + " -> ".join(elementos) + " <- Traseira"


class No:
    """
    Classe que representa um nó na implementação da fila como lista encadeada.
    """
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class FilaEncadeada:
    """
    Implementação de uma fila usando uma lista encadeada.
    A fila segue o princípio FIFO (First In, First Out).
    """
    def __init__(self):
        """
        Inicializa uma fila vazia.
        """
        self.frente = None  # Referência para o primeiro nó
        self.traseira = None  # Referência para o último nó
        self._tamanho = 0  # Contador para o tamanho da fila
    
    def esta_vazia(self):
        """
        Verifica se a fila está vazia.
        
        Returns:
            bool: True se a fila estiver vazia, False caso contrário.
        """
        return self.frente is None
    
    def tamanho(self):
        """
        Retorna o número de elementos na fila.
        
        Returns:
            int: Número de elementos na fila.
        """
        return self._tamanho
    
    def enfileirar(self, item):
        """
        Insere um elemento no final da fila.
        
        Args:
            item: O elemento a ser inserido.
        """
        novo_no = No(item)
        
        if self.esta_vazia():
            # Se a fila estiver vazia, o novo nó é tanto a frente quanto a traseira
            self.frente = novo_no
        else:
            # Se não, o novo nó é adicionado após a traseira atual
            self.traseira.proximo = novo_no
        
        # O novo nó se torna a nova traseira
        self.traseira = novo_no
        self._tamanho += 1
    
    def desenfileirar(self):
        """
        Remove e retorna o elemento do início da fila.
        
        Returns:
            O elemento removido do início.
        
        Raises:
            Exception: Se a fila estiver vazia.
        """
        if self.esta_vazia():
            raise Exception("Erro: Fila vazia")
        
        item = self.frente.valor
        
        # Move a referência da frente para o próximo nó
        self.frente = self.frente.proximo
        
        # Se a frente se tornar None, a fila está vazia e a traseira também deve ser None
        if self.frente is None:
            self.traseira = None
        
        self._tamanho -= 1
        return item
    
    def frente_fila(self):
        """
        Retorna o elemento do início da fila sem removê-lo.
        
        Returns:
            O elemento do início da fila.
        
        Raises:
            Exception: Se a fila estiver vazia.
        """
        if self.esta_vazia():
            raise Exception("Erro: Fila vazia")
        
        return self.frente.valor
    
    def __str__(self):
        """
        Retorna uma representação em string da fila.
        
        Returns:
            str: Uma representação da fila.
        """
        if self.esta_vazia():
            return "Fila vazia"
        
        elementos = []
        atual = self.frente
        
        while atual is not None:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        
        return "Frente -> " + " -> ".join(elementos) + " <- Traseira"


# Exemplo de uso - Simulação de atendimento em um banco
class Cliente:
    """
    Classe que representa um cliente para a simulação de banco.
    """
    def __init__(self, id, tempo_atendimento):
        self.id = id
        self.tempo_atendimento = tempo_atendimento
    
    def __str__(self):
        return f"Cliente {self.id} (tempo: {self.tempo_atendimento}min)"


def simular_atendimento_banco(num_clientes, num_caixas):
    """
    Simula o atendimento de clientes em um banco com múltiplos caixas.
    
    Args:
        num_clientes (int): Número de clientes para simular.
        num_caixas (int): Número de caixas disponíveis no banco.
    
    Returns:
        tuple: Um tuplo contendo o tempo total de atendimento e o tempo médio de espera.
    """
    import random
    
    # Criar uma fila de clientes
    fila_clientes = FilaEncadeada()
    
    # Gerar clientes aleatórios
    for i in range(num_clientes):
        tempo_atendimento = random.randint(1, 15)  # Tempo de atendimento entre 1 e 15 minutos
        cliente = Cliente(i+1, tempo_atendimento)
        fila_clientes.enfileirar(cliente)
    
    print(f"Simulando atendimento em um banco com {num_caixas} caixas e {num_clientes} clientes...")
    
    # Inicializar caixas (todos inicialmente livres, valor é o tempo restante de atendimento)
    caixas = [0] * num_caixas
    
    # Estatísticas
    tempo_total = 0
    tempo_espera_total = 0
    clientes_atendidos = 0
    
    # Simular o tempo passando
    while not fila_clientes.esta_vazia() or any(caixa > 0 for caixa in caixas):
        # Decrementar o tempo de atendimento em cada caixa
        for i in range(num_caixas):
            if caixas[i] > 0:
                caixas[i] -= 1
        
        # Atribuir clientes a caixas livres
        for i in range(num_caixas):
            if caixas[i] == 0 and not fila_clientes.esta_vazia():
                cliente = fila_clientes.desenfileirar()
                caixas[i] = cliente.tempo_atendimento
                tempo_espera_total += tempo_total
                clientes_atendidos += 1
                print(f"Tempo {tempo_total}: {cliente} começou a ser atendido no caixa {i+1}")
        
        tempo_total += 1
    
    # Calcular estatísticas
    tempo_medio_espera = tempo_espera_total / num_clientes
    
    print(f"\nSimulação concluída!")
    print(f"Tempo total de atendimento: {tempo_total-1} minutos")
    print(f"Tempo médio de espera: {tempo_medio_espera:.2f} minutos")
    
    return tempo_total-1, tempo_medio_espera


# Demonstração das implementações
if __name__ == "__main__":
    print("Demonstração da Fila com Array:")
    fila_array = FilaArray(5)
    
    print("Enfileirando elementos...")
    for i in range(1, 6):
        fila_array.enfileirar(i)
        print(f"Após enfileirar {i}: {fila_array}")
    
    print("\nDesenfileirando elementos...")
    while not fila_array.esta_vazia():
        item = fila_array.desenfileirar()
        print(f"Desenfileirado: {item}, Fila atual: {fila_array}")
    
    print("\nDemonstração da Fila com Lista Encadeada:")
    fila_encadeada = FilaEncadeada()
    
    print("Enfileirando elementos...")
    for i in range(1, 6):
        fila_encadeada.enfileirar(i)
        print(f"Após enfileirar {i}: {fila_encadeada}")
    
    print("\nDesenfileirando elementos...")
    while not fila_encadeada.esta_vazia():
        item = fila_encadeada.desenfileirar()
        print(f"Desenfileirado: {item}, Fila atual: {fila_encadeada}")
    
    print("\nExemplo: Simulação de atendimento em um banco")
    simular_atendimento_banco(10, 3)
