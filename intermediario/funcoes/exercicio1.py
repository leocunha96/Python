'''
crie uma função que multiple todos os argumentos nao nomeados recebidos.
Retorne o total para uma variável e mostre a variavel com o resultado.

Crie outra função que diga que o numero é par ou impar, e retorne par ou impar.

'''


def produto (*args) :
    
    lista = list(args)

    if '0' in lista :
        resultado = 0
        return resultado
    
    else :
        resultado = 1
        for numero in lista :
            resultado *= numero
        return resultado


def parImpar (numero) :
    if numero % 2 == 0 :
        return 'Par'
    else: 
        return 'Impar'


numero = produto (1,2,3,4,8)
print (numero)


tipo = parImpar (numero)
print (tipo)