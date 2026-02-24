#Desafio068
# Faça um programa que jogue par ou ímpar com o computador.
# O jogo será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

njog = ncom = cont = 0

print('=-='*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-='*10)

while True:
    njog = int(input('Digite um valor: '))
    ncom = randint(0, 10)
    soma = njog + ncom
    opcao = ' '

    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar? [P/I]:  ')).strip().upper()[0]
    print(f'Você jogou {njog} e o computador {ncom}, o que resultou em {soma} que é ', end='')
    print('PAR' if soma % 2 == 0 else 'IMPAR')

    if opcao == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!!')
            cont += 1
        else:
            print('Você PERDEU...')
            break
    elif opcao == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!!')
            cont += 1
        else:
            print('Você PERDEU...')
            break
    print('Vamos jogar novamente!')
print(f'Você venceu {cont} vezes seguidas.')
