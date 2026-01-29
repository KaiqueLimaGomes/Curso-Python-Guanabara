#Desafio013
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo sálario, com 15% de aumento.

salario = float(input('Informe seu sálario atual: R$ '))

#Valor inteiro da porcentagem EX: 15%
porc = 15
nsalario = salario + (salario * porc / 100)
print('Seu salário de R$ {:.2f} com aumento de {}% \n Novo salário: R$ {:.2f}'.format(salario, porc, nsalario))
