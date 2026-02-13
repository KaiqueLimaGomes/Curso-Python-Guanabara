#Desafio063
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
# de uma sequência de Fibonacci.

n= int(input('Digite quantos termos você quer mostrar: '))
t1 =0
t2 = 1
t3 = 0
cont= 3

print('{}, {}'.format(t1, t2), end=', ')

while cont <= n:
    t3 = t1 + t2
    if cont < n:
        print(t3, end=', ')
    else:
        print(t3, end='.')
    t1= t2
    t2= t3
    cont += 1
