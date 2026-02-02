#Desafio028
#Escreva um programa que faça o computador "penser" em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu
import random
from random import randint

chute = int(input('Digite um numero entre 0 e 5: '))
num = random.randint(0, 5)

if chute == num:
    print('Parabéns! Você acertou o número escolhido!')
else:
    print('Infelizmente você não acertou, o número escolhido foi {}.'.format(num))