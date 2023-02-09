
#introdução ao desempacotamento + tuples (tuplas)

#nomes = ['maria', 'helena', 'luiz'] #é possivel fazer assim

#nome1, nome2, nome3 = nomes

#ou 

_, nome2, *resto = ['maria', 'helena', 'luiz', 'leonardo'] #o _ ignora o indice, e o *resto  é a maneira de guardar o restanto que não é pego, convencionalmente usasse tbm _

print(nome2)

print(resto)

#tipo tupla - uma lista imutavel, ou seja, que vai se manter e não se alterar.


#a tupla pode ser criada usando parenteses ao inves de colchetes, ou sem nada.

#é possivel converter uma lista também para tupla

lista  = ['leonardo', 'augusto', 'cunha']

nomes = tuple(lista)

print (nomes)

