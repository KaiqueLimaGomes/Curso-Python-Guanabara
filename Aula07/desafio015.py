#Desafio015
#Escreva um programa que pergunte a quantiade de KM percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado.

km = float(input('Qual a quantidade de km percorrido: '))
dia = int(input('Qual a quantidade de dias alugados: '))
custo = (dia * 60) + (km * 0.15)

print('O valor do carro alugado por {} dias e {}Km é de R${:.2f}'.format(dia, km, custo))