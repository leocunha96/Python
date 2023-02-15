#Faça um Programa que converta metros para centímetros.

def conversao (valor, tipo) :
    
    if tipo == 'm' :
        valor = float (valor)
        resultado = valor * 100
        return resultado
    elif tipo == 'cm' :
        valor = float (valor)
        resultado = valor / 100
        return resultado
    else :
        resultado = 'Tipo incorreto'
        return resultado

tipo = input ('Informe o tipo que será convertido convertido, sendo m (metros) e cm (centimetros): ')
valor = input ('Informe o valor que deseja converter: ')
resultado = conversao(valor,tipo)
print (f'O valor convertido é {resultado}')