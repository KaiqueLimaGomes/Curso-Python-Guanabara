#Desafio029
#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Digite a velocidade do carro: '))

if vel > 80:
    multa = ((vel - 80)* 7)
    print('Você passou {} Km/h a cima do permitido, você receberá uma multa de R${:.2f}!'.format((vel-80), multa))
print('Você passou dentro do limite de velocidade!')
