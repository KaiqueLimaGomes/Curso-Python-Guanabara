#Desafio050
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
pares = 0

for c in range(1, 7):
    num = int(input('Digite o {}º valor inteiro: '.format(c)))
    if num % 2 == 0:
        soma += num
        pares += 1
print('A soma dos {} números pares e a soma deles foi {}'.format(pares, soma))
print('FIM')
