#Desafio087
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha

matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]

total = terceira = maior =  0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('\n')
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')

        if matriz[linha][coluna] % 2 == 0:
            total += matriz[linha][coluna]
    print()

# A) A soma de todos os valores digitados.
print(f'O valor dos números digitados é {total}.')

# B) A soma dos valores da terceira coluna
for l in range(0,3):
    terceira += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {terceira}.')

# C) O maior valor da segunda linha
if matriz[1][0] > matriz[1][1] and matriz[1][0] > matriz[1][2]:
    maior += matriz[1][0]
elif matriz[1][1] > matriz[1][2]:
    maior += matriz[1][1]
else:
    maior += matriz[1][2]

print(f'O maior da segunda linha é {maior}.')
