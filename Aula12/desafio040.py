#Desafio040
#Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma menssagem no final,
# de acordo com a média atingida:
# - Média abaixo de 5.0 : REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Digite o valor da sua primeira nota: '))
n2 = float(input('Digite o valor da sua segunda nota: '))
media = (n1+n2) / 2

if media < 5.0:
    print('\033[41mREPROVADO! Estude mais para a proxima vez, sua média foi {:.2}!\033[m'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('\033[43mRECUPERAÇÃO! Se esforçe para passar! Sua média foi {:.2}!\033[m'.format(media))
elif media >= 7.0:
    print('\033[42mAPROVADO! Parabéns! Sua média foi {}!\033[m'.format(media))
else:
    print('\033[41mEntrada inválida!\033[m')