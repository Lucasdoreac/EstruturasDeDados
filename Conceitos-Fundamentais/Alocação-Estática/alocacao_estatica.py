"""
Exemplo de alocação estática de memória em Python
Autor: Lucas Dórea Cardoso e Deivid Cerqueira - UDF Ciência da Computação
"""

def demonstracao_alocacao_estatica():
    """
    Demonstração de como Python lida com alocação estática.
    
    Em Python, não há alocação estática verdadeira como em C/C++,
    mas podemos simular o conceito usando arrays de tamanho fixo
    e entender como o Python gerencia a memória internamente.
    """
    print("Demonstração de Alocação 'Estática' em Python")
    print("-" * 50)
    
    # 1. Arrays de tamanho fixo usando listas
    print("1. Arrays de tamanho fixo (simulado):")
    
    # Criando um array de tamanho fixo
    tamanho = 5
    array_fixo = [None] * tamanho
    
    print(f"Array criado com tamanho fixo de {tamanho} elementos: {array_fixo}")
    
    # Preenchendo o array
    for i in range(tamanho):
        array_fixo[i] = i * 10
    
    print(f"Array após preenchimento: {array_fixo}")
    
    # Tentativa de acesso além do limite (geraria erro)
    print("Tentativa de acesso além do limite (comentado no código)")
    # Descomentar para ver o erro:
    # array_fixo[tamanho] = 100  # Isso causaria um IndexError
    
    print("\n2. Tuplas (imutáveis e de tamanho fixo):")
    # 2. Tuplas - são imutáveis e têm tamanho fixo
    tupla_fixa = (1, 2, 3, 4, 5)
    print(f"Tupla criada: {tupla_fixa}")
    
    # Tentativa de modificação (geraria erro)
    print("Tentativa de modificação (comentado no código)")
    # Descomentar para ver o erro:
    # tupla_fixa[0] = 10  # Isso causaria um TypeError
    
    print("\n3. Variáveis 'estáticas' em funções:")
    
    # Em Python, não há verdadeiras variáveis estáticas locais,
    # mas podemos simular com atributos de função
    def contador():
        # Este atributo é inicializado apenas uma vez
        if not hasattr(contador, "contagem"):
            contador.contagem = 0
        
        contador.contagem += 1
        return contador.contagem
    
    for _ in range(5):
        print(f"Chamada do contador: {contador()}")
    
    print("\n4. Constantes (simuladas em Python):")
    
    # Python não tem constantes reais, mas por convenção
    # usamos letras maiúsculas para variáveis que não devem mudar
    PI = 3.14159
    TAMANHO_MAXIMO = 100
    NOME_APP = "Demonstração de Alocação Estática"
    
    print(f"Constantes definidas: PI={PI}, TAMANHO_MAXIMO={TAMANHO_MAXIMO}")
    print(f"NOME_APP={NOME_APP}")
    
    print("\n5. Classes com atributos de classe (estáticos):")
    
    class Configuracao:
        # Atributos de classe são compartilhados entre todas as instâncias
        versao = "1.0"
        autor = "Lucas Dórea Cardoso e Deivid Cerqueira"
        max_conexoes = 10
        
        def __init__(self, nome):
            # Este é um atributo de instância, não estático
            self.nome = nome
    
    print(f"Versão (atributo de classe): {Configuracao.versao}")
    print(f"Autor (atributo de classe): {Configuracao.autor}")
    
    # Criando instâncias
    config1 = Configuracao("Instância 1")
    config2 = Configuracao("Instância 2")
    
    # Alterando um atributo de classe
    Configuracao.versao = "1.1"
    
    # A alteração afeta todas as instâncias
    print(f"\nApós alteração:")
    print(f"Versão via classe: {Configuracao.versao}")
    print(f"Versão via instância 1: {config1.versao}")
    print(f"Versão via instância 2: {config2.versao}")
    
    print("\nConclusão:")
    print("Em Python, a alocação de memória é principalmente dinâmica e gerenciada")
    print("pelo coletor de lixo, mas podemos simular alguns aspectos de alocação")
    print("estática através de estruturas de tamanho fixo, atributos de classe e")
    print("convenções de nomenclatura.")

if __name__ == "__main__":
    demonstracao_alocacao_estatica()
