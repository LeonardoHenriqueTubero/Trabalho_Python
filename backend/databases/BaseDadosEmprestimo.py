from dataclasses import dataclass
from datetime import datetime

from backend.databases.BaseDadosAluno import BaseDadosAluno
from backend.databases.BaseDadosCidade import BaseDadosCidade
from backend.databases.BaseDadosCurso import BaseDadosCurso
from backend.databases.BaseDadosLivro import BaseDadosLivro
from backend.entities.Arvore import Arvore
from backend.entities.Emprestimo import Emprestimo

@dataclass
class BaseDadosEmprestimo:
    emprestimos: list[Emprestimo]
    arvore: Arvore | None = None

    def leitura(self, dados_livro: BaseDadosLivro, dados_aluno: BaseDadosAluno):
        codigo = 0
        while True:
            try:
                codigo = int(input("Digite o código (0 para sair): "))
                if codigo == 0:
                    break
            except ValueError:
                print("Código inválido. Por favor, digite um número.")
                continue

            livro_cod = int(input("Digite o codigo do livro: "))
            livro = dados_livro.busca_elemento(livro_cod)
            while livro is None:
                livro_cod = int(input("Digite novamente o codigo do livro: "))
                livro = dados_livro.busca_elemento(livro_cod)
            aluno_cod = int(input("Digite o codigo do aluno: "))
            aluno = dados_aluno.busca_elemento(aluno_cod)
            while aluno is None:
                aluno_cod = int(input("Digite novamente o codigo do aluno: "))
                aluno = dados_aluno.busca_elemento(aluno_cod)
            data_emprestimo = input("Digite a data de emprestimo: ")
            data_retorno = input("Digite a data de retorno: ")
            devolvido = False
            status = False
            emprestimo = datetime.strptime(data_emprestimo, "%d/%m/%Y").date()
            retorno = datetime.strptime(data_retorno, "%d/%m/%Y").date()
            novo = Emprestimo(codigo, livro, aluno, emprestimo, retorno, devolvido, status)
            self.emprestimos.append(novo)

    def incluir_emprestimos(self, emprestimos: list[Emprestimo]):
        for i in range(len(emprestimos)):
            self.emprestimos.append(emprestimos[i])

    def incluir_arvore(self):
        inicio = 0
        fim = len(self.emprestimos) - 1
        meio = int((inicio + fim) / 2)
        self.arvore = Arvore(self.emprestimos[meio].cod, meio, None, None)
        for i in range(len(self.emprestimos)):
            if i != meio:
                self.arvore.inserir(self.emprestimos[i].cod, i)

    def busca_elemento(self, cod: int):
        busca = Arvore.busca_no(self.arvore, cod)
        if busca is not None:
            return self.emprestimos[busca.endereco]
        else:
            print(f"Nó não encontrado")
            return None

    def excluir_registro(self, cod: int):
        busca = Arvore.busca_no(self.arvore, cod)
        if busca is not None:
            self.emprestimos[busca.endereco].excluir_dado()
            print(f"O código {cod} foi excluído!")
        self.arvore = Arvore.excluir(self.arvore, cod)


    def metodo_bolha(self):
        n = len(self.emprestimos)
        for i in range (n - 1):
            trocou = False
            for j in range (n - 1 - i):
                if self.emprestimos[j].cod > self.emprestimos[j+1].cod:
                    self.emprestimos[j], self.emprestimos[j + 1] = self.emprestimos[j + 1], self.emprestimos[j]
                    trocou = True
            if not trocou:
                break

    def leitura_exaustiva(self):
        lista = self.arvore.em_ordem_retorno()
        for i in range (len(lista)):
            emprestimo = self.busca_elemento(lista[i])
            if not emprestimo.status:
                print(f"{emprestimo}")

    def limpar_arvore(self):
        self.arvore = None