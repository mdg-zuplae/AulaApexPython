print('Bem-vindo ao sistema de agendamento')
print('\t1- Cadastrar usuário')
print('\t2- Listar usuário')

invalida = True

while(invalida):
    opcao = int(input('Escolha uma das opções: '))

    if(opcao == 1):
        print('Opt 1')
        invalida = False
    elif(opcao == 2):
        print('Opt 2')
        invalida = False
    else:
        print('Opção incorreta, digite novamente!')
    
