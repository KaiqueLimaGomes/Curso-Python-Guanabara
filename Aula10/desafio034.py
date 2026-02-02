#Desafio034
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%

sal = float(input('Digite o valor do seu salário: '))

if sal <= 1250:
    print('Com o aumento de 15%, o seu salário foi para R${:.2f}'.format(sal + (sal * 15/100)))
else:
    print('Com o aumento de 10%, o seu salário foi para R${:.2f}'.format(sal + (sal * 10/100)))
