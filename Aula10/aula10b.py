nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!') #Só imprime essa mensagem se o nome atender a condição.
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))