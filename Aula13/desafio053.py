#Desafio053
#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
#desconsiderendo os espaços.
#EX:APOS A SOPA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # Cria uma lista
junto = ''.join(palavras) #une a lista sem espaços
inverso = ''

for letra in range(len(junto) - 1, -1, -1): #ultima letra, até a primeira, voltando 1 letra
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('A frase É UM PALÍNDROMO')
else:
    print('A frase NÃO é um palíndromo')
