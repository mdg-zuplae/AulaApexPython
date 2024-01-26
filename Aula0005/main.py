# responsabilidade única, diz que uma funcao deve executar uma unica tarefa
def cadastra_usuario(nome, sobrenome, idade):
    usuario = {'nome': nome, 'sobrenome':sobrenome, 'idade':idade}
    return usuario


u = cadastra_usuario('Jorge', 'dos Meninos', 60)
print(u['idade'])
