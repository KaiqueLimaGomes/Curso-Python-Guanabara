#Desafio084
# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo numa lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dado = list()
pessoas = list()
maior = menor = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))

    if len(pessoas) == 0: #Se a lista estiver vazia ele já vai definir a primeira entrada como maior e menor
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]

    pessoas.append(dado[:])
    dado.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

# A) Quantas pessoas foram cadastradas.
print(f'No total você cadastrou {len(pessoas)} pessoas.')

# B) Uma listagem com as pessoas mais pesadas.
print(f'O manior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()

# C) Uma listagem com as pessoas mais leves.
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
