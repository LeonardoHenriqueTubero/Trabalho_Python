from dataclasses import dataclass

@dataclass
class Curso:
    cod: int
    descricao: str
    status: bool = False