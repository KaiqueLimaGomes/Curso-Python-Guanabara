#Desafio067
# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando
# o número solicitado for NEGATIVO.

n = cont = 0

while True:
    n = int(input('Quer ver a tabuada de qual número: '))
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{n} x {cont} = {n*cont}')
    print('--'*20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')