from dataclasses import dataclass
from datetime import datetime

import questionary
from rich.table import Table
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
            titulo = questionary.text("Digite o titulo:").ask()
            autor_cod = questionary.text("Digite o codigo do autor:", validate=lambda val: val.isdigit() or "Digite um número válido").ask()
            autor = dados_autor.busca_elemento(int(autor_cod))
            while autor is None:
                autor_cod = questionary.text("Digite novamente o codigo do autor:", validate=lambda val: val.isdigit() or "Digite um número válido").ask()
                autor = dados_autor.busca_elemento(int(autor_cod))
            categoria_cod = questionary.text("Digite o codigo da categoria:", validate=lambda val: val.isdigit() or "Digite um número válido").ask()
            categoria = dados_categoria.busca_elemento(int(categoria_cod))
            while categoria is None:
                categoria_cod = questionary.text("Digite o codigo da categoria:", validate=lambda val: val.isdigit() or "Digite um número válido").ask()
                categoria = dados_categoria.busca_elemento(int(categoria_cod))
            ano_publicacao = questionary.text("Digite a data de publicacao:").ask()
            disponivel = questionary.text("Digite a disponibilidade:").ask()
            disponibilidade = Disponibilidade.INDISPONIVEL
            if str.upper(disponivel) == "S":
                disponibilidade = Disponibilidade.DISPONIVEL
            status = False
            novo = Livro(codigo, titulo, autor, categoria, datetime.strptime(ano_publicacao, "%d/%m/%Y").date(), disponibilidade, status)
            self.livros.append(novo)

            continuar = questionary.confirm("Quer continuar?").ask()
            if not continuar:
                break
            codigo = codigo + 1

        with open('backend/data/dado_livros.pkl', 'wb') as file:
            pickle.dump(self.livros, file)

    def incluir_livros(self, livros: list[Livro]):
        for i in range(len(livros)):
            self.livros.append(livros[i])

    def incluir_arvore(self):
        if not self.livros:
            return
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

    def leitura_exaustiva(self) -> Table | None:
        if not self.livros:
            return None
        lista = self.arvore.em_ordem_retorno()
        table = Table(title="Autores", style="bold cyan")
        table.add_column("Id", justify="center", style="bold yellow")
        table.add_column("Titulo", justify="left", style="white")
        table.add_column("Ano de Publicacao", justify="left", style="white")
        table.add_column("Autor", justify="left", style="white")
        table.add_column("Cidade", justify="left", style="white")
        table.add_column("Estado", justify="left", style="white")
        table.add_column("Categoria", justify="left", style="white")
        table.add_column("Disponibilidade", justify="left", style="white")

        for i in range(len(lista)):
            livro = self.busca_elemento(lista[i])
            if not livro.status:
                table.add_row(
                    str(livro.cod),
                    livro.titulo,
                    str(livro.ano_publicacao),
                    livro.autor.nome,
                    livro.autor.cidade.descricao,
                    livro.autor.cidade.estado,
                    livro.categoria.descricao,
                    livro.disponibilidade.name
                )
        return table

    def leitura_exaustiva_emprestados(self) -> Table | None:
        if not self.livros:
            return
        lista = self.arvore.em_ordem_retorno()
        table = Table(title="Livros Emprestados", style="bold cyan")
        table.add_column("Id", justify="center", style="bold yellow")
        table.add_column("Titulo", justify="left", style="white")
        table.add_column("Ano de Publicacao", justify="left", style="white")
        table.add_column("Autor", justify="left", style="white")
        table.add_column("Cidade", justify="left", style="white")
        table.add_column("Estado", justify="left", style="white")
        table.add_column("Categoria", justify="left", style="white")
        table.add_column("Disponibilidade", justify="left", style="white")

        for i in range (len(lista)):
            livro = self.busca_elemento(lista[i])
            if not livro.status and livro.disponibilidade is Disponibilidade.INDISPONIVEL:
                table.add_row(
                    str(livro.cod),
                    livro.titulo,
                    str(livro.ano_publicacao),
                    livro.autor.nome,
                    livro.autor.cidade.descricao,
                    livro.autor.cidade.estado,
                    livro.categoria.descricao,
                    livro.disponibilidade.name
                )
        return table

    def limpar_arvore(self):
        self.arvore = None

    def contar_registros(self):
        num_cod = 1
        for _ in self.livros:
            num_cod = num_cod + 1
        return num_cod

    def retornar_disponiveis(self) -> int:
        count = 0
        for livro in self.livros:
            if livro.disponibilidade is Disponibilidade.DISPONIVEL:
                count = count + 1
        return count

    def retornar_indisponiveis(self) -> int:
        count = 0
        for livro in self.livros:
            if livro.disponibilidade is Disponibilidade.INDISPONIVEL:
                count = count + 1
        return count