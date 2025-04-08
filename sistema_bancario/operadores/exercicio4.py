while True:
    valor = int(input('Digite um valor (ou 0 para sair): '))
    
    if valor == 0:
        print('Saindo...')
        break  # Encerra o programa se o usuário digitar 0
    elif valor % 2 == 0:
        print('Número par')
    else:
        print('Número ímpar')
