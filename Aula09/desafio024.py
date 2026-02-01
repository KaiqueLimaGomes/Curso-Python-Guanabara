#Desafio024
#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de uma cidade: '))
cidade = cidade.strip()
cidade = cidade.upper()
print(cidade[:5] == 'SANTO')
