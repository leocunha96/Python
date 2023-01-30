# comentario em pyhton, essas linhas o interpretador ignora

print(123) #comentario na frente

"""
escrever o que eu quiser
chama-se docString, o interpretador do python le isso aqui
"""
print(12, 34, sep = "\n", end = "\n") #argumento end se utilizando indica qual parametro final da funcao sera utilizado, ex quebra de linha
print(56, 78, sep ='-') #argumento sep se utilizando indica qual parametro de separador sera utilizado para espacamento
print ("strings vao dentro de aspas, simples ou duplas")
print ("Utilizando o \"Escape\"") #o escape permite representarmos as aspas ao executar uma strintg no printf
print (r"Utilizando o \"Escape\"") #o caractere r antes da string mostra inclusive as barras invertidas
print ('Utilizando "aspas duplas" dentro de aspas simples') #utilizar aspas duplas dentro de simples eh um jeito mais facil para imprimir as aspas
print ("Utilizando 'aspas simples' dentro de aspas duplas") #o contrario eh valido


print (type ('Leonardo')) #classe type indica o tipo do argumento recebido
print (10 == 10) #return true 
print (10 == 11) #return false