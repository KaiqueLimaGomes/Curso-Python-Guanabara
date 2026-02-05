#Desafio044
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
# preço normal e condição de pagamento:
# - à vista Dinheiro / Cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: sem juros
# - 3x ou mais no cartão: 20% de juros

produto = float(input('Digite o preço do produto: R$'))
opcao = int(input('Qual a forma de pagamento:'
                  '\n 1 - à vista Dinheiro ou cheque, 10% de desconto'
                  '\n 2 - à vista no cartão, 5% de desconto'
                  '\n 3 - em até 2x no cartão, sem juros'
                  '\n 4 - 3x ou mais vezes no cartão com 20% de juros'
                  '\n Escolha um opção: '))

if opcao == 1:
    print('O valor do produto à vista no dinheiro ou cheque com 10% de desconto fica R${:.2f}'.format(produto - (produto * 10 / 100)))
elif opcao == 2:
    print('O valor do produto á vista no cartão, com 5% de desconto fica R${:.2f}'.format(produto - (produto * 5 / 100)))
elif opcao == 3:
    print('O valor do produto em até 2x no cartão sem juros fica R${:.2f}'.format(produto))
elif opcao == 4:
    print('O valor do produto em 3x ou mais, com 20% de juros, fica R${:.2f}'.format(produto + (produto * 20 / 100)))
else:
    print('\033[31mOpção Inválida!\033[m')