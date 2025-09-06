from dataclasses import dataclass

from backend.databases.BaseDadosAluno import BaseDadosAluno
from backend.databases.BaseDadosAutor import BaseDadosAutor
from backend.databases.BaseDadosCidade import BaseDadosCidade
from backend.databases.BaseDadosCurso import BaseDadosCurso


@dataclass
class Repositorio:
    dados_autores: BaseDadosAutor
    dados_cidades: BaseDadosCidade
    dados_cursos: BaseDadosCurso
    dados_alunos: BaseDadosAluno

