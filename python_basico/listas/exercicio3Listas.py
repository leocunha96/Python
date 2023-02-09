""""
Gerador primeiro digito do CPF

ex CPF : 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF multiplicando 
cada  um dos valores por uma contagem regressiva começando
de 10.

10  9  8  7  6  5  4  3  2 

7   4  6  8  2  4  8  9  0 

70 36 48 56 16 20 32 27  0


SOMA DOS NUMEROS = 70+36+48+56+16+20+32+27+0 = 301

Multiplicar o resultado anterior por 10 = 3010

Obter o resto da divisão da conta anterior por 11: 3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resulta é 0
Senão:
    resultado é o valor da conta
"""

cpf = '746.824.890-70'
cpfCorrigido = []
somatorio = 0
multiplicador = 10

for digito in cpf:
    if digito.isdigit():
        cpfCorrigido.append(digito)

cpfCorrigido.pop()
cpfCorrigido.pop()

    
print (cpfCorrigido)

for i in cpfCorrigido :
    
    i = int(i)
    produto = multiplicador * i
    multiplicador -= 1
    
    somatorio += produto

multiplicador = 10
resultado = multiplicador * somatorio

resultado = resultado % 11
primeiroDigito = 0

primeiroDigito = 0 if resultado > 9  else resultado 
print (primeiroDigito)
