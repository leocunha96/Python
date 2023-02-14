#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []

def calculoMedia (lista) :
    parametro = 0
    parametro = float (parametro)
    for numero in lista :
        numero = float (numero)
        parametro += numero
    return (parametro / 4)

print ("Programa para calculo da média semestra!\n")
i = 1

while i < 5 :
    numero = input (f"Digite a {i}ª nota: ")
    notas.append(numero)
    i += 1

media = (calculoMedia(notas))

print (f'A média do aluno é: {media}')

