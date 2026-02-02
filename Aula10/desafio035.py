#Desafio035
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não forma um triângulo.

r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('segunda reta: '))
r3 = int(input('terceira reta: '))

lista = [r1, r2, r3]
lista.sort()

if lista[2] < lista[0] + lista[1]:
    print('Essas medias formam um Triângulo!')
else:
    print('Essas medidas NÃO formam um Triângulo!')
