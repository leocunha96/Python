#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

def conversao (fahr) :
    fahr = float (fahr)
    valor = (fahr - 32) / 9
    valor *= 5
    return valor

x = input ("Informe o valor em Fahrenheit que deseja converter para Celsius: ")
valorConvertido = conversao(x)
print (f'{x}°F equivalem a {valorConvertido:.2f}ºC')
