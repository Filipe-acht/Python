'''
Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().
'''


frase = 'Curso em Video Python'
print(frase[1:12])
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
#print(len(frase.strip())) #remove os espaços em branco
print(frase.replace('Python', 'Android'))
#frase = frase.replace('Python', 'Android')
print('Curso' in frase)
print(frase.find('Video')) #retorna a posição se existir
print(frase.split()) #cria uma lista
dividido = frase.split()
print(dividido[2][3])