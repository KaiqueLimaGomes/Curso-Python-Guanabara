#Desafio069
# Crie um programa que leia a idade e o sexo de VÁRIAS PESSOAS.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

continuar = ' '
maioridade = 0
homens = 0
mulher = 0

while True:
    print('--'*10)
    print('Cadastre uma pessoa')
    print('--'*10)

    idade = int(input('Idade: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

    if idade >= 18:
        maioridade += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade <= 20:
        mulher += 1

    while continuar not in 'SN':
        continuar = str(input('Quer conitnuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Foram cadastradas {maioridade} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastradas {mulher} mulheres com menos de 20 anos')
