#Desafio056
# Desenvolva um program que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do mais velho
# - Quantas mulheres têm menos de 20 anos.

nome = ''
idade = 0
sexo = ''
media = 0
soma = 0
nomeVelho = 0
idadeVelho = 0
mulheres = 0

for c in range(1,5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]): ').upper()[0])

    soma += idade
    media = soma / c

    if sexo == 'H' and idade > idadeVelho:
        idadeVelho = idade
        nomeVelho = nome

    if sexo == 'M' and idade < 20:
        mulheres += 1

print('A  média de idade do grupo é {} anos.'.format(media))
print('O Homem mais velho é o {}, com {} anos.'.format(nomeVelho, idadeVelho))

if mulheres > 0:
    print('O grupo possui {} mulheres com menos de 20 anos.'.format(mulheres))
else:
    print('O Grupo não possui mulheres com menos de 20 anos.')