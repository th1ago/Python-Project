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
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'
    
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'
    
class Playlist():
    def __init__(self, nome, progamas):
        self.nome = nome
        self._programa = progamas
    
    def __getitem__(self, item):
        return self._programa[item]
    
    @property
    def listagem(self):
        return self._programa

    def __len__ (self):
        return len(self._programa)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
demolidor = Serie('Demolidor', 2016, 2)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta, demolidor]
playlist_fds = Playlist('Fds', filmes_e_series)

for programa in playlist_fds:
    print(programa)