from infra.configs.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Filmes(Base):
    __tablename__ = 'filmes' # essa propriedade é usada para definir o nome da tabela 
    titulo = Column(String(50), primary_key=True)
    genero = Column(String(50), nullable=False)
    ano = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f'Filme (titulo={self.titulo}, ano={self.ano})'