from dataclasses import dataclass

from backend.databases.BaseDadosCidade import BaseDadosCidade
from backend.databases.BaseDadosCurso import BaseDadosCurso
from backend.entities.Arvore import Arvore
from backend.entities.Aluno import Aluno
import pickle

@dataclass
class BaseDadosAluno:
    alunos: list[Aluno]
    arvore: Arvore | None = None

    def leitura(self, dados_curso: BaseDadosCurso, dados_cidade: BaseDadosCidade):
        codigo = self.contar_registros()
        while True:
            nome = input("Digite um nome: ")
            curso_cod = int(input("Digite o codigo do curso: "))
            curso = dados_curso.busca_elemento(curso_cod)
            while curso is None:
                curso_cod = int(input("Digite novamente o codigo do curso: "))
                curso = dados_curso.busca_elemento(curso_cod)
            cidade_cod = int(input("Digite o codigo da cidade: "))
            cidade = dados_cidade.busca_elemento(cidade_cod)
            while cidade is None:
                cidade_cod = int(input("Digite novamente o codigo da cidade: "))
                cidade = dados_cidade.busca_elemento(cidade_cod)
            status = False
            novo = Aluno(codigo, nome, curso, cidade, status)
            self.alunos.append(novo)

            if not self.continuar():
                break
            codigo = codigo + 1

        with open('data/dado_alunos.pkl', 'wb') as file:
            pickle.dump(self.alunos, file)

    def incluir_alunos(self, alunos: list[Aluno]):
        for i in range(len(alunos)):
            self.alunos.append(alunos[i])

    def incluir_arvore(self):
        inicio = 0
        fim = len(self.alunos) - 1
        meio = int((inicio + fim) / 2)
        self.arvore = Arvore(self.alunos[meio].cod, meio, None, None)
        for i in range(len(self.alunos)):
            if i != meio:
                self.arvore.inserir(self.alunos[i].cod, i)

    def busca_elemento(self, cod: int):
        busca = Arvore.busca_no(self.arvore, cod)
        if busca is not None:
            return self.alunos[busca.endereco]
        else:
            print(f"Nó não encontrado")
            return None

    def excluir_registro(self, cod: int):
        busca = Arvore.busca_no(self.arvore, cod)
        if busca is not None:
            self.alunos[busca.endereco].excluir_dado()
            print(f"O código {cod} foi excluído!")
        self.arvore = Arvore.excluir(self.arvore, cod)


    def metodo_bolha(self):
        n = len(self.alunos)
        for i in range (n - 1):
            trocou = False
            for j in range (n - 1 - i):
                if self.alunos[j].cod > self.alunos[j+1].cod:
                    self.alunos[j], self.alunos[j + 1] = self.alunos[j + 1], self.alunos[j]
                    trocou = True
            if not trocou:
                break

    def leitura_exaustiva(self):
        lista = self.arvore.em_ordem_retorno()
        for i in range (len(lista)):
            aluno = self.busca_elemento(lista[i])
            if not aluno.status:
                print(f"{aluno}")

    def limpar_arvore(self):
        self.arvore = None

    def contar_registros(self):
        num_cod = 1
        for _ in self.alunos:
            num_cod = num_cod + 1
        return num_cod

    def continuar(self):
        while True:
            opcao = input("Continuar a leitura? (S/N): ").strip().upper()
            if opcao in ("S", "N"):
                return opcao == "S"
            print("Opção inválida! Digite apenas S ou N.")