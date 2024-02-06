

class Serie:
    nome = ''
    sinopse = ''
    temporadas = 0
    episodios = 0
    duracao = ''
    elenco = ''
    classificacao = ''

    #metodo construtor
    def __init__(self, nome, sinopse):
        self.nome = nome
        self.sinopse = sinopse

    def __str__(self):
        return f'nome:{self.nome} - Sinopse: {self.sinopse}'