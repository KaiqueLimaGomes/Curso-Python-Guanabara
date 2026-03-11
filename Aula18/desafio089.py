#Desafio089
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = []
aluno = []

while True:
    nome = str(input('Nome: '))
    aluno.append(nome)
    nota1 = float(input('Nota 1: '))
    aluno.append(nota1)
    nota2 = float(input('Nota 2: '))
    aluno.append(nota2)
    boletim.append(aluno[:])
    aluno.clear()

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if opcao == 'N':
        break

print('**'*30)
print('No.  Nome    Média')
for pos, aluno in enumerate(boletim):
    print(f'{pos}')
    for nota in boletim[]:
        print(f'{boletim[nota]}')