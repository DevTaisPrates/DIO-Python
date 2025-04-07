from datetime import datetime

# Decorador de log para registrar chamadas de funções
def log_atividade(func):
    def wrapper(*args, **kwargs):
        hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"[LOG {hora}] Função '{func.__name__}' foi chamada.")
        return func(*args, **kwargs)
    return wrapper

# Função para cadastrar um cliente
clientes = {}  # Armazena os clientes em um dicionário com CPF como chave

@log_atividade
def cadastrar_cliente():
    cpf = input("Informe o CPF do cliente: ")
    if cpf in clientes:
        print("Cliente já cadastrado!")
    else:
        nome = input("Informe o nome do cliente: ")
        telefone = input("Informe o telefone do cliente: ")
        clientes[cpf] = {'nome': nome, 'telefone': telefone}
        print(f"Cliente {nome} cadastrado com sucesso!")

# Função para cadastrar uma conta bancária
contas = {}  # Armazena as contas bancárias em um dicionário com o número da conta como chave

@log_atividade
def cadastrar_conta_bancaria():
    cpf = input("Informe o CPF do cliente: ")
    if cpf not in clientes:
        print("Cliente não encontrado! Cadastre o cliente primeiro.")
        return

    numero_conta = input("Informe o número da conta bancária: ")
    if numero_conta in contas:
        print("Número de conta já cadastrado!")
    else:
        agencia = input("Informe o número da agência: ")
        saldo_inicial = float(input("Informe o saldo inicial da conta: "))
        contas[numero_conta] = {'cpf_cliente': cpf, 'agencia': agencia, 'saldo': saldo_inicial}
        print(f"Conta bancária {numero_conta} cadastrada com sucesso!")

# Função de depósito com log
@log_atividade
def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: +R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")
    except ValueError:
        print("Entrada inválida. Digite um número.")
    return saldo, extrato

# Função de saque com log
@log_atividade
def sacar(saldo, extrato, saques_realizados, limite_saque, saques_diarios):
    if saques_realizados >= saques_diarios:
        print("Limite diário de saques atingido.")
    else:
        try:
            valor = float(input("Informe o valor do saque: "))
            if valor > saldo:
                print("Saldo insuficiente para saque.")
            elif valor > limite_saque:
                print(f"O limite máximo por saque é de R$ {limite_saque:.2f}.")
            elif valor > 0:
                saldo -= valor
                saques_realizados += 1
                extrato.append(f"Saque: -R$ {valor:.2f}")
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Valor inválido para saque.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
    return saldo, extrato, saques_realizados

# Função para mostrar extrato com log e iterador
class ExtratoIterator:
    def __init__(self, extrato):
        self._extrato = extrato
        self._indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._indice < len(self._extrato):
            movimento = self._extrato[self._indice]
            self._indice += 1
            return movimento
        else:
            raise StopIteration

@log_atividade
def mostrar_extrato(saldo, extrato):
    print("\n=== Extrato ===")
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        for movimento in ExtratoIterator(extrato):
            print(movimento)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("==================")

# Função para gerar relatório financeiro com log
@log_atividade
def gerar_relatorio(extrato, saldo):
    total_depositos = sum(float(mov.split('R$ ')[1]) for mov in extrato if "Depósito" in mov)
    total_saques = sum(float(mov.split('R$ ')[1]) for mov in extrato if "Saque" in mov)

    print("\n=== Relatório Financeiro ===")
    print(f"Total de Depósitos: R$ {total_depositos:.2f}")
    print(f"Total de Saques:    R$ {total_saques:.2f}")
    print(f"Saldo Final:        R$ {saldo:.2f}")
    print("============================")

# Função de menu principal
def menu():
    saldo = 0.0
    limite_saque = 500
    saques_diarios = 3
    saques_realizados = 0
    extrato = []

    while True:
        print("""
        === Menu ===
        1. Depósito
        2. Saque
        3. Extrato
        4. Relatório
        5. Cadastrar Cliente
        6. Cadastrar Conta Bancária
        7. Sair
        """)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)
        
        elif opcao == "2":
            saldo, extrato, saques_realizados = sacar(
                saldo, extrato, saques_realizados, limite_saque, saques_diarios
            )
            print(f"Você ainda pode realizar {saques_diarios - saques_realizados} saques hoje.")
        
        elif opcao == "3":
            mostrar_extrato(saldo, extrato)
        
        elif opcao == "4":
            gerar_relatorio(extrato, saldo)
        
        elif opcao == "5":
            cadastrar_cliente()
        
        elif opcao == "6":
            cadastrar_conta_bancaria()
        
        elif opcao == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
menu()
