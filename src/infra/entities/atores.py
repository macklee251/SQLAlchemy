from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Atores(Base):
    __tablename__ = 'atores' # essa propriedade é usada para definir o nome da tabela 
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    titulo_filme = Column(Integer, ForeignKey("filmes.id"))
    
    def __repr__(self):
        return f'Atores (nome={self.nome}), Filme ({self.titulo_filme})'