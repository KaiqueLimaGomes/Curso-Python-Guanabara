#Desafio
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número inteiro: '))

if num % 1 == num and num % num == 1:
    print('O número {} é PRIMO')
else:
    print('O número {} não é primo.')