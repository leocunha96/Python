#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#F = C x 1,8 + 32

def conversao (celsius) :
    celsius= float (celsius)
    valor = (celsius * 1.8) + 32
    return valor

x = input ("Informe o valor em Celsius que deseja converter para Fahrenheit: ")
valorConvertido = conversao(x)
print (f'{x}°C equivalem a {valorConvertido:.2f}ºF')
