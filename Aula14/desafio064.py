#Desafio064
# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma ente eles (desconsiderando o flag)

n = 0
soma = 0
cont = 0

while n!= 999:
    n = int(input("digite um número inteiro: "))
    soma += n
    cont += 1

print('Você digitou {} números e soma de todos eles foi {}'.format(cont - 1, soma - 999))
