from dataclasses import dataclass

@dataclass
class Cidade:
    cod: int
    descricao: str
    estado: str
    status: bool = False

    def excluir_dado(self):
        self.status = True