from series import Serie


class CrudSeries:
    lista_serie = []
    
    def cadastrar(self, nome, sinopse, temporadas, epsodios, duracao, elenco, classificacao):
        serie = Serie()
        serie.nome = nome
        serie.sinopse = sinopse
        serie.temporadas = temporadas
        serie.epsodios = epsodios
        serie.duracao = duracao
        serie.elenco = elenco
        serie.classificacao = classificacao
        self.lista_serie.append(serie)

    def listar(self):
        return self.lista_serie