lanche = ['hamburgue', 'suco', 'pizza', 'picole']

lanche.append('biscoito') # cria um novo elemento 'biscoito' na posição
lanche.insert(0, 'cachorro-quente') # cria um novo elemento na posição 0 e reorganiza as posições

# lista atual : lanche = ['cachorro-quente','hamburgue', 'suco', 'pizza', 'picole', 'biscoito']

del lanche[3] #Elimina o elemento da posição 3, no caso a pizza e reorganiza as posições.
lanche.pop() #Normalmente usado par eliminar o último elemento, mas pode ser usado com parametro para eliminar o indice desejado.

if 'pizza' in lanche:
    lanche.remove('pizza') #Elimina pelo conteudo.
