from dataclasses import dataclass
from datetime import date

from backend.entities.Aluno import Aluno
from backend.entities.Livro import Livro

@dataclass
class Emprestimo:
    cod: int
    livro: Livro
    aluno: Aluno
    data_emprestimo: date
    data_devolucao: date
    devolvido: bool = False
    status: bool = False

    def excluir_dado(self):
        self.status = True