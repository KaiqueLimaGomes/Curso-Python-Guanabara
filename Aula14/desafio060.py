#Desafio060
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# EX: 5! = 5x4x3x2x1 = 120

num = int(input('Digite um numero inteiro: '))
mult = num
cont = num
print('{}! = '.format(num), end='')

while cont >= 1:
    if cont > 1:
        print(cont, end='x')
        mult = mult * (cont - 1)
        cont -= 1
    else:
        print(cont, end='= ')
        cont -= 1
print(mult)


# MELHORIA DE CÓDIGO -> CHATGPT

# num = int(input('Digite um numero inteiro: '))
# cont = num
# mult = 1
#
# print(f'{num}! = ', end='')
#
# while cont >= 1:
#     print(cont, end='')
#     if cont > 1:
#         print('x', end='')
#     else:
#         print(' = ', end='')
#     mult *= cont
#     cont -= 1
#
# print(mult)

# CÓDIGO DO GUANABARA-> CHATGPT
#
# from math import factorial
#
# n = int(input('Digite um número para calcular seu Fatorial: '))
# c = n
# f = 1
#
# while c > 0:
#    print('{}'.format(c), end='')
#    print(' x ' if c > 1 else ' = ', ende='' )
#    f *= c
#    c -= 1
