#Resolução do professor para o exercicio do jogo da forca

#Colocar variaveis fora do while para guardar resultados das iterações realizadas no loop.
#Pois se estas variaveis são declaradas dentro do loop, ao reiniciar, elas são zeradas.

import os #importando modulo os para zerar o terminal do usuario

palavraSecreta = input ('Digite a palavra secreta: ') 
letrasAcertadas = ''
numeroTentativas = 0 
while True :

    letraDigitada = input ('Digite uma letra: ')
    numeroTentativas += 1 

    if len(letraDigitada) > 1 : #verifica se o usuário digitou apenas uma letra de fato
        print ('Digite apenas uma letra!')
        continue

    if letraDigitada in palavraSecreta : #verifica se a letra digitada está dentro da palavra secreta
        letrasAcertadas += letraDigitada #se estiver, letras acertadas recebe a letra digitada

    palavraFormada = '' #a palavra formada começa vazia sem no loop do while

    for letra in palavraSecreta : #este for é para verificar as letras acertadas e imprimir elas visiveis. E o que não for acertado, é imprimido *
        if letra in letrasAcertadas :
            palavraFormada += letra #se a letra atual da palavra secreta estiver em letras acertadas, a palavra formada recebe a letra atual
        else:
            palavraFormada += '*' #caso não esteja, a palavra formada recebe o *

    print ('Palavra formada:', palavraFormada) #este print é para imprimir a palavra formada, ele aqui, imprime ela direto, pronta, na mesma linha

    if palavraFormada == palavraSecreta :
        os.system('clear') #passando comando clear para o sistema
        print ('Parabéns!! Você ganhou!!')
        print ('A palavra era ',palavraSecreta)
        print ('Tentativas: ',numeroTentativas)
        letrasAcertadas = '' #zerando as variaveis pois o usuario aqui ja ganhou
        numeroTentativas = 0 

