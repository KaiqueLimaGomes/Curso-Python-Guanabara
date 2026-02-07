#Desafio051
# Desenvolva um programa que leia o primeiro termo e a razão de um PA.
# No final mostre os 10 primeiros termos dessa progressão.

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
print(termo, end=',')
for c in range(0, 10):
    termo += razao
    print(termo, end=',')
