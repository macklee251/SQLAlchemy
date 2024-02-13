from infra.configs.connection import DBConnectionHandle 
from infra.entities.atores import Atores
from infra.entities.filmes import Filmes

class AtoresRepository:
    def select(self):
        with DBConnectionHandle() as db:
            data = db.session\
            .query(Atores)\
            .join(Filmes, Atores.titulo_filme == Filmes.titulo)\
            .order_by(Atores.nome)\
            .with_entities(
                Atores.nome,
                Filmes.titulo,
                Filmes.genero
                )\
            . all()
            return data
    