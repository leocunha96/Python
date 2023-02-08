
print ('Bem vindo ao jogo da Forca!')


palavraChave = input ('Digite uma palavra para jogar: ')
letra = ''
palavraFormada = ''
tamanhoPalavra = len(palavraChave)
repeticao = 0
palavraCriptografada = ''
palavraValidada = 1
tamanhoLetrasCertas = 0
letrasCertas = ''

while palavraValidada == 1 : #validação da palavra chave, caso essa não esteja ok, é solicitado uma palavra valida 

        for letraAnalisada in palavraChave: #verificando caracteres dentro da palavra digitada
            letraPalavra = letraAnalisada
            if letraPalavra.isalpha() : #esse metodo verifica se cada caractere é uma letra do alfabeto
                palavraValidada = 0

            else :
                print ('Por favor, digite apenas letras para a palavra!')
                palavraChave = input ('Por favor, digite novamente: ')
                palavraValidada = 1
                break#solicitando uma letra ao usuario

for letra in palavraChave: #colocando * em todas as letras de palavraCriptografada
    palavraCriptografada += '*'

print (f'A palavra é {palavraCriptografada} e ela possui {tamanhoPalavra} letras!')

while (palavraFormada != palavraChave) : 

    letraEscolhida = input ('Digite uma letra para adivinha a palavra: ') #solicitando uma letra ao usuario 

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
            

    print (palavraCriptografada)

    tamanhoLetrasCertas = len(letrasCertas)
        
    if tamanhoLetrasCertas == tamanhoPalavra : #verificar letras repetidas
        palavraFormada = palavraChave


    
print (repeticao)
    #
