#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

def calculo (altura) :
    pesoIdeal = (altura*72.7)-58
    return pesoIdeal

getAltura = input ('Informe sua altura para verificação do seu peso ideal: ')
getAltura = float (getAltura)
peso = calculo(getAltura)

print (f'Para a altura de {getAltura} m, o peso ideal recomendado é de {peso:.2f} kg')
