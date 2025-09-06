from dataclasses import dataclass
from datetime import datetime

from backend.databases.BaseDadosAutor import BaseDadosAutor
from backend.databases.BaseDadosCategoria import BaseDadosCategoria
from backend.entities.Arvore import Arvore
from backend.entities.Livro import Livro
from backend.entities.enums.Disponibilidade import Disponibilidade


@dataclass
class BaseDadosLivro:
    livros: list[Livro]
    arvore: Arvore | None = None

    def leitura(self, dados_autor: BaseDadosAutor, dados_categoria: BaseDadosCategoria):
        codigo = 0
        while True:
            try:
                codigo = int(input("Digite o código (0 para sair): "))
                if codigo == 0:
                    break
            except ValueError:
                print("Código inválido. Por favor, digite um número.")
                continue

            titulo = input("Digite um titulo: ")
            autor_cod = int(input("Digite o codigo do autor: "))
            autor = dados_autor.busca_elemento(autor_cod)
            while autor is None:
                autor_cod = int(input("Digite novamente o codigo do autor: "))
                autor = dados_autor.busca_elemento(autor_cod)
            categoria_cod = int(input("Digite o codigo da categoria: "))
            categoria = dados_categoria.busca_elemento(categoria_cod)
            while categoria is None:
                categoria_cod = int(input("Digite novamente o codigo da categoria: "))
                categoria = dados_categoria.busca_elemento(categoria_cod)
            ano_publicacao = input("Digite a data de publicacao: ")
            disponivel = input("Está disponível (S/N)? ")
            disponibilidade = Disponibilidade.INDISPONIVEL
            if str.upper(disponivel) == "S":
                disponibilidade = Disponibilidade.DISPONIVEL
            status = False
            novo = Livro(codigo, titulo, autor, categoria, datetime.strptime(ano_publicacao, "%d/%m/%Y").date(), disponibilidade, status)
            self.livros.append(novo)

    def incluir_livros(self, livros: list[Livro]):
        for i in range(len(livros)):
            self.livros.append(livros[i])

    def incluir_arvore(self):
        inicio = 0
        fim = len(self.livros) - 1
        meio = int((inicio + fim) / 2)
        self.arvore = Arvore(self.livros[meio].cod, meio, None, None)
        for i in range(len(self.livros)):
            if i != meio:
                self.arvore.inserir(self.livros[i].cod, i)

    def busca_elemento(self, cod: int):
        busca = Arvore.busca_no(self.arvore, cod)
        if busca is not None:
            return self.livros[busca.endereco]
        else:
            print(f"Nó não encontrado")
            return None

    def excluir_registro(self, cod: int):
        busca = Arvore.busca_no(self.arvore, cod)
        if busca is not None:
            self.livros[busca.endereco].excluir_dado()
            print(f"O código {cod} foi excluído!")
        self.arvore = Arvore.excluir(self.arvore, cod)


    def metodo_bolha(self):
        n = len(self.livros)
        for i in range (n - 1):
            trocou = False
            for j in range (n - 1 - i):
                if self.livros[j].cod > self.livros[j+1].cod:
                    self.livros[j], self.livros[j + 1] = self.livros[j + 1], self.livros[j]
                    trocou = True
            if not trocou:
                break

    def leitura_exaustiva(self):
        lista = self.arvore.em_ordem_retorno()
        for i in range (len(lista)):
            livro = self.busca_elemento(lista[i])
            if not livro.status:
                print(f"{livro}")

    def limpar_arvore(self):
        self.arvore = None