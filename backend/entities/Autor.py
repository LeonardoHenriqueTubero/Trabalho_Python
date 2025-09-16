from dataclasses import dataclass

from backend.entities.Cidade import Cidade


@dataclass
class Autor:
    cod: int
    nome: str
    cidade: Cidade
    status: bool = False

    def excluir_dado(self):
        self.status = True

    def __repr__(self):
        return f"Codigo: {self.cod}, Nome: {self.nome}, Cidade: {self.cidade.descricao}, Estado: {self.cidade.estado}"