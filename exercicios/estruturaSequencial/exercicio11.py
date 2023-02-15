'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.

'''

int1 = input ('Informe o primeiro numero inteiro: ')
int1 = int (int1)
int2 = input ('Informe o segundo numero inteiro: ')
int2 = int (int2)
real1 = input ('Informe um numero real: ')
real1 = float (real1)

calculo1 = (int1*2)*(int2/2)
calculo2 = (int1*3)+real1
calculo3 = real1 ** 3

print (f'O produto do dobro de {int1} com metade de {int2} é igual a {calculo1}')
print (f'A soma do triplo de {int1} com {real1} é iguall a {calculo2}')
print (f'{real1} elevado ao cubo é igual a {calculo3}')