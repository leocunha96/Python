#exercicio calculadora com + - * /

parametro = 's'
i = 0
j = 0

while (parametro == 's') or (parametro == 'S'): 
    
    i = 0

    while i == 0:
        numeroA = input ('Digite o primeiro numero: ')
    
        if numeroA.isdigit():
            i = 1
            numeroA = float (numeroA)

        else:
            print('Caractere inválido, digite um número válido!')
    i = 0

    while i == 0:

        numeroB = input ('Digite o segundo numero: ')

        if numeroB.isdigit():
            i = 1
            numeroB = float (numeroB)

        else:
            print('Caractere inválido, digite um número válido!')
    i = 0
    
    resultado = 0
    resultado = float (resultado)
    
    while i == 0 :
        operacao = input ('Digite a operação desejada: ')
        opcoes = '+-*/'
        if  (('+' in operacao) or ('-' in operacao) or ('*' in operacao) or ('/'in operacao)) :
        
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
            
            i = 1
        
        else:
            print ('Operador inválido, digite novamente:')
    i = 0
    print ('\n\n')
    parametro = input ('Deseja utilizar a calculadora?\nDIgite s para SIM e n para NÃO! ')
