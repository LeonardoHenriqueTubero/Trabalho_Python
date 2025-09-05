from dataclasses import dataclass

@dataclass
class Categoria:
    cod: int
    descricao: str
    status: bool = False