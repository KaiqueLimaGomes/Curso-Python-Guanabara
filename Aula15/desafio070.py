#Desafio070
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1.000
# C) Qual é o nome do produto mais barato.

total = cont = pbarato = 0
nbarato = ''
primeiro = True

print('--'*10)
print('Kalunga')
print('--'*10)

while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))

    total += preco

    if preco > 1000:
        cont += 1

    if primeiro:
        pbarato = preco
        nbarato = produto
        primeiro = False
    elif preco < pbarato:
        pbarato = preco
        nbarato = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'O valor total gasto na compra foi de R${total:.2f}')
print(f'Dos produtos comprados, {cont} produtos custam mais de R$1.000')
print(f'{nbarato} foi o produto mais barato, custando R${pbarato:.2f}')
