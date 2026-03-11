galera = list()
dado = list()
totmai = totmen = 0
for c in range(1,4):
    dado.append(str(input(f'Pessoa {c} nome: ')))
    dado.append(int(input(f'Pessoa {c} idade: ')))
    galera.append(dado[:]) # sem o [:] para criar a cópia de dados ele irá apagar nas duas lista quando roda o clear()
    dado.clear()
print(galera)
print('\n')

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade ')
