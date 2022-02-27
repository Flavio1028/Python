class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f' {self._nome} - {self.ano} - {self.duracao} mim - {self._likes}  Likes '

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f' {self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes}  Likes '

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)

vingadores = Filme('Vingadores - guerra infinita', 2018, 160)
atlanta = Serie("Atlanta", 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie("demolidor", 2016, 2)

vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('Fim de Semana', filmes_e_series)

for programa in playlist_fim_de_semana:
    print(programa)