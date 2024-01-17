def multiplicacao(n1, n2, n3):
    resultado = n1 * n2 * n3
    return resultado


v1 = 2
v2 = 3
v3 = 5

# argumentos nomeados
r = multiplicacao(n3=v3, n2=v2, n1=v1)
print(r)