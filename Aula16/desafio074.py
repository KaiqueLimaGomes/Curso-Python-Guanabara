#Desafio074
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e maior valor que estão na tupla.

from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os valores sorteados foram: {tupla}')
print(f'O menor valor gerado é {min(tupla)}')
print(f'O maior valor gerado é {max(tupla)}')
