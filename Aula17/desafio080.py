#Desafio080
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os numa lista,
# já na posição correta de inserção, (sem usar o sort()).
# no final, mostre a lista ordenada na tela.

lista = []

for cont in range(5):
    num = int(input('Digite um valor: '))

    if lista == []:
        lista.append(num)
        print('Adicionado')
    else:
        for pos, v in enumerate(lista):
            if num <= v:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos}')
                break
        else:
            lista.append(num)
            print('Adicionado ao final')

print(lista)
