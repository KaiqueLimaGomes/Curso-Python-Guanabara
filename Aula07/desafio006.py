#Desafio 006
#Crie um algoritimo que leia um número e mostre  o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
q = n ** (1/2)
print('Seu numero é {}, o drobo é {},'.format(n, d), end=' ')
print('o triplo é {} \n E a r aiz quadrada de {} é {:.2f} '.format(t, n, q))