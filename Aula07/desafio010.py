#Desafio010
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$ 1,00 = R$ 3,27
r = float(input('Digite quantos Reias você quer converter: R$'))
d = 3.27
c = r/d
print('R${:.2f} dar para comprar US${:.2f} '.format(r, c))
