#Desafio061
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura WHILE.

# termo = int(input("Digite o primeiro termo: "))
# razao = int(input("Digite a razão: "))
# final = termo + (10 - 1 ) * razao
# for c in range(termo, final + razao, razao):
#     print(c, end=',')
# print('FIM')

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
cont = 1

while cont < 11:
    if cont > 9:
        print(termo, end='.')
    else:
        print(termo, end=',')
    termo += razao
    cont += 1