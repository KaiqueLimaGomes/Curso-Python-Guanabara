teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:]) # SEM o [:], ele não cria uma cópia aparte
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) # SEM o [:], ele não cria uma cópia aparte
print(galera)
