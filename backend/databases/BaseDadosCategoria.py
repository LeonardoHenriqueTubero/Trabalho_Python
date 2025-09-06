from dataclasses import dataclass

from backend.entities.Arvore import Arvore
from backend.entities.Categoria import Categoria

@dataclass
class BaseDadosCategoria:
    categorias: list[Categoria]
    arvore: Arvore | None = None

    def leitura(self):
        codigo = 0
        while True:
            try:
                codigo = int(input("Digite o código (0 para sair): "))
                if codigo == 0:
                    break
            except ValueError:
                print("Código inválido. Por favor, digite um número.")
                continue

            descricao = input("Digite uma descricao: ")
            status = False
            novo = Categoria(codigo, descricao, status)
            self.categorias.append(novo)

    def incluir_arvore(self):
        inicio = 0
        fim = len(self.categorias) - 1
        meio = int((inicio + fim) / 2)
        self.arvore = Arvore(self.categorias[meio].cod, meio, None, None)
        for i in range(len(self.categorias)):
            if i != meio:
                self.arvore.inserir(self.categorias[i].cod, i)

    def busca_elemento(self, cod: int):
        busca = Arvore.busca_no(self.arvore, cod)
        if busca is not None:
            return self.categorias[busca.endereco]
        else:
            print(f"Nó não encontrado")
            return None

    def excluir_registro(self, cod: int):
        busca = Arvore.busca_no(self.arvore, cod)
        if busca is not None:
            self.categorias[busca.endereco].excluir_dado()
            print(f"O código {cod} foi excluído!")
        self.arvore = Arvore.excluir(self.arvore, cod)

    def metodo_bolha(self):
        n = len(self.categorias)
        for i in range (n - 1):
            trocou = False
            for j in range (n - 1 - i):
                if self.categorias[j].cod > self.categorias[j+1].cod:
                    self.categorias[j], self.categorias[j + 1] = self.categorias[j + 1], self.categorias[j]
                    trocou = True
            if not trocou:
                break

    def leitura_exaustiva(self):
        lista = self.arvore.em_ordem_retorno()
        for i in range (len(lista)):
            categorias = self.busca_elemento(lista[i])
            if not categorias.status:
                print(f"{categorias}")

    def limpar_arvore(self):
        self.arvore = None