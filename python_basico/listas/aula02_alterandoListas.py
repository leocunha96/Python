#CRUD --> Create, Ready, Update, Delete

#métodos úteis ---> append, insert, pop, del, clear, extend, +

#append -- adiciona um item ao final

#insert -- adiciona um item no indice escolhido

#pop -- remove do final ou do indice escolhido

#del -- deleta um indice

#clear -- limpa a lista

#extend -- extende a lista

#+ -- concatena listas

lista = [10,20,30,40] #create

print (lista) #ready

lista [2] = 300 #update 

print (lista) 

del lista [2] #delete

print (lista) #veja que o indice 2 na lista é deletado
# dependendo do tamanho da lista, isso exige muito processamento, pq move todos os itens da lista
#uma lista é comum adicionar ou retirar coisas da lista, e não mudar dados dela, pq exige processamento


lista.append(50) #como tudo em python é objeto, temos metodos para tudo
lista.append(60) #aqui é adicionado elementos no final da lista
lista.append(70) #nao exige quase nada de processamento, pois adiciona ao final

print (lista)

ultimoValor = lista.pop() #remove o ultimo elemento da lista

print(lista, 'Removido', ultimoValor) #removeu o 70 no caso

#quando a lista não é tão grande é possivel realizar algumas outras operações pois nao afetara tanto no processamento

lista.insert(0, 5) #inserindo no indice 0, o numero 5

print (lista) #veja que ele empurrou todos os indices para poder adicionar o numero 5 no indice selecionado.

listaA = [1,2,3]
listaB = [4,5,6]

listaC = listaA + listaB

print (listaC) #concatenou as listas atraves do +

listaD = listaA.extend(listaC) #retorna none, pois vc executou uma ação que nao retorna nada. Ele extende a lista que chama a ação, no casa a listaA

print(listaD)

print(listaA)