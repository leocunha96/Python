#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

def calculoArea(raio):
    pi = 3.14
    calculo =  pi*(raio**2)
    return calculo

raio = input ('Informe o valor do raio para cálculo da sua área: ')
raio = float (raio)

area = calculoArea(raio)

print (f'A área do circulo de raio {raio} é igual a {area}.')