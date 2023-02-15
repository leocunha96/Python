#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def calculoArea(lado):
    calculo =  lado**2
    return calculo

lado = input ('Informe o valor do lado do quadrado para cálculo da sua área: ')
lado = float (lado)

area = calculoArea(lado)
dobroArea = area * 2

print (f'A área do quadra de lado {lado} é igual a {area}. O dobro desta área é igual a {dobroArea}.')