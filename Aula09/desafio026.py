#Desafio026
#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase qualquer: '))
frase = frase.strip()
frase = frase.lower()
print('A letra "A" apareceu {} vezes'.format(frase.count('a')))
print('O primeiro "A" aparenceu na posicição {}'.format(frase.find('a')+1)) #adicionar +1 para não contar apartir do zero
print('O Último "A" apareceu na posição {}'.format(frase.rfind('a')+1))
