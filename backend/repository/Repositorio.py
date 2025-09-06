from dataclasses import dataclass

from backend.databases.BaseDadosAluno import BaseDadosAluno
from backend.databases.BaseDadosAutor import BaseDadosAutor
from backend.databases.BaseDadosCategoria import BaseDadosCategoria
from backend.databases.BaseDadosCidade import BaseDadosCidade
from backend.databases.BaseDadosCurso import BaseDadosCurso
from backend.databases.BaseDadosEmprestimo import BaseDadosEmprestimo
from backend.databases.BaseDadosLivro import BaseDadosLivro

@dataclass
class Repositorio:
    dados_autores: BaseDadosAutor
    dados_cidades: BaseDadosCidade
    dados_cursos: BaseDadosCurso
    dados_alunos: BaseDadosAluno
    dados_categorias: BaseDadosCategoria
    dados_livros: BaseDadosLivro
    dados_emprestimos: BaseDadosEmprestimo

