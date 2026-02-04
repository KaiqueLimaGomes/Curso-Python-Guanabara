#Desafio036
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
#ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa que deseja comprar? R$'))
anos = float(input('Em quantos anos desejar pagar? '))
sal = float(input('Qual o seu salário? R$ '))
prestacao = casa / (anos * 12)

if prestacao > sal * 30/100:
    print('Infelizmente o seu empréstimo foi negado, a prestação ficou muito alta.')
else:
    print('PARABÉNS, seu empréstimo foi aprovado! A prestação ficou em R${:.2f}'.format(prestacao))
print('Obrigado pela preferência!')
