#Desafio055
# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lido

listaPeso = []

for c in range(1,7):
    peso = float(input('Peso da {}º pessoa: '.format(c)))
    listaPeso.append(peso) #Adiciona o input dentro da lista listaPeso

listaPeso.sort() #Organiza a lista de forma crescente
print('O menor peso foi {}Kg e o maior foi {}Kg'.format(listaPeso[0], listaPeso[5]))