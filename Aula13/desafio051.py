#Desafio051
# Desenvolva um programa que leia o primeiro termo e a razão de um PA.
# No final mostre os 10 primeiros termos dessa progressão.

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
final = termo + (10 - 1 ) * razao
for c in range(termo, final + razao, razao):
    print(c, end=',')
print('FIM')
