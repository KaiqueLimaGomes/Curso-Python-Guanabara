#Desafio049
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# contudo, agora utilizando um laço for.

print('-=-' * 10)
print('TABUADA'.center(30,' '))
print('-=-' * 10)

num = int(input('Digite o numero da tabuada: '))

for c in range(1, 11):
    print('{} x {} = {}'.format(c, num, c * num))
print('FIM')
