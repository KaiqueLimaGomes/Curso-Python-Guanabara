#Desafio042
# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tippo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

reta1 = int(input('Digite o valor da primeira reta: '))
reta2 = int(input('Digite o valor da segunda reta: '))
reta3 = int(input('Digite o valor da terceira reta: '))

lista = [reta1, reta2, reta3]
lista.sort()

if lista[2] < lista[0] + lista[1]:
    print('Essas medias formam um Triângulo!')
    if reta1 == reta2 == reta3:
        print('As medidas são de um triângulo Equilátero.')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('As medidas são de um triângulo Isósceles.')
    elif reta1 !=  reta2 != reta3:
        print('As medidas são de um triangulo Escaleno.')
else:
    print('Essas medidas NÃO formam um Triângulo!')
