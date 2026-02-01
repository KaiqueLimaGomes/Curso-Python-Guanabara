#Desafio022
#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas.
#O nome com todas as letras minúsculas.
#Quantas letras ao todo(sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome Completo: '))
nome = nome.strip() #Elimina espaços vazios desnecessários, para não influenciar no item 3.
print('Em maiúsculo: {}'.format(nome.upper()))
print('Em minúsculo: {}'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(''.join(nome.split())))) #Meu RACIOCÍNIO!!
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' '))) #Suguestão mais simples e funcional!
print('Seu primeiro nome tem {} letras'.format(len(nome.split()[0])))  #Pode chamar a função e selecionar a posição da lista depois.
