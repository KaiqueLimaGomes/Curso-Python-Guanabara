#Desafio043
# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule o seu IMC e mostre o seu status,
# de acordo com a tabela abaixo:
# abaixo de 18.5: Abaixo do peso
# entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input('Digite seu peso: Kg '))
altura = float(input('Digite sua altura: m '))
imc = peso/(altura * altura)

if imc <= 18.5:
    print('Seu IMC é {:.1f}, você está abaixo do peso.'.format(imc))
elif 18.5 < imc <= 25:
    print('Seu IMC é {:.1f}, você está no peso ideal.'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é {:.1f}, você está com Sobrepeso.'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é {:.1f}, você está com Obesidade.'.format(imc))
elif 40 < imc:
    print('Seu IMC é {:.1f}, você está com Obesidade Mórbida'.format(imc))
else:
    print('\033[0;31mEntrada inválida!\033[m')
