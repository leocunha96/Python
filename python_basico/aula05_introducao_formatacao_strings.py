#formatação de string

nome = 'Leonardo'
idade = 26
altura = 1.73
peso = 82.0
imc = peso / (altura ** 2)

linha1 = f'{nome} tem altura de {altura}' #f no inicio é f-Strings, permite a utilização de variaveis no texto, através da utilização de {}
linha2 = f'pesa {peso} quilos e seu imc é: {imc:.2f}' #utilizar :.2f diz que estamos querendo 2 casas decimais.

print(linha1)
print(linha2)

#tudo em Python é objeto!

a = 'A'
b = 'B'
c = 1.1
string = 'a = {nome1} b = {nome2} c = {nome3:.2f}'
formato = string.format(nome1 = a,nome2 = b, nome3 = c) #utilizando parametro nomeado, se eu coloco parametro no primeiro indice, todos os demais devem ter também
print(formato)