from dataclasses import dataclass
from datetime import date, datetime

from entities.Autor import Autor
from entities.Categoria import Categoria
from entities.enums.Disponibilidade import Disponibilidade


@dataclass
class Livro:
    cod: int
    titulo: str
    autor: Autor
    categoria: Categoria
    ano_publicacao: date
    disponibilidade: Disponibilidade