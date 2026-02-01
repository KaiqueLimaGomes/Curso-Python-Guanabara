#Desafio025
#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome completo: '))
nome = nome.strip()
nome = nome.upper()
print('Seu sobrenome tem Silva? {}'.format('SILVA' in nome))

#Se o por EX o nome for 'SILVANA' ele ainda retornará True