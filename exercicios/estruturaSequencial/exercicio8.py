#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

def calculoSalario (valorHora, horasTrabalhadas) :
    valorHora = float (valorHora)
    horasTrabalhadas = float (horasTrabalhadas)
    salario = valorHora * horasTrabalhadas
    return salario

valorHora = input ('Informe quanto você ganha por hora: ')
horasTrabalhadas = input ('Informe quantas horas você trabalhou durante o mês: ')
salario = calculoSalario (valorHora, horasTrabalhadas)
print (f'O seu salário para este mês será de: R$ {salario}')

