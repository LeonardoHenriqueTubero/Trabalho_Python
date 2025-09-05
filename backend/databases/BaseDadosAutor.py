from dataclasses import dataclass

from backend.entities.Arvore import Arvore
from backend.entities.Autor import Autor
from backend.entities.Cidade import Cidade

@dataclass
class BaseAutorsAutor:
    autores: list[Autor]
    arvore: Arvore | None = None

    def leitura(self):
        codigo = 0
        dados = []
        while True:
            try:
                codigo = int(input("Digite o código (0 para sair): "))
                if codigo == 0:
                    break
            except ValueError:
                print("Código inválido. Por favor, digite um número.")
                continue

            nome = input("Digite um nome: ")
            cidade = Cidade(1, "batata", "SP", False)
            status = False
            novo = Autor(codigo, nome, cidade, status)
            self.autores.append(novo)

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

    def leitura_exaustiva(self):
        lista = self.arvore.em_ordem_retorno()
        for i in range (len(lista)):
            autor = self.busca_elemento(lista[i])
            if not autor.status:
                print(f"{autor}")

    def limpar_arvore(self):
        self.arvore = None