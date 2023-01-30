nome = input('Qual o seu nome? ')
a = input('Digite um numero ')
b = input('Digite outro numero ')
print(f'O seu nome é {nome=}') #colocar o igual vai imprimir o nome da variavel mais o valor dela
print(f'A soma de {a} com {b} é igual a {a+b}')

#Desta forma, será imprimido a concatenção dos numeros para a e b. Pois são strings
#Uma solução é fazer a type cast, veja:

a = int(a)
b = int(b)

print(f'A soma de {a} com {b} é igual a {a+b}')

#porem, por enquanto, se inserirmos uma letra para os numeros, o programa ai crashar. Ainda será aprendido como consertar isso!
