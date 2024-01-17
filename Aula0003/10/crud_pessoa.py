lista_pessoas = []
id = 0

def create(nome, sobrenome, idade):
    global id
    id = id + 1
    pessoa = {'id':id, 'nome':nome, 'sobrenome': sobrenome, 'idade': idade}
    lista_pessoas.append(pessoa)
    return f'Pessoa {nome} cadastrada com sucesso'

def read_all():
    return lista_pessoas

def read_by_id(id):
    pessoa_encontrada = None

    for pessoa in lista_pessoas:
        if pessoa['id'] == id:
            pessoa_encontrada = pessoa
    
    return pessoa_encontrada

def update(pessoa):
    elementos = len(lista_pessoas)
    for indice in range(0, elementos): #for incremental
        if lista_pessoas[indice]['id'] == pessoa['id']:
            lista_pessoas[indice] = pessoa


def delete(id):
    elementos = len(lista_pessoas)
    for indice in range(0, elementos): #for incremental
        if lista_pessoas[indice]['id'] == id:
            del lista_pessoas[indice]



