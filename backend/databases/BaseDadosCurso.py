from dataclasses import dataclass

from backend.entities.Arvore import Arvore
from backend.entities.Curso import Curso
import pickle

@dataclass
class BaseDadosCurso:
    cursos: list[Curso]
    arvore: Arvore | None = None

    def leitura(self):
        codigo = self.contar_registros()
        while True:
            descricao = input("Digite uma descricao: ")
            status = False
            novo = Curso(codigo, descricao, status)
            self.cursos.append(novo)

            if not self.continuar():
                break
            codigo = codigo + 1

        with open('backend/data/dado_cursos.pkl', 'wb') as file:
            pickle.dump(self.cursos, file)

    def incluir_arvore(self):
        inicio = 0
        fim = len(self.cursos) - 1
        meio = int((inicio + fim) / 2)
        self.arvore = Arvore(self.cursos[meio].cod, meio, None, None)
        for i in range(len(self.cursos)):
            if i != meio:
                self.arvore.inserir(self.cursos[i].cod, i)

    def busca_elemento(self, cod: int):
        busca = Arvore.busca_no(self.arvore, cod)
        if busca is not None:
            return self.cursos[busca.endereco]
        else:
            print(f"Nó não encontrado")
            return None

    def excluir_registro(self, cod: int):
        busca = Arvore.busca_no(self.arvore, cod)
        if busca is not None:
            self.cursos[busca.endereco].excluir_dado()
            print(f"O código {cod} foi excluído!")
        self.arvore = Arvore.excluir(self.arvore, cod)

    def metodo_bolha(self):
        n = len(self.cursos)
        for i in range (n - 1):
            trocou = False
            for j in range (n - 1 - i):
                if self.cursos[j].cod > self.cursos[j+1].cod:
                    self.cursos[j], self.cursos[j + 1] = self.cursos[j + 1], self.cursos[j]
                    trocou = True
            if not trocou:
                break

    def leitura_exaustiva(self):
        lista = self.arvore.em_ordem_retorno()
        for i in range (len(lista)):
            cursos = self.busca_elemento(lista[i])
            if not cursos.status:
                print(f"{cursos}")

    def limpar_arvore(self):
        self.arvore = None

    def contar_registros(self):
        num_cod = 1
        for _ in self.cursos:
            num_cod = num_cod + 1
        return num_cod

    def continuar(self):
        while True:
            opcao = input("Continuar a leitura? (S/N): ").strip().upper()
            if opcao in ("S", "N"):
                return opcao == "S"
            print("Opção inválida! Digite apenas S ou N.")