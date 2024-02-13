from infra.repository.atores_repository import AtoresRepository
from infra.repository.filmes_repository import FilmesRepository
 
repo_a = AtoresRepository() 
repo_f = FilmesRepository()


response_a = repo_a.select()
response_f = repo_f.select()

print(response_a)

