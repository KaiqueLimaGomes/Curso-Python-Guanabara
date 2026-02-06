for c in range(0,6):
    print('Oi')
print('FIM')

for c in range(1, 6): #conta de 1 a 5
    print(c)
print('FIM 1')

for c in range(6, 0 , -1 ): #Conta de 6 a 0 (Descrecente), necessario adicionar -1
    print(c)
print('FIM 2')

for c in range (0, 10 , 2): #Conta de 0 a 10 (Pulando de 2 em 2), PARA NO 8
    print(c)
print('FIM 3')

n = int(input('Digite um numero: '))
for c in range(0 , n): #Define o range de 0 até o valor de N
    print(c)
print('FIM 4')

#Recebe a entrada da contagem inicial (i), contagem final (f) e passos (p), O f+1 é para ir até a contagem real de f.
i = int(input('Inicio: '))
f = int(input('Final: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('FIM 5')
