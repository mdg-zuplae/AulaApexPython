# CRUD
# Create = Criar -  cadastrar algo
# Read - Ler - listar um ou mais dados
# Update - Alterar - alterar o valor de um dado
# Delete - Deletar - apagar algum dado

# PEP8
def create():
    msg = 'Usuário cadastrado com sucesso'
    return msg

def read():
    msg = 'Usuário de ID= encontrado'
    return msg

def read_all():
    msg = 'Listagem de usuarios'
    return msg

def update():
    msg = 'Usuário alterado com sucesso!'
    return msg

def delete():
    msg = 'Usuário excluído com sucesso!'
    return msg

mensagem = read_all()
print(mensagem)
