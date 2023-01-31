#peça ao usuário para digitar seu nome
#peça ao usuário para digitar sua idade
#se nome e idade forem digitados:
#exiba:
#seu nome é {nome}
#seu nome invertido é {nome invertido}
#se o nome contem ou não espaços
#seu nome tem {n} letras
#a primeira letra do seu nome é {letra}
#a ultima letra do seu nome é {letra}

#Se nada for digitado em nome ou idade:
#exiba "Desculpe, voce deixou campos vazios."


nome = input ('Digite seu nome: ')
idade = input ('Digite sua idade: ')

if nome and idade :
    print(f'Seu nome é: {nome}.')
    print (f'Seu nome invertido é: {nome[::-1]}.')

    if ' ' in nome:
        print ('Seu nome possui espaços')
    else:
        print ('Seu nome não possui espaços')
        
    print (f'Seu nome tem {len(nome)} letras.')
    print (f'A primeira letra do seu nome é: {nome[:1]}.')
    print (f'A ultima letra do seu nome é: {nome [len(nome)-1:]}')


else:
    print ('Desculpe, você deixou campos vazios.')