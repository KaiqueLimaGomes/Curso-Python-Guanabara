#Desafio020
#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
#Faça um programa que leia o nome dos quatro alunos e msotre a ordem sorteada.
import random
from random import shuffle

nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
ordem = random.shuffle(lista)
print('A ordem de apresentação será 1ª {}, 2ª {}, 3ª {} e 4ª {}.'.format(lista[0], lista[1], lista[2], lista[3]))
