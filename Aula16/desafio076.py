#Desafio076
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 29.99,
         'Estojo', 25,
         'Transferidor', 5.50,
         'Compasso', 9.99,
         'Mochila', 159.80,
         'Canetinhas', 22.40,
         'Livro', 27.60)

print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)

for pos in range (0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-' * 40)