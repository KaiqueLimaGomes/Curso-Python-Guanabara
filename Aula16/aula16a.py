lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas são imutáveis, não alteram seu valor durante o programa.

# Primeira maneira lendo o tamanho de posições
# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]}')

# Segunda maneira de forma automática
# for comida in lanche:
#     print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche)) # mostra o valor lanche de forma ordenada.

print('Comi pra caramba!!')