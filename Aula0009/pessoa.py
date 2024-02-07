

class Pessoa:

    def __init__(self, nome, sobrenome, idade, endereco):
       self.nome = nome
       self.sobrenome = sobrenome
       self.idade = idade
       self.endereco = endereco

    def __str__(self):
        return f'{self.nome};{self.sobrenome};{self.idade};{self.endereco}'