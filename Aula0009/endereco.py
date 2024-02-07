

class Endereco:

    def __init__(self, rua, numero, complemento, bairro, cidade):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade

    def __str__(self):
        return f'{self.rua};{self.numero};{self.complemento}:{self.bairro};{self.cidade}'