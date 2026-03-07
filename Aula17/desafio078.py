#Desafio078
# Faça um programa que leia 5 valores numéricos e guarde-os numa lista.
# No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista.

lista = []

for cont in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))

print(f'Você digitou os valores {lista}')

print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for pos, v in enumerate(lista):
    if v == max(lista):
        print(f'{pos}...', end='')

print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for pos, v in enumerate(lista):
    if v == min(lista):
        print(f'{pos}...', end='')
