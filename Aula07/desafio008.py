#Desafio008
#Escreva um programa que leia um valor em metros e o exiba convertido em centimetos e milimetros.
m = float(input('Digite uma medida em metros: '))


km = m / 1000 #Quilômetro
hm = m / 100  #Hectômetro
dam = m / 10  #Decâmetro
dm = m * 10   #Decímetro
cm = m * 100  #Centímetro
mm = m * 1000 #Milímetro

print('{} metros em \n centimetros é {:.0f} cm \n milímetros é {:.0f} mm\n'.format(m, cm, mm))
print('A medida de {}m corresponde a:\n {} Quilômetro\n {} Hectômetro\n {} Decâmetro\n'.format(m, km, hm, dam), end='')
print(' {:.0f} Decímetro\n {:.0f} Centímetro\n {:.0f} Milímetro'.format(dm, cm, mm))