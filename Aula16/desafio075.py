#Desafio075
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

# A) Quantas vezes apareceu o valor 9
print(f'O número 9 apareceu {num.count(9)} vezes.')

# B) Em que posição foi digitado o primeiro valor 3.
if 3 in num:
       print(f'O primeiro número 3 foi digitado na posição {num.index(3)+1}')
else:
       print('O valor 3 não foi digitado em nenhuma posição.')
# C) Quais foram os números pares.
print('Os valores pares digitados foram ', end= ' ')
for n in num:
       if n % 2 == 0:
              print(n, end =' ')
