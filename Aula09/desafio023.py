#Desafio023
#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#EX: Digite um número: 1834
#Unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1

num = int(input('Digite um número entre 0 a 9999: '))

#tentativa por matematica
und = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print('Milhar: ', mil)
print('Centena: ', cen)
print('Dezena: ', dez)
print('Unidade: ', und)
print('________________________')

#Tentativa por STRING, dá erro se o número for menor que 1000
num = str(num)
num = num.strip() #Elimina espaços vazios desnecessários
print('Milhar: ', num[0])
print('Centena: ', num[1])
print('Dezena: ', num[2])
print('Unidade: ', num[3])
