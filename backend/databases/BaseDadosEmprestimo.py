from dataclasses import dataclass
from datetime import datetime, timedelta, date

from backend.databases.BaseDadosAluno import BaseDadosAluno
from backend.databases.BaseDadosLivro import BaseDadosLivro
from backend.entities.Arvore import Arvore
from backend.entities.Emprestimo import Emprestimo
import pickle

from backend.entities.enums.Disponibilidade import Disponibilidade


@dataclass
class BaseDadosEmprestimo:
    emprestimos: list[Emprestimo]
    arvore: Arvore | None = None

    def leitura(self, dados_livro: BaseDadosLivro, dados_aluno: BaseDadosAluno):
        codigo = self.contar_registros()
        livro_cod = int(input("Digite o codigo do livro: "))
        livro = dados_livro.busca_elemento(livro_cod)
        while livro is None:
            livro_cod = int(input("Digite novamente o codigo do livro: "))
            livro = dados_livro.busca_elemento(livro_cod)
        if livro.disponibilidade is Disponibilidade.INDISPONIVEL:
            print("Livro Indisponivel para Emprestimos")
        else:
            dados_livro.mudar_disponibilidade(livro_cod)
            aluno_cod = int(input("Digite o codigo do aluno: "))
            aluno = dados_aluno.busca_elemento(aluno_cod)
            while aluno is None:
                aluno_cod = int(input("Digite novamente o codigo do aluno: "))
                aluno = dados_aluno.busca_elemento(aluno_cod)
            emprestimo = datetime.strptime(input("Digite a data de emprestimo: "), "%d/%m/%Y").date()
            retorno = emprestimo + timedelta(days=7)
            devolvido = False
            status = False
            novo = Emprestimo(codigo, livro, aluno, emprestimo, retorno, devolvido, status)
            self.emprestimos.append(novo)

        with open('data/dado_emprestimos.pkl', 'wb') as file:
            pickle.dump(self.emprestimos, file)
        with open('data/dado_livros.pkl', 'wb') as file:
            pickle.dump(dados_livro, file)

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

    def contar_registros(self):
        num_cod = 1
        for _ in self.emprestimos:
            num_cod = num_cod + 1
        return num_cod

    def devolucao(self, dados_livros : BaseDadosLivro):
        self.leitura_exaustiva()
        data_atual = date.today()
        emprestimo = self.busca_elemento(int(input("Qual emprestimo quer realizar a devolucao?")))

        if emprestimo is None:
            return
        
        if data_atual > emprestimo.data_devolucao:
            print(f"O livro esta {(data_atual - emprestimo.data_devolucao).days} atrasado!")
        emprestimo.devolvido = True
        dados_livros.mudar_disponibilidade(emprestimo.livro.cod)
        with open("data/dado_emprestimos.pkl", "wb") as file:
            pickle.dump(self.emprestimos, file)