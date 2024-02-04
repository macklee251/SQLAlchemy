from infra.configs.connection import DBConnectionHandle 
from infra.entities.filmes import Filmes

class FilmesRepository:
    def select(self):
        with DBConnectionHandle() as db:
            data = db.session.query(Filmes).all()
            return data
         