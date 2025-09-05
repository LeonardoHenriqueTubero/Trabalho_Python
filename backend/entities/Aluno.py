from dataclasses import dataclass

from backend.entities.Curso import Curso
from backend.entities.Cidade import Cidade

@dataclass
class Aluno:
    cod: int
    nome: str
    curso: Curso
    cidade: Cidade
    status: bool = False

    def excluir_dado(self):
        self.status = True