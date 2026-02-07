#Desafio055
# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lido

listaPeso = []

for c in range(0,6):
    peso = float(input('Digite seu peso: '))
    listaPeso.append(peso) #Adiciona o input dentro da lista listaPeso

listaPeso.sort() #Organiza a lista de forma crescente
print('O menor peso foi {}Kg e o maior foi {}Kg'.format(listaPeso[0], listaPeso[5]))