#Desafio079
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os numa lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista=[]

while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor Duplicado! Não vou adicionar...')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso.')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
print('-*-'*20)
lista.sort()
print(f'Você digitou os valores {lista}')
