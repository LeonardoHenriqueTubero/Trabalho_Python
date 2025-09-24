import pickle
from dataclasses import dataclass
from pathlib import Path
from backend.databases.BaseDadosAluno import BaseDadosAluno
from backend.databases.BaseDadosAutor import BaseDadosAutor
from backend.databases.BaseDadosCategoria import BaseDadosCategoria
from backend.databases.BaseDadosCidade import BaseDadosCidade
from backend.databases.BaseDadosCurso import BaseDadosCurso
from backend.databases.BaseDadosEmprestimo import BaseDadosEmprestimo
from backend.databases.BaseDadosLivro import BaseDadosLivro

caminho_raiz = Path(__file__).parent.parent.parent

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
        caminho_completo = caminho_raiz / 'backend' / 'data' / 'dado_cidades.pkl'
        with open(caminho_completo, 'rb') as file:
            self.dados_cidades.cidades = pickle.load(file)
        self.dados_cidades.arvore = None
        self.dados_cidades.incluir_arvore()

    def carregar_cursos(self):
        caminho_completo = caminho_raiz / 'backend' / 'data' / 'dado_cursos.pkl'
        with open(caminho_completo, 'rb') as file:
            self.dados_cursos.cursos = pickle.load(file)
        self.dados_cursos.arvore = None
        self.dados_cursos.incluir_arvore()

    def carregar_alunos(self):
        caminho_completo = caminho_raiz / 'backend' / 'data' / 'dado_alunos.pkl'
        with open(caminho_completo, 'rb') as file:
            self.dados_alunos.alunos = pickle.load(file)
        self.dados_alunos.arvore = None
        self.dados_alunos.incluir_arvore()

    def carregar_autores(self):
        caminho_completo = caminho_raiz / 'backend' / 'data' / 'dado_autores.pkl'
        with open(caminho_completo, 'rb') as file:
            self.dados_autores.autores = pickle.load(file)
        self.dados_autores.arvore = None
        self.dados_autores.incluir_arvore()

    def carregar_categorias(self):
        caminho_completo = caminho_raiz / 'backend' / 'data' / 'dado_categorias.pkl'
        with open(caminho_completo, 'rb') as file:
            self.dados_categorias.categorias = pickle.load(file)
        self.dados_categorias.arvore = None
        self.dados_categorias.incluir_arvore()

    def carregar_livros(self):
        caminho_completo = caminho_raiz / 'backend' / 'data' / 'dado_livros.pkl'
        try:
            with open(caminho_completo, 'rb') as file:
                self.dados_livros.livros = pickle.load(file)
                self.dados_livros.arvore = None
                self.dados_livros.incluir_arvore()
        except FileNotFoundError:
            self.dados_livros.livros = []

    def carregar_emprestimos(self):
        caminho_completo = caminho_raiz / 'backend' / 'data' / 'dado_emprestimos.pkl'
        try:
            with open(caminho_completo, 'rb') as file:
                self.dados_emprestimos.emprestimos = pickle.load(file)
                self.dados_emprestimos.arvore = None
                self.dados_emprestimos.incluir_arvore()
        except FileNotFoundError:
            self.dados_emprestimos.emprestimos = []

    def carregar_tudo(self):
        self.carregar_cidades()
        self.carregar_cursos()
        self.carregar_alunos()
        self.carregar_autores()
        self.carregar_categorias()
        self.carregar_livros()
        self.carregar_emprestimos()