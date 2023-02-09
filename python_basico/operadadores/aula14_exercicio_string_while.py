#Qual letra mais apareceu na frase ?

frase = input('Digite uma frase para saber qual é a letra que mais aparece nela: ')

i = 0
letraQueMaisApareceu = ''
vezesQueMaisApareceu = 0

while i < len(frase) :

    letraAtual = frase[i]
    repeticoesLetraAtual = frase.count(letraAtual)

    if letraAtual == ' ' :
        i += 1
        continue

    elif vezesQueMaisApareceu < repeticoesLetraAtual :
        
        vezesQueMaisApareceu = repeticoesLetraAtual
        letraQueMaisApareceu = letraAtual



    i += 1

print (f'A letra que apareceu mais vezes foi a letra {letraQueMaisApareceu}, aparecendo {vezesQueMaisApareceu} vezes!')
