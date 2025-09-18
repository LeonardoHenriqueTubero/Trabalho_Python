from dataclasses import dataclass
from datetime import datetime

from backend.databases.BaseDadosAutor import BaseDadosAutor
from backend.databases.BaseDadosCategoria import BaseDadosCategoria
from backend.entities.Arvore import Arvore
from backend.entities.Livro import Livro
from backend.entities.enums.Disponibilidade import Disponibilidade
import pickle

@dataclass
class BaseDadosLivro:
    livros: list[Livro]
    arvore: Arvore | None = None

    def leitura(self, dados_autor: BaseDadosAutor, dados_categoria: BaseDadosCategoria):
        codigo = self.contar_registros()
        while True:
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

            if not self.continuar():
                break
            codigo = codigo + 1

        with open('data/dado_livros.pkl', 'wb') as file:
            pickle.dump(self.livros, file)

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

    def mudar_disponibilidade(self, cod: int):
        busca = Arvore.busca_no(self.arvore, cod)
        if busca is not None:
            if self.livros[busca.endereco].disponibilidade is Disponibilidade.DISPONIVEL:
                self.livros[busca.endereco].disponibilidade = Disponibilidade.INDISPONIVEL
            else:
                self.livros[busca.endereco].disponibilidade = Disponibilidade.DISPONIVEL

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

    def leitura_exaustiva_emprestados(self):
        lista = self.arvore.em_ordem_retorno()
        for i in range (len(lista)):
            livro = self.busca_elemento(lista[i])
            if not livro.status and livro.disponibilidade is Disponibilidade.INDISPONIVEL:
                print(f"{livro}")

    def limpar_arvore(self):
        self.arvore = None

    def contar_registros(self):
        num_cod = 1
        for _ in self.livros:
            num_cod = num_cod + 1
        return num_cod

    def continuar(self):
        while True:
            opcao = input("Continuar a leitura? (S/N): ").strip().upper()
            if opcao in ("S", "N"):
                return opcao == "S"
            print("Opção inválida! Digite apenas S ou N.")

    def retornar_disponiveis(self):
        count = 0
        for livro in self.livros:
            if livro.disponibilidade is Disponibilidade.DISPONIVEL:
                count = count + 1
        print(f"Numero de livros disponiveis: {count}")

    def retornar_indisponiveis(self):
        count = 0
        for livro in self.livros:
            if livro.disponibilidade is Disponibilidade.INDISPONIVEL:
                count = count + 1
        print(f"Numero de livros emprestados: {count}")