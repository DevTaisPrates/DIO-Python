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
        4. Sair
        """)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: +R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Valor inválido para depósito.")
        
        elif opcao == "2":
            if saques_realizados >= saques_diarios:
                print("Limite diário de saques atingido.")
            else:
                valor = float(input("Informe o valor do saque: "))
                if valor > saldo:
                    print("Saldo insuficiente para saque.")
                elif valor > limite_saque:
                    print("O limite máximo por saque é de R$ 500,00.")
                elif valor > 0:
                    saldo -= valor
                    saques_realizados += 1
                    extrato.append(f"Saque: -R$ {valor:.2f}")
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                else:
                    print("Valor inválido para saque.")
        
        elif opcao == "3":
            print("\n=== Extrato ===")
            if not extrato:
                print("Nenhuma movimentação registrada.")
            else:
                for movimento in extrato:
                    print(movimento)
            print(f"Saldo atual: R$ {saldo:.2f}")
            print("==================")
        
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamando a função para iniciar o menu
menu()
