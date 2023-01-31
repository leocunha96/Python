#Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, 
#excreva: "Seu nome é curto", se tiver entre 5 e 6 letras, escreva : "Seu nome é normal",
#se for maior que 6 letras escreva: "Seu nome é muito grande".

nome = input ('Qual é o seu nome? ')

if len (nome) <= 4 :
    print ('Seu nome é curto')
elif len (nome) <= 6 :
    print ('Seu nome é normal')
else:
    print ('Seu nome é muito grande')