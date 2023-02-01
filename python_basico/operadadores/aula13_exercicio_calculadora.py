#exercicio calculadora com + - * /

parametro = 's'

while (parametro == 's') or (parametro == 'S'): 
    
    numeroA = input ('Digite o primeiro numero: ')
    numeroB = input ('Digite o segundo numero: ')
    operacao = input ('Digite a operação desejada: ')
    resultado = 0
    numeroA = float (numeroA)
    numeroB = float (numeroB)
    resultado = float (resultado)

    if operacao == '+':
        resultado = numeroA + numeroB
        print (f'O resultado da adição de {numeroA} com {numeroB} é: {resultado}')
    elif operacao == '-':    
        resultado = numeroA - numeroB
        print (f'O resultado da subtração de {numeroA} com {numeroB} é: {resultado}')
    elif operacao == '*':    
        resultado = numeroA * numeroB
        print (f'O resultado da multiplicação de {numeroA} com {numeroB} é: {resultado}')
    elif operacao == '/':    
        resultado = numeroA / numeroB
        print (f'O resultado da divisão de {numeroA} com {numeroB} é: {resultado}')
    else:
        print ('Operador inválido')
    print ('\n\n')
    parametro = input ('Deseja utilizar a calculadora?\nDIgite s para SIM e n para NÃO! ')
