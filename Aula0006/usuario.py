class Usuario:
    nome =  ''
    sobrenome = ''
    email = ''
    senha = ''

    def __str__(self) -> str:
        return f'{self.nome} - {self.sobrenome} - {self.email} - {self.senha}'