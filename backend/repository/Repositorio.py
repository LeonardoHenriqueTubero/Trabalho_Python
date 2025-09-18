import pickle
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

    @classmethod
    def iniciar_repositorio(cls):
        return Repositorio(
            BaseDadosAutor([]),
            BaseDadosCidade([]),
            BaseDadosCurso([]),
            BaseDadosAluno([]),
            BaseDadosCategoria([]),
            BaseDadosLivro([]),
            BaseDadosEmprestimo([])
        )

    def carregar_cidades(self):
        with open('data/dado_cidades.pkl', 'rb') as file:
            self.dados_cidades.cidades = pickle.load(file)
        self.dados_cidades.arvore = None
        self.dados_cidades.incluir_arvore()

    def carregar_cursos(self):
        with open('data/dado_cursos.pkl', 'rb') as file:
            self.dados_cursos.cursos = pickle.load(file)
        self.dados_cursos.arvore = None
        self.dados_cursos.incluir_arvore()

    def carregar_alunos(self):
        with open('data/dado_alunos.pkl', 'rb') as file:
            self.dados_alunos.alunos = pickle.load(file)
        self.dados_alunos.arvore = None
        self.dados_alunos.incluir_arvore()

    def carregar_autores(self):
        with open('data/dado_autores.pkl', 'rb') as file:
            self.dados_autores.autores = pickle.load(file)
        self.dados_autores.arvore = None
        self.dados_autores.incluir_arvore()

    def carregar_categorias(self):
        with open('data/dado_categorias.pkl', 'rb') as file:
            self.dados_categorias.categorias = pickle.load(file)
        self.dados_categorias.arvore = None
        self.dados_categorias.incluir_arvore()

    def carregar_livros(self):
        try:
            with open('data/dado_livros.pkl', 'rb') as file:
                self.dados_livros.livros = pickle.load(file)
                self.dados_livros.arvore = None
                self.dados_livros.incluir_arvore()
        except FileNotFoundError:
            self.dados_livros.livros = []

    def carregar_emprestimos(self):
        try:
            with open('data/dado_emprestimos.pkl', 'rb') as file:
                self.dados_emprestimos.emprestimos = pickle.load(file)
                self.dados_emprestimos.arvore = None
                self.dados_emprestimos.incluir_arvore()
        except FileNotFoundError:
            self.dados_emprestimos.emprestimos = []