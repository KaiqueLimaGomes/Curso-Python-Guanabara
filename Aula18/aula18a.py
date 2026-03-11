pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
              #0     #1      #0     #1      #0    #1
                  #0            #1             #2

print(pessoas[0][0]) #print do elemento zero em seguida o elemento zero da segunda lista "PEDRO"
print(pessoas[1][1]) #print do elemento 1 na primeira lista e o elemento 1 da segunda lista "19"
print(pessoas[2][0]) #print do elemento 2 na primeira lista e o elemento 0 da segunda lista "João"
print(pessoas[1]) #printo do elemento 1 inteiro da primeira lista "['Maria', 19]"

print('\n', '-*-' * 30, '\n')

for p in pessoas : # para cada Pessoa em Pessoas
    print(p) #imprime pessoa
    print(f'{p[0]} tem {p[1]} anos de idade.') # imprime: NOME tem IDADE anos de idade.
