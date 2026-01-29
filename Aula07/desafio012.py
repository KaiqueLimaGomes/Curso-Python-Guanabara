#Desafio012
#Faça um algoritmo que leia preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual o preço do produto? R$'))
#Valor inteiro do desconto EX: 5%
desconto = 5
npreco = preco - (preco * desconto/100)
print('O produto com {}% de desconto fica R${:.2f}'.format(desconto, npreco))
