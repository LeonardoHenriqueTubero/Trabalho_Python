import re
from dataclasses import dataclass
from datetime import datetime, timedelta, date

import questionary
from questionary import Choice
from rich.console import Console
from rich.table import Table

from backend.databases.BaseDadosAluno import BaseDadosAluno
from backend.databases.BaseDadosLivro import BaseDadosLivro
from backend.entities.Arvore import Arvore
from backend.entities.Emprestimo import Emprestimo
import pickle

from backend.entities.enums.Disponibilidade import Disponibilidade

console = Console(force_terminal=True)

@dataclass
class BaseDadosEmprestimo:
    emprestimos: list[Emprestimo]
    arvore: Arvore | None = None

    def leitura(self, dados_livro: BaseDadosLivro, dados_aluno: BaseDadosAluno):
        if not dados_livro.livros:
            console.print(f"[bold red]!Nenhum livro cadastrado!")
        else:
            codigo = self.contar_registros()
            livro_cod = int(questionary.text("Digite o codigo do livro:", validate=lambda val: val.isdigit() or "Digite um número válido").ask())
            livro = dados_livro.busca_elemento(int(livro_cod))
            while livro is None:
                livro_cod = questionary.text("Digite novamente o codigo do livro:", validate=lambda val: val.isdigit() or "Digite um número válido").ask()
                livro = dados_livro.busca_elemento(int(livro_cod))
            if livro.disponibilidade is Disponibilidade.INDISPONIVEL:
                console.print(f"[bold red]!Livro Indisponivel para Emprestimos!")
            else:
                dados_livro.mudar_disponibilidade(livro_cod)
                aluno_cod = questionary.text("Digite o codigo do aluno:", validate=lambda val: val.isdigit() or "Digite um número válido").ask()
                aluno = dados_aluno.busca_elemento(int(aluno_cod))
                while aluno is None:
                    aluno_cod = questionary.text("Digite novamente o codigo do aluno:", validate=lambda val: val.isdigit() or "Digite um número válido").ask()
                    aluno = dados_aluno.busca_elemento(aluno_cod)
                emprestimo = date.today()
                retorno = emprestimo + timedelta(days=7)
                devolvido = False
                status = False
                novo = Emprestimo(codigo, livro, aluno, emprestimo, retorno, devolvido, status)
                self.emprestimos.append(novo)

        with open('backend/data/dado_emprestimos.pkl', 'wb') as file:
            pickle.dump(self.emprestimos, file)
        with open('backend/data/dado_livros.pkl', 'wb') as file:
            pickle.dump(dados_livro.livros, file)

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

    def leitura_exaustiva(self) -> Table | None:
        if not self.emprestimos:
            return None
        lista = self.arvore.em_ordem_retorno()
        table = Table(title="Emprestimos", style="bold cyan")
        table.add_column("Id", justify="center", style="bold yellow")
        table.add_column("Livro", justify="left", style="white")
        table.add_column("Aluno", justify="left", style="white")
        table.add_column("Data Emprestimo", justify="left", style="white")
        table.add_column("Data Devolucao", justify="left", style="white")
        table.add_column("Devolvido", justify="left", style="white")
        for i in range (len(lista)):
            emprestimo = self.busca_elemento(lista[i])
            if not emprestimo.status:
                table.add_row(
                    str(emprestimo.cod),
                    emprestimo.livro.titulo,
                    emprestimo.aluno.nome,
                    emprestimo.data_emprestimo.strftime('%d/%m/%Y'),
                    emprestimo.data_devolucao.strftime('%d/%m/%Y'),
                    'SIM' if emprestimo.devolvido is True else 'NAO'
                )
        return table

    def leitura_exaustiva_atrasado(self) -> Table | None:
        if not self.emprestimos:
            return None
        lista = self.arvore.em_ordem_retorno()
        table = Table(title="Emprestimos", style="bold cyan")
        table.add_column("Id", justify="center", style="bold yellow")
        table.add_column("Livro", justify="left", style="white")
        table.add_column("Aluno", justify="left", style="white")
        table.add_column("Data Emprestimo", justify="left", style="white")
        table.add_column("Data Devolucao", justify="left", style="white")
        table.add_column("Devolvido", justify="left", style="white")
        for i in range (len(lista)):
            emprestimo = self.busca_elemento(lista[i])
            if not emprestimo.status and date.today() > emprestimo.data_devolucao:
                table.add_row(
                    str(emprestimo.cod),
                    emprestimo.livro.titulo,
                    emprestimo.aluno.nome,
                    emprestimo.data_emprestimo.strftime('%d/%m/%Y'),
                    emprestimo.data_devolucao.strftime('%d/%m/%Y'),
                    'SIM' if emprestimo.devolvido is True else 'NAO'
                )
        return table

    def leitura_exaustiva_disponivel(self) -> list[str] | None:
        if not self.emprestimos:
            return None
        lista = self.arvore.em_ordem_retorno()
        emprestimos_disponiveis = []
        for i in range (len(lista)):
            emprestimo = self.busca_elemento(lista[i])
            if not emprestimo.status and emprestimo.devolvido is False:
                emprestimo_disponivel = {
                    "id": emprestimo.cod,
                    "titulo_livro": emprestimo.livro.titulo
                }
                emprestimos_disponiveis.append(emprestimo_disponivel)
        return emprestimos_disponiveis

    def qtd_emprestimo_periodo(self):
        if not self.emprestimos:
            return
        count = 0
        data_inicial_str = questionary.text("Digite a data inicial (dd/mm/aaaa):", validate=self.validar_data).ask()
        data_final_str = questionary.text("Digite a data final (dd/mm/aaaa):", validate=self.validar_data).ask()
        data_inicial = datetime.strptime(data_inicial_str, "%d/%m/%Y").date()
        data_final = datetime.strptime(data_final_str, "%d/%m/%Y").date()
        for emprestimo in self.emprestimos:
            if data_inicial <= emprestimo.data_emprestimo <= data_final:
                count = count + 1
        console.print(f"[bold yellow]Numero de emprestimos por período: {count}")

    def limpar_arvore(self):
        self.arvore = None

    def contar_registros(self):
        num_cod = 1
        for _ in self.emprestimos:
            num_cod = num_cod + 1
        return num_cod

    def contar_registros_disponivel(self):
        for emprestimo in self.emprestimos:
            if emprestimo.devolvido is False:
                return True
        return False

    def devolucao(self, dados_livros : BaseDadosLivro):
        if not self.contar_registros_disponivel():
            return
        else:
            data_atual = date.today()
            emprestimo = self.busca_elemento(int(questionary.select(
                "Qual emprestimo quer realizar a devolucao?",
            choices=[Choice(title=e["titulo_livro"], value=e["id"])
                     for e in self.leitura_exaustiva_disponivel()]).ask()))

            if emprestimo is None and emprestimo.devolvido is True:
                return

            if data_atual > emprestimo.data_devolucao:
                console.print(f"O livro esta [bold red]{(data_atual - emprestimo.data_devolucao).days}[/bold red] dia(s) atrasado!")
            emprestimo.devolvido = True
            dados_livros.mudar_disponibilidade(emprestimo.livro.cod)
            with open('backend/data/dado_emprestimos.pkl', 'wb') as file:
                pickle.dump(self.emprestimos, file)
            with open('backend/data/dado_livros.pkl', 'wb') as file:
                pickle.dump(dados_livros.livros, file)

    def validar_data(self, valor):
        padrao = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}$'
        if re.match(padrao, valor):
            return True
        return "Data inalida! Use o formato dd/mm/aaaa."