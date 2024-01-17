# paramentro opcional, pode ser recebido ou nao, deve ser o ultimo parâmetro
def subtracao(n1, n2, n3=0):
    resultado = n1 - n2 - n3
    return resultado


v1 = 20
v2 = 10
v3 = 5
r = subtracao(v1, v2, v3)
print(r)