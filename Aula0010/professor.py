from pessoa import Pessoa


class Professor(Pessoa):
    turmas =  []
    registro = ''

    def __str__(self):
        return f'{super().__str__()},{self.turmas},{self.registro} '