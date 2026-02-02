#Desafio031
#Desenvolva um programa que pergunte a distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
#e R$0,45 para viagens mais longas.

km = float(input('Digite a distância da viagem, Km '))

if km <= 200:
    print('O valor da passagem para {:.0f}Km é de R${:.2f}'.format(km, (km * 0.50)))
else:
    print('O valor da passagem para {:.0f}Km é de R${:.2f}'.format(km, (km * 0.45)))
