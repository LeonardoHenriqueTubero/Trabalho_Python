from dataclasses import dataclass

@dataclass
class Categoria:
    cod: int
    descricao: str
    status: bool = False

    def excluir_dado(self):
        self.status = True