lista = ['Bruna', 'Larissa', 'Amanda', 'Juliete', 'Maria']

for p in lista: #foreach
    print(p)


for n in range(0,len(lista)): #for incremental tradicional
    print(lista[n])

#remove
lista.remove('Larissa')
print(lista)
#pop
dado = lista.pop(0)
print(lista)
print('Dado removido: '+ dado)
#del
del lista[1]
print(lista)