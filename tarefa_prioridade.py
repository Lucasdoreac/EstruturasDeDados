"""
Sistema de Gerenciamento de Tarefas com Prioridades usando Filas
Autor: Lucas Dórea Cardoso e Deivid Cerqueira - UDF Ciência da Computação

Problema: Em um ambiente de trabalho colaborativo, precisamos gerenciar diversas tarefas
com diferentes níveis de prioridade. As tarefas de alta prioridade devem ser executadas
antes das tarefas de baixa prioridade, mas tarefas da mesma prioridade devem ser
executadas na ordem em que foram adicionadas.

Solução: Implementação de um sistema de gerenciamento de tarefas usando filas de
prioridade. Cada tarefa tem um nome, descrição e nível de prioridade. As tarefas são
organizadas em filas separadas por prioridade.
"""

class Tarefa:
    """
    Classe que representa uma tarefa no sistema de gerenciamento.
    """
    def __init__(self, nome, descricao, prioridade):
        """
        Inicializa uma nova tarefa.
        
        Args:
            nome (str): Nome da tarefa.
            descricao (str): Descrição detalhada da tarefa.
            prioridade (int): Nível de prioridade da tarefa (1 = alta, 2 = média, 3 = baixa).
        """
        self.nome = nome
        self.descricao = descricao
        self.prioridade = prioridade
    
    def __str__(self):
        """
        Retorna uma representação em string da tarefa.
        
        Returns:
            str: Representação da tarefa.
        """
        prioridade_texto = {1: "Alta", 2: "Média", 3: "Baixa"}.get(self.prioridade, "Desconhecida")
        return f"Tarefa: {self.nome} (Prioridade: {prioridade_texto})\nDescrição: {self.descricao}"


class FilaTarefas:
    """
    Implementação de uma fila simples para armazenar tarefas de mesma prioridade.
    """
    def __init__(self):
        """
        Inicializa uma fila vazia.
        """
        self.tarefas = []
    
    def adicionar(self, tarefa):
        """
        Adiciona uma tarefa ao final da fila.
        
        Args:
            tarefa (Tarefa): A tarefa a ser adicionada.
        """
        self.tarefas.append(tarefa)
    
    def remover(self):
        """
        Remove e retorna a tarefa do início da fila.
        
        Returns:
            Tarefa: A tarefa removida ou None se a fila estiver vazia.
        """
        if not self.esta_vazia():
            return self.tarefas.pop(0)
        return None
    
    def frente(self):
        """
        Retorna a tarefa do início da fila sem removê-la.
        
        Returns:
            Tarefa: A tarefa no início da fila ou None se a fila estiver vazia.
        """
        if not self.esta_vazia():
            return self.tarefas[0]
        return None
    
    def esta_vazia(self):
        """
        Verifica se a fila está vazia.
        
        Returns:
            bool: True se a fila estiver vazia, False caso contrário.
        """
        return len(self.tarefas) == 0
    
    def tamanho(self):
        """
        Retorna o número de tarefas na fila.
        
        Returns:
            int: Número de tarefas na fila.
        """
        return len(self.tarefas)


