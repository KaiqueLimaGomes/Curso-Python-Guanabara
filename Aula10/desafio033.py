#Desafio033
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('terceiro número: '))

ordem = [n1, n2, n3]
ordem.sort() #Ordena os números da lista em ordem crescente

if ordem[0] == ordem[2]:
    print('Os três valores são iguais')
else:
    print('O maior número é {} e o menor é {}'.format(ordem[2], ordem[0]))