from dataclasses import dataclass
from rich.table import Table
from backend.entities.Arvore import Arvore
from backend.entities.Autor import Autor
from backend.databases.BaseDadosCidade import BaseDadosCidade
import pickle

@dataclass
class BaseDadosAutor:
    autores: list[Autor]
    arvore: Arvore | None = None

    def leitura(self, dados_cidades: BaseDadosCidade):
        codigo = self.contar_registros()
        while True:
            nome = input("Digite um nome: ")
            cidade_cod = int(input("Digite o codigo da cidade: "))
            cidade = dados_cidades.busca_elemento(cidade_cod)
            while cidade is None:
                cidade_cod = int(input("Digite novamente o codigo da cidade: "))
                cidade = dados_cidades.busca_elemento(cidade_cod)
            status = False
            novo = Autor(codigo, nome, cidade, status)
            self.autores.append(novo)

            if not self.continuar():
                break
            codigo = codigo + 1

        with open('backend/data/dado_autores.pkl', 'wb') as file:
            pickle.dump(self.autores, file)

    def incluir_arvore(self):
        inicio = 0
        fim = len(self.autores) - 1
        meio = int((inicio + fim) / 2)
        self.arvore = Arvore(self.autores[meio].cod, meio, None, None)
        for i in range(len(self.autores)):
            if i != meio:
                self.arvore.inserir(self.autores[i].cod, i)

    def busca_elemento(self, cod: int):
        busca = Arvore.busca_no(self.arvore, cod)
        if busca is not None:
            return self.autores[busca.endereco]
        else:
            print(f"Nó não encontrado")
            return None

    def excluir_registro(self, cod: int):
        busca = Arvore.busca_no(self.arvore, cod)
        if busca is not None:
            self.autores[busca.endereco].excluir_dado()
            print(f"O código {cod} foi excluído!")
        self.arvore = Arvore.excluir(self.arvore, cod)

    def metodo_bolha(self):
        n = len(self.autores)
        for i in range (n - 1):
            trocou = False
            for j in range (n - 1 - i):
                if self.autores[j].cod > self.autores[j+1].cod:
                    self.autores[j], self.autores[j + 1] = self.autores[j + 1], self.autores[j]
                    trocou = True
            if not trocou:
                break

    def leitura_exaustiva(self) -> Table:
        lista = self.arvore.em_ordem_retorno()
        table = Table(title="Autores", style="bold cyan")
        table.add_column("Id", justify="center", style="bold yellow")
        table.add_column("Nome", justify="left", style="white")
        table.add_column("Cidade", justify="left", style="white")
        for i in range (len(lista)):
            autor = self.busca_elemento(lista[i])
            if not autor.status:
                table.add_row(str(autor.cod), autor.nome, autor.cidade.descricao)
        return table

    def limpar_arvore(self):
        self.arvore = None

    def contar_registros(self):
        num_cod = 1
        for _ in self.autores:
            num_cod = num_cod + 1
        return num_cod

    def continuar(self):
        while True:
            opcao = input("Continuar a leitura? (S/N): ").strip().upper()
            if opcao in ("S", "N"):
                return opcao == "S"
            print("Opção inválida! Digite apenas S ou N.")