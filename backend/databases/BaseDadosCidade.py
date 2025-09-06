from dataclasses import dataclass

from backend.entities.Arvore import Arvore
from backend.entities.Cidade import Cidade

@dataclass
class BaseDadosCidade:
    cidades: list[Cidade]
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
            estado = input("Digite um estado: ")
            status = False
            novo = Cidade(codigo, descricao, estado, status)
            self.cidades.append(novo)

    def incluir_arvore(self):
        inicio = 0
        fim = len(self.cidades) - 1
        meio = int((inicio + fim) / 2)
        self.arvore = Arvore(self.cidades[meio].cod, meio, None, None)
        for i in range(len(self.cidades)):
            if i != meio:
                self.arvore.inserir(self.cidades[i].cod, i)

    def busca_elemento(self, cod: int):
        busca = Arvore.busca_no(self.arvore, cod)
        if busca is not None:
            return self.cidades[busca.endereco]
        else:
            print(f"Nó não encontrado")
            return None

    def excluir_registro(self, cod: int):
        busca = Arvore.busca_no(self.arvore, cod)
        if busca is not None:
            self.cidades[busca.endereco].excluir_dado()
            print(f"O código {cod} foi excluído!")
        self.arvore = Arvore.excluir(self.arvore, cod)

    def metodo_bolha(self):
        n = len(self.cidades)
        for i in range (n - 1):
            trocou = False
            for j in range (n - 1 - i):
                if self.cidades[j].cod > self.cidades[j+1].cod:
                    self.cidades[j], self.cidades[j + 1] = self.cidades[j + 1], self.cidades[j]
                    trocou = True
            if not trocou:
                break

    def leitura_exaustiva(self):
        lista = self.arvore.em_ordem_retorno()
        for i in range (len(lista)):
            cidades = self.busca_elemento(lista[i])
            if not cidades.status:
                print(f"{cidades}")

    def limpar_arvore(self):
        self.arvore = None