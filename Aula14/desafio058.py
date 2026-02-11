#Desafio058
# Melhore o jogo dp DESAFIO 028, onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinha até acertar, mostrando no final quantos palpites
# foram necessários para vencer.
import time
from random import randint

palpite = 99
cont = 0

linha = '-=-' * 20
print(linha)
print('Jogo da Adivinhação'.center(len(linha)))
print(linha)

time.sleep(1)
print('COMPUTADOR PENSNADO...')
escolhido = randint(0, 10)

time.sleep(2)
print('COMPUTADOR: Pensei em um número de 0 a 10! Que número é esse?')

while escolhido != palpite:
    palpite = int(input('Palpite: '))
    cont += 1
    if palpite != escolhido:
        print('\033[31m Errou... Tente novamente!\033[m')

print('\033[42mPARABÉNS, você acertou!\033[m')
print('O número pensado pelo Computador foi {}.'.format(escolhido))
if cont == 1:
    print('Você acertou de primeira! Excelente!')
else:
    print('Você acertou na {}ª tentativa!'.format(cont))
