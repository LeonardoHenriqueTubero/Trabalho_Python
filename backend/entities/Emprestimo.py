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

    def __repr__(self):
        data_emprestimo_formatada = self.data_emprestimo.strftime('%d/%m/%Y')
        data_devolucao_formatada = self.data_devolucao.strftime('%d/%m/%Y')

        return (f"Codigo: {self.cod}, "
                f"Livro: {self.livro.titulo}, "
                f"Aluno: {self.aluno.nome}, Cidade: {self.aluno.cidade.descricao}, "
                f"Data Emprestimo: {data_emprestimo_formatada}, "
                f"Data Devolucao: {data_devolucao_formatada}, "
                f"Devolvido: {'SIM' if self.devolvido is True else 'NAO'}")