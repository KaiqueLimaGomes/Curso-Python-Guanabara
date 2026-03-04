#Desafio072
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extenso, de ZERO até VINTE.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla  = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco',
          'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
          'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
          'Dezesseis', 'Dezessete', 'Dezoito',' Dezenove', 'Vinte')

Continuar = 'S'

while True:
    num = int(input('Digite um número entre 0 e 20: '))

    if num < 0 or num > 20:
       print('Número inválido, tente novamente!')

    else:
        print(f'Você digitou o número {tupla[num]}.')
        continuar = (str(input('Deseja continuar? [S/N]: '))).upper().strip()[0]
        if continuar != 'S':
            break
