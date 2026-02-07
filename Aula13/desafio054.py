#Desafio054
#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.
from datetime import date


maiores = 0
menores = 0

for c in range(1, 8):
    nasc = int(input('Ano de nascimento da {}º pessoa: '.format(c)))
    if date.today().year - nasc > 18:
        maiores += 1
    else:
        menores += 1
print('Dentro do grupo das 7 pessoas, {} são maiores e {} são menores de idade.'.format(maiores, menores))
