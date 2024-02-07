

class Pessoa:
    nome = ''
    sobrenome = ''
    idade = 0

    def __str__(self):
        return f'{self.nome},{self.sobrenome},{self.idade}'