#Desafio017
#Faça um programa que leia o comprimento do cateto oposto edo cateto adjacente de um triângulo retângulo,
#Calcule e mostre o comprimento da hipotenusa
import math
from math import hypot

catOp = float(input('Digite o valor do cateto oposto: '))
catAd = float(input('Digite o valor do segundo cateto adjacente: '))
print('O comprimente da hiporenusa é {:.2f}.'.format(hypot(catOp, catAd)))
