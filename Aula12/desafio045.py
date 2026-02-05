#Desafio045
#Crie um programa que faça o computador jogar JOKENPÔ com você.
import random

print('-=-' * 20)
print('JOKENPÔ      ' *5)
print('-=-' * 20)
user = str(input('Escolha:'
      '\n Pedra'
      '\n Papel'
      '\n Tesoura'
      '\n Opção: '))
opcoes = ['Pedra', 'Papel', 'Tesoura']
pc = random.choice(opcoes)

if user == pc:
    print('EMPATE! Você escolheu {} e o computador {}'.format(user, pc))
    