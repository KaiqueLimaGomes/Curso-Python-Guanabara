#Desafio011
#Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta um área de 2m².

largura = float(input('Qual a largura da parede em metros: '))
altura = float(input('Qual a altura da parede em metros: '))
area = largura * altura
tinta = 2 #valor que cada litro de tinta pinta um área por m²
litro = area/tinta
print('Para pintar um parede com {:.2f} m² será necessário {:.2f} litros de tinta.'.format(area, litro))