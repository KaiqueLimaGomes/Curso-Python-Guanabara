n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999: #Verifica se entrada do número é a BANDEIRA (FLAG) de saída antes de somar.
        break   #Comando de saída do Loop.
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}') #PEP F String, novo modelo de declaração python 3.6