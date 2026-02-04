#Desafio038
#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é Maior
# - O segundo valor é Maior
# - Não existe valor maior, os dois são iguais.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digte o segundo número: '))

if num1 > num2:
    print('O primeiro valor {} é maior que o segundo {}.'.format(num1, num2))
elif num1 < num2:
    print('O segundo valor {} é maior que o primeiro {}.'.format(num2, num1))
elif num1 == num2:
    print('Não existe valor maior, os dois são iguais.')
