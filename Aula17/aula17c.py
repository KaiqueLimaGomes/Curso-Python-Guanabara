valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a #Não faz uma cópia da lista e sim uma ligação!
b[2] = 8 # Então se você alterar em B antera em A
b = a[:] # B recebe todos os itens de A, aí sim faz uma cópia de A em B.
print(f'Lista A: {a}')
print(f'Lista B: {b}')