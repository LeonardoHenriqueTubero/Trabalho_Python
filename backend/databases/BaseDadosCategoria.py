from dataclasses import dataclass

from backend.entities.Arvore import Arvore
from backend.entities.Categoria import Categoria
import pickle

@dataclass
class BaseDadosCategoria:
    categorias: list[Categoria]
    arvore: Arvore | None = None

    def leitura(self):
        codigo = self.contar_registros()
        while True:
            descricao = input("Digite uma descricao: ")
            status = False
            novo = Categoria(codigo, descricao, status)
            self.categorias.append(novo)

            if not self.continuar():
                break
            codigo = codigo + 1

        with open('backend/data/dado_categorias.pkl', 'wb') as file:
            pickle.dump(self.categorias, file)

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

    def contar_registros(self):
        num_cod = 1
        for _ in self.categorias:
            num_cod = num_cod + 1
        return num_cod

    def continuar(self):
        while True:
            opcao = input("Continuar a leitura? (S/N): ").strip().upper()
            if opcao in ("S", "N"):
                return opcao == "S"
            print("Opção inválida! Digite apenas S ou N.")