#1. ESTRUTURAS DE DADOS GLOBAIS (Simulam o "Banco de Dados")
# ----------------------------------------------------------------------

# CLIENTES: Dicionário. Chave: documento (string), Valor: dicionário do cliente
CLIENTES = {}

# CONTAS: Lista de dicionários de contas
CONTAS = []

# EMPRESTIMOS: Lista de dicionários de empréstimos
EMPRESTIMOS = []

# Variáveis sequenciais para gerar IDs únicos
NUMERO_CONTA_SEQ = 1001
NUMERO_TRANSACAO_SEQ = 1

class Cliente:
    def __init__(self, nome, documento):
        self.nome = nome  
        self.documento = documento
        self._contas = [] 
rfedre