#operadores in e not in
#Lembrar que Strings em Python são iteráveis
# 0 1 2 3 4 5 6 7
# L e o n a r d o
#-8-7-6-5-4-3-2-1

nome = 'Leonardo'

print (nome[2]) #letra o
print (nome[-8]) #letra L

print ('n' in nome) #retorna true
print ('p' in nome)
print ('nar' in nome)
print ('z' not in nome)

preco = 5.495

variavel = '%s, o preço do litro da gasolina está %.2f' % (nome, preco)

print (variavel)

print ('O hexadecimal de %d é %x' % (15, 15))
