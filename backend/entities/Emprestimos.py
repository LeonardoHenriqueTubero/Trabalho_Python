from dataclasses import dataclass
from datetime import date, datetime

from entities.Aluno import Aluno
from entities.Livro import Livro

@dataclass
class Emprestimo:
    cod: int
    livro: Livro
    aluno: Aluno
    data_emprestimo: date
    data_devolucao: date
    devolvido: bool = False