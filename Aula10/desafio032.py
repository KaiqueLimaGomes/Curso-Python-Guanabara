#Desafio032
#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or 400 == 0:
    print('O ano de {} é Bissexto!'.format(ano))
else:
    print('O ano de {} NÃO é Bissexto!'.format(ano))
