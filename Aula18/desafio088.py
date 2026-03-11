#Desafio088
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em lista composta.

from random import randint

jogos = []

num = int(input('Quantos jogos você quer que eu sorteie? '))

for c in range(num):
    jogo = []

    for n in range(0,6):
        sorteio = randint(1, 60)
        if sorteio not in jogo:
            jogo.append(sorteio)

    jogo.sort()
    jogos.append(jogo)

for i, jogo in enumerate(jogos):
    print(f'Jogo {i + 1}: {jogo}')
