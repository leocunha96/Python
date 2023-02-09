'''
split e join com list e str

split -- divide uma string

join -- une uma string
'''

frase = 'Olha só que coisa interessante'
listaFrase = frase.split() #é possivel passar como argumento o fator separador para o slit

fraseUnida = ''.join(listaFrase)#entre as '' é passado o separador para as palavras, sem nada = tudo junto
print(listaFrase)
print(fraseUnida)