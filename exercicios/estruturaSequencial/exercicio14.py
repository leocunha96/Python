'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
 variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite 
 e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas

'''

def calculoPeso (peso) :
    pesoLei = 50.0
    if peso > pesoLei :
        multa = 4 * (peso - pesoLei)
        return multa
    if peso <= pesoLei :
        multa = 0
        return multa

def mensagem (resultado) :
    if resultado == 0 :
        print ( 'Tudo certo seu João Papo-de-Pescador, hoje o senhor seguiu a lei, tem nenhum multa não!')
    else :
        print (f'Eita Lasqueira, o senhor passou da conta, precisa paga uma multa de R$ {resultado}')

print ('Bão dia seu João, tudo certo?\nBOra ve esse pexe')

peso = input ('Informe quantos kg o senhor pescou hoje: ')
peso = float (peso)
resultado = calculoPeso (peso)
mensagem (resultado)
