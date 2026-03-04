a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c)) #quantas posições tem o C
print(c.count(5)) # quantas vezes o n 5 está aparencendo (2 vezes)
print(c.index(8)) # em que posição está o n 8 (posição 1)
print(c.index(5,1)) # retorna a posição do n 5 apartir da posição (retorna posição 5)

pessoa = ('Kaique', 28, 'M', 71.50)
# del(pessoa)  # Comando para apagar uma variavel, unica modificação aceita. Não apaga item dentro da tupla.