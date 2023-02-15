'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7

'''

def calculo (altura, genero) :
    if genero == 'homem' :
        pesoIdeal = (altura*72.7)-58
        return pesoIdeal
    elif genero == 'mulher' :
       pesoIdeal = (altura*62.1)-44.7
       return pesoIdeal  
      

getAltura = input ('Informe sua altura para verificação do seu peso ideal: ')
getAltura = float (getAltura)
getGen = input ('Inforrme se você é homem ou mulher: ')
getGen = getGen.lower()
peso = calculo(getAltura, getGen)

print (f'Para a altura de {getAltura} m, o peso ideal para {getGen} é de {peso:.2f} kg')
