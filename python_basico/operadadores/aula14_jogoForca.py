#exercicio jogo da forca


print ('Bem vindo ao jogo da Forca!')


palavraChave = input ('Digite uma palavra para jogar: ') #solicitar 1 palavra
import os
os.system('clear')
palavraFormada = ''
tamanhoPalavra = len(palavraChave)
repeticao = 0
palavraCriptografada = ''
palavraValidada = 0
tamanhoLetrasCertas = 0
letrasCertas = ''
letrasRepetidas = 0

while palavraValidada == 0 : #validação da palavra chave, caso essa não esteja ok, é solicitado uma palavra valida 

        for letraAnalisada in palavraChave: #verificando caracteres dentro da palavra digitada
            letraPalavra = letraAnalisada
            if letraPalavra.isalpha() : #esse metodo verifica se cada caractere é uma letra do alfabeto
                palavraValidada = 1

            else :
                print ('Por favor, digite apenas letras para a palavra!')
                palavraChave = input ('Por favor, digite novamente: ')
                palavraValidada = 0
                break#solicitando uma letra ao usuario

for letra in palavraChave: #colocando * em todas as letras de palavraCriptografada
    palavraCriptografada += '*'

print (f'A palavra é {palavraCriptografada} e ela possui {tamanhoPalavra} letras!')

while (palavraFormada != palavraChave) : 

    letraValidada = 0

    while letraValidada == 0 : #verificação em loop se o usuario digitou letra

        letraEscolhida = input ('Digite uma letra para adivinha a palavra: ') #solicitando uma letra ao usuario 

        if letraEscolhida.isalpha() :
            letraValidada = 1
            if letraEscolhida in letrasCertas :
                print ('Esta letra ja foi escolhida uma vez, por favor, escolha outra letra. ')
            
            else:
            
                if letraEscolhida in palavraChave : #verificando se a letra digitada está entre a palavra chave!
                    letrasCertas += letraEscolhida
                    palavraCriptografada = '' #esvaziando palavra criptografa para preencher com as letras certas
                    for letra in palavraChave:
                        if letra == letraEscolhida:
                            palavraCriptografada += letraEscolhida
                            
                        elif letra in letrasCertas :
                            palavraCriptografada += letra
                        
                            
                        else:
                            palavraCriptografada += '*'
                    print (f'A letra {letraEscolhida} está dentro da palavra secreta!')
                    
                else:
                    repeticao += 1
                    print (f'A letra {letraEscolhida} não está dentro da palavra secreta!')
        
        else :
            print ('Por favor, digite apenas letras para a palavra!')
            letraValidada = 0
            break#solicitando uma letra ao usuario

        
        
    if '*' not in palavraCriptografada:
        for i in letrasCertas :
            letraAtual = palavraChave.count(i)
            if letraAtual > 1 :
                tamanhoLetrasCertas += letraAtual
            else:
                tamanhoLetrasCertas += 1
                
    
            

    print (palavraCriptografada)

        
    if tamanhoLetrasCertas == tamanhoPalavra : #verificar letras repetidas
        palavraFormada = palavraChave


if repeticao == 0 :
    print ('Parabens, você adivinhou a palavra sem errar nenhuma vez!')    
else:
    print (f'Parabéns, você adivinhou a palavra! Você precisou de {repeticao} tentativas!')

