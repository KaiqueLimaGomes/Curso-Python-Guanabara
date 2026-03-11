#Desafio084
# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo numa lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dado = list()
pessoas = list()
total = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    total += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'No total você cadastrou {total} pessoas.')
print('As pessoas acima de 100Kg foram: ', end='')
for p in pessoas:

    if p[1] >= 100:
        print(p[0])
