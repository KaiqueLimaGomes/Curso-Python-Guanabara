#Desafio018
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('digite um ângulo qualquer: '))
seno = math.sin(math.radians(angulo))
cos = math.sin(math.cos(angulo))
tan = math.sin(math.tan(angulo))
print('O ângulo {}º tem como:\n SENO {:.2f}\n COSSENO {:.2f}\n TANGENTE {:.2f}'.format(angulo, seno, cos, tan))
