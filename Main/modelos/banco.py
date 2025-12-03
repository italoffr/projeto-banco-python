CLIENTES = []
CONTAS = []
EMPRESTIMOS = []

PROXIMO_ID_CLIENTE = 1
PROXIMO_NUMERO_CONTA = 1001

# Função que auxilia na busca pelo cliente na lista
def buscar_cliente_por_id(id_cliente):
    # A lista CLIENTES é usada diretamente
    for cliente in CLIENTES:
        if cliente["id_cliente"] == id_cliente:
            return cliente
    # Corrigindo o erro de indentação: só retorna None após checar todos
    return None 

# Função de cadastro de cliente
def cadastrar_cliente(nome, cpf, telefone, endereco):
    # Precisamos usar 'global' para modificar o contador
    global PROXIMO_ID_CLIENTE
    
    novo_cliente = {
        "id_cliente": PROXIMO_ID_CLIENTE, # Usando o contador global
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "endereco": endereco
    }
    CLIENTES.append(novo_cliente) # Adiciona à lista global
    PROXIMO_ID_CLIENTE += 1 # Incrementa o contador global
    return novo_cliente
    
# Função para abrir uma nova conta
def abrir_conta(id_cliente, tipo_conta="Corrente", saldo_inicial=0.0):
    # Precisamos usar 'global' para modificar o contador
    global PROXIMO_NUMERO_CONTA
    
    # 1. Busca o cliente na lista de clientes
    cliente_existe = buscar_cliente_por_id(id_cliente) # Chama a função independente
    if not cliente_existe:
        print("Erro: Cliente não encontrado.")
        return None
        
    # 2. Define atributos básicos da conta
    nova_conta = {
        "numero": str(PROXIMO_NUMERO_CONTA).zfill(4) + "-5",
        "saldo": saldo_inicial,
        "data_abertura": "2025-12-02",
        "id_cliente": id_cliente,
        "tipo": tipo_conta,
    }

    # 3. Adiciona atributos específicos com base no 'tipo'
    if tipo_conta == "Corrente":
        nova_conta["limite_credito"] = 500.00
    elif tipo_conta == "Poupanca":
        nova_conta["taxa_juros"] = 0.005 #  -> taxa_juros  0.5%

    CONTAS.append(nova_conta) # Adiciona a lista global
    PROXIMO_NUMERO_CONTA += 1 # Incrementa o contador global
    return nova_conta

#  TESTE  ----------------------------

if __name__ == "__main__":
    print("--- INICIANDO TESTES DO SISTEMA PROCEDURAL ---")
    
    # Chamadas diretas das funções (sem objeto Banco)
    cliente_a = cadastrar_cliente("Carlos", "123", "999", "Rua X")
    cliente_b = cadastrar_cliente("Diana", "456", "888", "Rua Y")
    
    abrir_conta(cliente_a["id_cliente"], "Corrente", 1000.00)
    abrir_conta(cliente_b["id_cliente"], "Poupanca", 50.00)
    
    print("\n[RESULTADO 1] Lista Global de Clientes:")
    print(CLIENTES)
    
    print("\n[RESULTADO 2] Lista Global de Contas:")
    print(CONTAS)