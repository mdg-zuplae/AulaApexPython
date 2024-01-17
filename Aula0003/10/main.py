from crud_pessoa import create, read_all, read_by_id, update

print(create('Joao', 'Silva', 80))
print(create('Maria', 'Souza', 16))
print(create('Antonio', 'Miranda', 45))


lista = read_all()
for p in lista:
    print(p)

# p = read_by_id(3)
# print(p)
pessoa_alterada = {'id':3, 'nome':'Tonho', 'sobrenome': 'Da Lua', 'idade': 98}
update(pessoa_alterada)

print('Dados com  a alteracao')
lista = read_all()
for p in lista:
    print(p)
