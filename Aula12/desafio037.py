#Desafio037
#Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite um numero inteiro qualquer: '))
opcao =int(input('Escolha qual a opção que será a base de conversão'
      '\n 1 para binário'
      '\n 2 para octal'
      '\n 3 para hexadecimal'
      '\n opção: '))

if opcao == 1:
    print('O número {} na base binária é {}.'.format(num, bin(10)[2:]))
elif opcao == 2:
    print('O número {} na base octal é {}^8.'.format(num, oct(num)))
elif opcao == 3:
    print('O número {} na base hexadecimal é {}.'.format(num, hex(num)[2:].upper()))
else:
    print('\033[0;30;41mOpção inválida!!\033[m')
