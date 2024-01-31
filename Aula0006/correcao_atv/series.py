class Serie:
    nome = ''
    sinopse = ''
    temporadas  = 0
    epsodios  = 0
    duracao = ''
    elenco  = ''
    classificacao  = ''

    def __str__(self) -> str:
        return f'{self.nome};{self.sinopse};{self.temporadas};{self.epsodios};{self.duracao};{self.elenco};{self.classificacao}'