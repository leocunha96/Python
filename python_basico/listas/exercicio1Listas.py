'''exibir os idices da lista
0 maria
1 helena
2 luiz
'''

lista = ['maria', 'helena', 'luiz']
i = 0

lista.append('joao')
for nome in lista :
    print ('Nome:',nome, 'Indice:',i)
    i += 1

#outra solução usando range

indices = range(len(lista))

for indice in indices:
    print (indice, lista[indice])