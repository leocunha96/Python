#iterando strings com while


nome = input ('Qual é o seu nome? ')
tamanho = len (nome)
indice = 0
novo_nome = ''


while indice < tamanho: 
    letra = nome [indice]
    novo_nome += f'*{letra}'
    indice += 1
novo_nome += '*'    
print (novo_nome)
