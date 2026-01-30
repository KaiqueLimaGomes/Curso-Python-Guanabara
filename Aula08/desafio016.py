#Desafio016
#Crie um programa que leia um número Real qualquer pelo teclado e mostre na sua tela a porção inteira.
#EX: Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.

import math

num = float(input('Digite um número Real qualquer: '))
print('A porção inteira de {} é {}'.format(num, (math.trunc(num))))
