from dataclasses import dataclass

from entities.Curso import Curso
from entities.Cidade import Cidade


@dataclass
class Aluno:
    cod: int
    nome: str
    curso: Curso
    cidade: Cidade
