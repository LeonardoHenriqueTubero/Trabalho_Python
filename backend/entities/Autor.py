from dataclasses import dataclass

from entities.Cidade import Cidade


@dataclass
class Autor:
    cod: int
    nome: str
    cidade: Cidade
