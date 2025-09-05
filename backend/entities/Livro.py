from dataclasses import dataclass
from datetime import date, datetime

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