from usuario_crud import CrudUsuario

crud = CrudUsuario()

print('Bem-vindo ao sistema de agendamento')
print('\t1- Cadastrar usuário')
print('\t2- Listar usuário')

opcao_digitada_valida = False

while(not opcao_digitada_valida):
    opcao = int(input('Escolha uma das opções: '))
    

    if(opcao == 1):
        nome = input('Digite o nome:')
        sobrenome = input('Digite o sobrenome:')
        email = input('Digite o email:')
        senha = input('Digite a senha :')
        crud.cadastrar(nome, sobrenome, email, senha)

    elif(opcao == 2):
        for u in crud.listar():
            print(u)
    else:
        print('Opção incorreta, digite novamente!')
    
