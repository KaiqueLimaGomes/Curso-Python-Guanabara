#Desafio041
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 25 anos: Sênior
# Acima: MASTER

from datetime import date

idade = int(input('Dgite o ano do seu nascimento: '))
ano = date.today().year

if ano - idade <= 9:
    print('Sua categoria é a MIRIM')
elif 9 < ano - idade <= 14:
    print('Sua categoria é INFANTIL')
elif 14 < ano - idade <= 19:
    print('Sua categoria é JUNIOR')
elif 19 < ano - idade <=25:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')
print('Bem-vindo a Confedereção Nacional de Natação!')
