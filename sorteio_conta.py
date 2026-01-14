import random

nomes = []
opcao = -1

while opcao != 0:
    print('\n1 - Adicionar nomes')
    print('2 - Sortear quem paga')
    print('0 - Sair')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        while True:
            nome = input('Digite um nome: ')
            nomes.append(nome)

            continuar = input('Deseja adicionar outro nome? (sim/não): ').lower()
            if continuar != 'sim':
                break

    elif opcao == 2:
        if len(nomes) == 0:
            print('Nenhum nome cadastrado!')
        else:
            sorteado = random.choice(nomes)
            print(f'Parabéns, você paga a conta hoje: {sorteado}')

    elif opcao == 0:
        print('Saindo...')

    else:
        print('Opção inválida')
