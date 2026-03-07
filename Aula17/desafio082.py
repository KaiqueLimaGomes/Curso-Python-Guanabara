#Desafio082
# Crie um programa que vai ler vários números e colocar numa lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e valores impares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
impares = []
pares = []

while True:
    lista.append(int(input('Digite um valor: ')))
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break

for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'Os valores que você digitou foi {lista}')
print(f'Os valores PARES são {pares}')
print(f'Os valores ÍMPARES são {impares}')