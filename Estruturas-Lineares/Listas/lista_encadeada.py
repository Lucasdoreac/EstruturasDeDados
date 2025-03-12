"""
Implementação de Lista Encadeada em Python
Autor: Lucas Dórea Cardoso e Deivid Cerqueira - UDF Ciência da Computação
"""

class No:
    """
    Classe que representa um nó na lista encadeada.
    Cada nó contém um valor e uma referência para o próximo nó.
    """
    def __init__(self, valor):
        self.valor = valor  # Valor armazenado no nó
        self.proximo = None  # Referência para o próximo nó (None por padrão)

class ListaEncadeada:
    """
    Implementação de uma lista encadeada simples.
    Mantém referência para o primeiro nó (cabeça) da lista.
    """
    def __init__(self):
        """
        Inicializa uma lista encadeada vazia.
        """
        self.cabeca = None  # Referência para o primeiro nó
        self.tamanho = 0    # Contador para o tamanho da lista
    
    def esta_vazia(self):
        """
        Verifica se a lista está vazia.
        
        Returns:
            bool: True se a lista estiver vazia, False caso contrário.
        """
        return self.cabeca is None
    
    def tamanho_lista(self):
        """
        Retorna o tamanho atual da lista.
        
        Returns:
            int: Número de elementos na lista.
        """
        return self.tamanho
    
    def inserir_inicio(self, valor):
        """
        Insere um novo nó no início da lista.
        
        Args:
            valor: O valor a ser armazenado no novo nó.
        """
        novo_no = No(valor)  # Cria um novo nó
        
        if self.esta_vazia():
            # Se a lista estiver vazia, o novo nó se torna a cabeça
            self.cabeca = novo_no
        else:
            # Se não, o novo nó aponta para a cabeça atual
            # e se torna a nova cabeça
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
        
        self.tamanho += 1
    
    def inserir_final(self, valor):
        """
        Insere um novo nó no final da lista.
        
        Args:
            valor: O valor a ser armazenado no novo nó.
        """
        novo_no = No(valor)  # Cria um novo nó
        
        if self.esta_vazia():
            # Se a lista estiver vazia, o novo nó se torna a cabeça
            self.cabeca = novo_no
        else:
            # Encontra o último nó
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            
            # O último nó aponta para o novo nó
            atual.proximo = novo_no
        
        self.tamanho += 1
    
    def inserir_posicao(self, valor, posicao):
        """
        Insere um novo nó em uma posição específica da lista.
        
        Args:
            valor: O valor a ser armazenado no novo nó.
            posicao: A posição onde o novo nó será inserido (0-based).
        
        Raises:
            IndexError: Se a posição for inválida.
        """
        # Verifica se a posição é válida
        if posicao < 0 or posicao > self.tamanho:
            raise IndexError("Posição inválida")
        
        # Caso especial: inserção no início
        if posicao == 0:
            self.inserir_inicio(valor)
            return
        
        # Caso especial: inserção no final
        if posicao == self.tamanho:
            self.inserir_final(valor)
            return
        
        # Caso geral: inserção no meio
        novo_no = No(valor)
        
        # Navegação até o nó anterior à posição desejada
        atual = self.cabeca
        for _ in range(posicao - 1):
            atual = atual.proximo
        
        # Insere o novo nó entre o atual e o próximo
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no
        
        self.tamanho += 1
    
    def remover_inicio(self):
        """
        Remove o nó do início da lista.
        
        Returns:
            O valor do nó removido.
        
        Raises:
            IndexError: Se a lista estiver vazia.
        """
        if self.esta_vazia():
            raise IndexError("Não é possível remover de uma lista vazia")
        
        valor = self.cabeca.valor  # Valor a ser retornado
        self.cabeca = self.cabeca.proximo  # A cabeça agora é o segundo nó
        
        self.tamanho -= 1
        return valor
    
    def remover_final(self):
        """
        Remove o nó do final da lista.
        
        Returns:
            O valor do nó removido.
        
        Raises:
            IndexError: Se a lista estiver vazia.
        """
        if self.esta_vazia():
            raise IndexError("Não é possível remover de uma lista vazia")
        
        # Caso especial: apenas um nó na lista
        if self.cabeca.proximo is None:
            valor = self.cabeca.valor
            self.cabeca = None
            self.tamanho -= 1
            return valor
        
        # Caso geral: múltiplos nós
        # Navega até o penúltimo nó
        atual = self.cabeca
        while atual.proximo.proximo is not None:
            atual = atual.proximo
        
        valor = atual.proximo.valor  # Valor do último nó
        atual.proximo = None  # Remove a referência para o último nó
        
        self.tamanho -= 1
        return valor
    
    def remover_posicao(self, posicao):
        """
        Remove o nó de uma posição específica da lista.
        
        Args:
            posicao: A posição do nó a ser removido (0-based).
        
        Returns:
            O valor do nó removido.
        
        Raises:
            IndexError: Se a posição for inválida ou a lista estiver vazia.
        """
        # Verifica se a lista está vazia
        if self.esta_vazia():
            raise IndexError("Não é possível remover de uma lista vazia")
        
        # Verifica se a posição é válida
        if posicao < 0 or posicao >= self.tamanho:
            raise IndexError("Posição inválida")
        
        # Caso especial: remoção do início
        if posicao == 0:
            return self.remover_inicio()
        
        # Caso especial: remoção do final
        if posicao == self.tamanho - 1:
            return self.remover_final()
        
        # Caso geral: remoção no meio
        # Navega até o nó anterior ao que será removido
        atual = self.cabeca
        for _ in range(posicao - 1):
            atual = atual.proximo
        
        valor = atual.proximo.valor  # Valor do nó a ser removido
        atual.proximo = atual.proximo.proximo  # Remove a referência
        
        self.tamanho -= 1
        return valor
    
    def buscar(self, valor):
        """
        Busca um valor na lista e retorna sua posição.
        
        Args:
            valor: O valor a ser buscado.
        
        Returns:
            int: A posição do valor na lista, ou -1 se não for encontrado.
        """
        atual = self.cabeca
        posicao = 0
        
        while atual is not None:
            if atual.valor == valor:
                return posicao
            atual = atual.proximo
            posicao += 1
        
        return -1  # Valor não encontrado
    
    def obter_valor(self, posicao):
        """
        Retorna o valor na posição especificada.
        
        Args:
            posicao: A posição do valor desejado (0-based).
        
        Returns:
            O valor na posição especificada.
        
        Raises:
            IndexError: Se a posição for inválida.
        """
        if posicao < 0 or posicao >= self.tamanho:
            raise IndexError("Posição inválida")
        
        atual = self.cabeca
        for _ in range(posicao):
            atual = atual.proximo
        
        return atual.valor
    
    def __str__(self):
        """
        Retorna uma representação em string da lista.
        
        Returns:
            str: Uma representação da lista no formato "valor1 -> valor2 -> ... -> valorN".
        """
        if self.esta_vazia():
            return "Lista vazia"
        
        valores = []
        atual = self.cabeca
        
        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.proximo
        
        return " -> ".join(valores)

# Exemplo de uso
if __name__ == "__main__":
    lista = ListaEncadeada()
    
    print("Inserindo elementos na lista...")
    lista.inserir_inicio(10)
    lista.inserir_final(20)
    lista.inserir_final(30)
    lista.inserir_posicao(15, 1)
    
    print(f"Lista: {lista}")
    print(f"Tamanho da lista: {lista.tamanho_lista()}")
    
    print("\nBuscando elementos...")
    print(f"Posição do valor 15: {lista.buscar(15)}")
    print(f"Posição do valor 25: {lista.buscar(25)}")
    
    print("\nAcessando elementos por posição...")
    print(f"Elemento na posição 0: {lista.obter_valor(0)}")
    print(f"Elemento na posição 2: {lista.obter_valor(2)}")
    
    print("\nRemovendo elementos...")
    print(f"Removido do início: {lista.remover_inicio()}")
    print(f"Lista após remoção: {lista}")
    
    print(f"Removido da posição 1: {lista.remover_posicao(1)}")
    print(f"Lista após remoção: {lista}")
    
    print(f"Removido do final: {lista.remover_final()}")
    print(f"Lista após remoção: {lista}")
