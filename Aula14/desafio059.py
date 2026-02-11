#Desafio059
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos Números
# [5] Sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
opcao = 0



while opcao != 5:
    print('--' * 10)
    print('Escolha uma Opção: ')
    print('''
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos Números
        [5] Sair do programa
    ''')
    opcao = int(input('Opção: '))

    if opcao not in range(1, 6):
        print('\033[31m Entrada Inválida, Tente novamente!\033[m')

    else:
        if opcao == 1:
            print('{} + {} = {}'.format(num1, num2, num1 + num2))

        if opcao == 2:
            print('{} x {} = {}'.format(num1, num2, num1 * num2))

        if opcao == 3:
            if num1 > num2:
                print('O número {} é maior que {}'.format(num1, num2))
            else:
                print('O Número {} é maior que {}'.format(num2, num1))

        if opcao == 4:
            print('Digite novos números')
            num1 = float(input('Primeiro número: '))
            num2 = float(input('Segundo número: '))

print('FIM')
