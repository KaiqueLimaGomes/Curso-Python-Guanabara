#Desafio065
# Crie um programa que leia vários números inteiros pelo teclado. No final da execuçãp,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = 0
soma = 0
cont = 0
sair = 'S'

while sair != 'N':
    num = int(input('Digite um número inteiro: '))
    soma += num
    cont += 1
    sair = str(input('Desejar continuar? [S/N] ').upper().strip())
print('Você digitou {} números e a soma deles é {} e a média é {}'.format(cont, soma, soma / cont))