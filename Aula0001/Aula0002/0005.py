# procedimento
def boas_vindas():
    print('Bem-vindo ao sistema soma')

# funcao
# Responsabilidade unica - uma funcao deve fazer apenas uma coisa
# ter apenas uma responsabilidade - ajuda no reaproveitamento de codigo
def pega_nome():
    nome = input('Digite seu nome: ')
    return nome

def saudacao(nome):
    print(f'Olá, {nome}')

boas_vindas()
nome2 = pega_nome()
saudacao(nome2)
