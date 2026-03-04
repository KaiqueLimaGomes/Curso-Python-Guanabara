#Desafio073
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 Colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time chapecoense.

tabela = ('Palmeiras', 'São Paulo', 'Corinthians', 'Bahia', 'Fluminense', 'Athletico_PR', 'Bragantino', 'Grêmio', 'Chapecoense', 'Mirassol',
          'Flamengo', 'Coritiba', 'Santos', 'Botafogo', 'EC Vitória', 'Remo', 'Atlético-MG', 'Internacional', 'Cruzeiro', 'Vasco da Gama')

print('Lista do Brasileirão: ', tabela)

print('-=-'*20)
# A) Apenas os 5 primeiros colocados.
print('Os 5 primeiros colocados são: ', tabela[0:5])

print('-=-'*20)
# B) Os últimos 4 Colocados da tabela.
print('Os 4 últimos colocados são: ',tabela[-4:])

print('-=-'*20)
# C) Uma lista com os times em ordem alfabética.
print('Times em ordem alfabética: ' ,sorted(tabela))

print('-=-'*20)
# D) Em que posição na tabela está o time chapecoense.
print(f'O Chapecoense está na {tabela.index('Chapecoense')+1}ª posição.')