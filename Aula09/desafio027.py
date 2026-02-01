#Desafio027
#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
#Primeiro: Ana
#Último: Souza

nome = str(input('Digite seu nome completo: '))
nome = nome.strip()
nc = nome.split()
tam = len(nc)-1
print('Seu primeiro nome é {}!'.format(nc[0]))
print('Seu ultimo nome é {}!'.format(nc[tam]))
#print('Seu ultimo nome é {}'.format(nc[len(nc)-1])) #Resolução Professor