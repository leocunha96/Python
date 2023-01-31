#Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito
#exiba a saudação apropriada. Ex: Bom dia (01-11), Boa tarde(12-17) e Boa Noite (18-00)

hora = input ('Que horas são? \nInforme seguindo o padrão: 00:00 ')
dia =  '01' <= hora [:2:] <= '11'
tarde = '12' <= hora [:2:] <= '17'
noite = '18' <= hora [:2:] <= '24'


if dia:
    print ('Bom dia!')
elif tarde:
    print ('Boa tarde!')
elif noite:
    print ('Boa noite!')
else:
    print ('Valor invalido')