from datetime import datetime


class Usuario:
    def __init__(self, nome, email, senha, funcao):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.funcao = funcao
        self.data_criacao = datetime.now()

    def __str__(self):
        return f'{self.nome} - {self.email} - {self.senha} - {self.funcao} - {self.data_criacao}'