class GerenciadorTarefas:
    """
    Sistema de gerenciamento de tarefas que utiliza filas de prioridade.
    """
    def __init__(self):
        """
        Inicializa o gerenciador de tarefas com filas para cada nível de prioridade.
        """
        # Filas para cada nível de prioridade (1 = alta, 2 = média, 3 = baixa)
        self.filas_prioridades = {
            1: FilaTarefas(),  # Alta prioridade
            2: FilaTarefas(),  # Média prioridade
            3: FilaTarefas()   # Baixa prioridade
        }
    
    def adicionar_tarefa(self, tarefa):
        """
        Adiciona uma tarefa ao gerenciador com base em sua prioridade.
        
        Args:
            tarefa (Tarefa): A tarefa a ser adicionada.
        
        Returns:
            bool: True se a tarefa foi adicionada com sucesso, False caso contrário.
        """
        # Verifica se a prioridade é válida
        if tarefa.prioridade not in self.filas_prioridades:
            print(f"Erro: Prioridade inválida ({tarefa.prioridade})")
            return False
        
        # Adiciona a tarefa à fila correspondente
        self.filas_prioridades[tarefa.prioridade].adicionar(tarefa)
        print(f"Tarefa '{tarefa.nome}' adicionada com prioridade {tarefa.prioridade}")
        return True
    
    def proxima_tarefa(self):
        """
        Retorna a próxima tarefa a ser executada com base na prioridade.
        Remove a tarefa da fila.
        
        Returns:
            Tarefa: A próxima tarefa a ser executada ou None se não houver tarefas.
        """
        # Verifica as filas por ordem de prioridade
        for prioridade in sorted(self.filas_prioridades.keys()):
            fila = self.filas_prioridades[prioridade]
            if not fila.esta_vazia():
                return fila.remover()
        
        print("Não há tarefas pendentes")
        return None
    
    def visualizar_proxima_tarefa(self):
        """
        Visualiza a próxima tarefa a ser executada sem removê-la.
        
        Returns:
            Tarefa: A próxima tarefa a ser executada ou None se não houver tarefas.
        """
        # Verifica as filas por ordem de prioridade
        for prioridade in sorted(self.filas_prioridades.keys()):
            fila = self.filas_prioridades[prioridade]
            if not fila.esta_vazia():
                return fila.frente()
        
        print("Não há tarefas pendentes")
        return None
    
    def estatisticas(self):
        """
        Retorna estatísticas sobre as tarefas no gerenciador.
        
        Returns:
            dict: Dicionário com estatísticas.
        """
        total_tarefas = sum(fila.tamanho() for fila in self.filas_prioridades.values())
        
        stats = {
            "total": total_tarefas,
            "por_prioridade": {
                prioridade: fila.tamanho()
                for prioridade, fila in self.filas_prioridades.items()
            }
        }
        
        return stats
    
    def listar_todas_tarefas(self):
        """
        Lista todas as tarefas no gerenciador, agrupadas por prioridade.
        """
        total_tarefas = 0
        
        print("\n===== LISTA DE TAREFAS =====")
        
        # Para cada nível de prioridade
        for prioridade in sorted(self.filas_prioridades.keys()):
            fila = self.filas_prioridades[prioridade]
            num_tarefas = fila.tamanho()
            total_tarefas += num_tarefas
            
            prioridade_texto = {1: "ALTA", 2: "MÉDIA", 3: "BAIXA"}.get(prioridade, "DESCONHECIDA")
            print(f"\n--- Prioridade {prioridade_texto} ({num_tarefas} tarefas) ---")
            
            # Se a fila estiver vazia
            if fila.esta_vazia():
                print("Nenhuma tarefa nesta categoria")
                continue
            
            # Lista as tarefas desta prioridade
            for i, tarefa in enumerate(fila.tarefas):
                print(f"{i+1}. {tarefa.nome} - {tarefa.descricao[:50]}{'...' if len(tarefa.descricao) > 50 else ''}")
        
        print(f"\nTotal: {total_tarefas} tarefas")
        print("============================")


# Demonstração do sistema
if __name__ == "__main__":
    # Criar o gerenciador de tarefas
    gerenciador = GerenciadorTarefas()
    
    # Adicionar algumas tarefas de exemplo
    tarefas = [
        Tarefa("Corrigir bug crítico", "O sistema de login está falhando para alguns usuários", 1),
        Tarefa("Atualizar documentação", "Atualizar a documentação da API com os novos endpoints", 2),
        Tarefa("Otimizar consulta SQL", "A consulta de relatórios está muito lenta", 1),
        Tarefa("Adicionar novos ícones", "Adicionar os ícones para o novo tema", 3),
        Tarefa("Revisar pull requests", "Revisar os PRs pendentes da equipe", 2),
        Tarefa("Corrigir erros de digitação", "Corrigir erros de digitação na interface", 3),
        Tarefa("Investigar falha de segurança", "Verificar possível vulnerabilidade reportada", 1),
        Tarefa("Implementar dark mode", "Adicionar suporte para tema escuro", 2)
    ]
    
    # Adicionar as tarefas ao gerenciador
    print("Adicionando tarefas ao gerenciador...\n")
    for tarefa in tarefas:
        gerenciador.adicionar_tarefa(tarefa)
    
    # Mostrar estatísticas
    stats = gerenciador.estatisticas()
    print("\nEstatísticas:")
    print(f"Total de tarefas: {stats['total']}")
    for prioridade, quantidade in stats['por_prioridade'].items():
        prioridade_texto = {1: "Alta", 2: "Média", 3: "Baixa"}.get(prioridade, "Desconhecida")
        print(f"Prioridade {prioridade_texto}: {quantidade} tarefas")
    
    # Listar todas as tarefas
    gerenciador.listar_todas_tarefas()
    
    # Processar algumas tarefas
    print("\nProcessando tarefas por ordem de prioridade:")
    for _ in range(5):
        tarefa = gerenciador.proxima_tarefa()
        if tarefa:
            print(f"\nExecutando: {tarefa}")
            print("-" * 40)
    
    # Mostrar estatísticas atualizadas
    stats = gerenciador.estatisticas()
    print("\nEstatísticas atualizadas:")
    print(f"Total de tarefas restantes: {stats['total']}")
    for prioridade, quantidade in stats['por_prioridade'].items():
        prioridade_texto = {1: "Alta", 2: "Média", 3: "Baixa"}.get(prioridade, "Desconhecida")
        print(f"Prioridade {prioridade_texto}: {quantidade} tarefas")
    
    # Listar as tarefas restantes
    gerenciador.listar_todas_tarefas()
