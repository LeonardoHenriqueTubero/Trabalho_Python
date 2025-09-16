from dataclasses import dataclass
from datetime import date

from backend.entities.Autor import Autor
from backend.entities.Categoria import Categoria
from backend.entities.enums.Disponibilidade import Disponibilidade

@dataclass
class Livro:
    cod: int
    titulo: str
    autor: Autor
    categoria: Categoria
    ano_publicacao: date
    disponibilidade: Disponibilidade
    status: bool = False

    def excluir_dado(self):
        self.status = True

    def __repr__(self):
        return (f"Codigo: {self.cod}, Titulo: {self.titulo}, Ano de Publicacao: {self.ano_publicacao}, "
                f"Autor: {self.autor.nome}, "
                f"Cidade: {self.autor.cidade.descricao}, "
                f"Estado: {self.autor.cidade.estado}, "
                f"Categoria: {self.categoria.descricao}, "
                f"Disponibilidade: {self.disponibilidade.name}")