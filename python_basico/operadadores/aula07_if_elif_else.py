#if / elif       / else
#se / se não se / se não

entrada = input ('Você quer entrar ou sair? ')

if entrada == 'entrar': #não abrimos chaves e nem colocamos parenteses na condição, colocamos dois pontos :
    print ('Você  entrou!') #por não ter chave, precisamos dar um "tab" para o interpretador entender que está dentro do if

elif entrada == 'sair':
    print ('Você saiu!')

else:
    print('Opção invalida!')

print ('Obrigado!')