from crud_series import CrudSeries


print('Bem-vindo ao Netflix')
print('\t1 - Cadastrar')
print('\t2 - Listar')
print('\t3 - Sair')


crud = CrudSeries()
invalido = True
while(invalido):
    opcao = int(input('Digite uma opção do menu:'))

    if(opcao == 1):
        nome = input('Digite o nome: ')
        sinopse = input('Digite a sinopse: ')
        temporadas = input('Digite o numero de temporadas: ')
        epsodios = input('Digite o numero de epsodios: ')
        duracao = input('Digite a duracao: ')
        elenco = input('Digite o elenco: ')
        classificacao = input('Digite a classificação: ')
        crud.cadastrar(nome, sinopse, temporadas, epsodios, duracao, elenco, classificacao)
        
    elif(opcao == 2):
        for s in crud.listar():
            print(s)

    elif(opcao == 3):
        print('Saindo ...')
        invalido = False
    else:
        print('Opcao invalida, digite novamente\n')
