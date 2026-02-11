#Desafio062
# Melhore o DESAFIO 061, perguntando para o usuário se quer mostrar mais termos.
# O Programa encerra quando ele disser que quer mostrar 0 termos.

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

termos = 10
contador = 1
total = 0

while termos != 0:
    total += termos

    while contador <= total:
        print(primeiro, end=', ')
        primeiro += razao
        contador += 1

    termos = int(input("\nQuantos termos a mais? "))

print("Programa encerrado.")
