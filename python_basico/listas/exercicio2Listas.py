""""
Faça uma lista de compras. O usuário deve ter a possibilidade de inserir,
apagar e listar valores da sua lista. Não permita que o programa quebre 
com erros de indices inexistente da lista.

"""
import os
lista = []
while True : 
    
    opcao = input ('Selecione uma opção:\n[I]nserir [A]pagar [L]istar: ')
    opcao = opcao.upper()
    print (opcao)
    item = ''
    
    
    if opcao == 'I' :
        os.system('clear')
        item = input ('Item: ')
        lista.append(item)
        os.system('clear')

    elif opcao == 'A' :
        os.system('clear')
        if len(lista) == 0 :
            print ('Não existe item na lista para ser apagado')
        else :
            print ('Selecione o número do item que deseja remover da lista:')
            for i, nome in enumerate(lista):
                print ('Item: ',i,'-',nome)
            item = int (input ('Remover item: '))
            if item > len(lista):
                os.system('clear')
                print ('Este indice não existe no momento')
            else:
                lista.pop(item)
                os.system('clear')

    elif opcao == 'L' :
        os.system('clear')
        for i, nome in enumerate(lista):
            print ('Item: ',i,'-',nome)
    else :
        os.system('clear')
        print ('Opção invalida.')

