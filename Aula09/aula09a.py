frase = 'Curso em Vídeo Python'
print(frase) #Imprime a string armazenada
print(frase[3]) #imprime o caracter da terceira possição 'S'
print(frase[3:13]) #imprime do terceiro caracter até 12, o 13 não contabiliza
print(frase[:10]) #imprime do inicio até o caracter 9, o 10 não cantabiliza
print(frase[10:]) #imprime da posição 10 até o final
print(frase[1:15:2]) #impre da posição 1 até a 14 pulando de 2 em 2, o 15 não contabiliza
print(frase[::2]) #imprime do inicio ao fim pulando de 2 em 2 posição

print(""" um 
texto 
grande 
de 
varias 
linhas
 aqui""")  # 3x" para imprimir um texto grande com um unico print

print(frase.count('o')) #Conta quantos caracteres semelhante o texto possui, Possui diferença em letra ALTA e baixa
print(frase.upper().count('O')) #Deixa o texto em caixa ALTA e procura todos os 'O'
print(frase.lower) #Deixa o texto em minisculo
print(len(frase)) #Conta quantidade de caracteres da string, inclusive espaços vazios antes e depois do texto
print(frase.strip()) #Remove espaços vazios indesejados antes e depois do texto, não remove o espaço entre palavras
print(frase.replace('Python', 'Android')) # Subistitui o primeiro valor pelo segundo
print(frase.find('em'))  #Procura o valor dentro da string, retorna a posição do caracter inicial da busca, case sensitive.
print(frase.split()) #Cria uma lista separando as palavras por espaço
dividido = frase.split()
print(dividido[2] [3]) #Pega o item dois da lista e mostra o terceiro caracter
