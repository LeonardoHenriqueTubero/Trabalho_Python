import questionary
from rich.panel import Panel

from backend.repository.Repositorio import Repositorio
from rich.console import Console
import pyfiglet

console = Console(force_terminal=True)

def exibir_painel():

    texto = pyfiglet.figlet_format("Sistema de Biblioteca")
    print(texto)


if __name__ == "__main__":
    repo = Repositorio.iniciar_repositorio()
    while True:
        exibir_painel()
        escolha = questionary.select(
            "O que deseja fazer?",
            choices=[
                "Consultar alunos",
                "Consultar autores",
                "Incluir livros",
                "Consultar livros",
                "Realizar empréstimo",
                "Consultar empréstimos",
                "Realizar devolução",
                "Consultar livros emprestados",
                "Empréstimos com devolução atrasada",
                "Qtd. de livros emprestados por período",
                "Sair"
            ]
        ).ask()
        match escolha:
            case "Sair":
                console.print(f"[bold red]Saindo do sistema...")
                break
            case "Consultar alunos":
                repo.carregar_cidades()
                repo.carregar_cursos()
                repo.carregar_alunos()
                alunos = repo.dados_alunos.leitura_exaustiva()
                console.print(alunos)
            case "Consultar autores":
                repo.carregar_cidades()
                repo.carregar_autores()
                autores = repo.dados_autores.leitura_exaustiva()
                console.print(autores)
            case "Incluir livros":
                console.print(Panel.fit("[bold cyan]Cadastro de Livros[/bold cyan]", style="bold cyan"))
                repo.carregar_cidades()
                repo.carregar_autores()
                repo.carregar_categorias()
                repo.carregar_livros()
                repo.dados_livros.leitura(repo.dados_autores, repo.dados_categorias)
            case "Consultar livros":
                repo.carregar_cidades()
                repo.carregar_autores()
                repo.carregar_categorias()
                repo.carregar_livros()
                livros = repo.dados_livros.leitura_exaustiva()
                console.print(livros)
                disponiveis = repo.dados_livros.retornar_disponiveis()
                indisponiveis = repo.dados_livros.retornar_indisponiveis()
                console.print(f"[bold green]Livros disponiveis: {disponiveis}")
                console.print(f"[bold red]Livro indisponiveis: {indisponiveis}")
            case "Realizar empréstimo":
                console.print(Panel.fit("[bold cyan]Realizar Emprestimos[/bold cyan]", style="bold cyan"))
                repo.carregar_cidades()
                repo.carregar_cursos()
                repo.carregar_alunos()
                repo.carregar_autores()
                repo.carregar_categorias()
                repo.carregar_livros()
                repo.dados_emprestimos.leitura(repo.dados_livros, repo.dados_alunos)
            case "Consultar empréstimos":
                repo.carregar_cidades()
                repo.carregar_cursos()
                repo.carregar_alunos()
                repo.carregar_autores()
                repo.carregar_categorias()
                repo.carregar_livros()
                repo.carregar_emprestimos()
                emprestimos = repo.dados_emprestimos.leitura_exaustiva()
                console.print(emprestimos)
            case "Realizar devolução":
                console.print(Panel.fit("[bold cyan]Realizar a devolução[/bold cyan]", style="bold cyan"))
                repo.carregar_cidades()
                repo.carregar_cursos()
                repo.carregar_alunos()
                repo.carregar_autores()
                repo.carregar_categorias()
                repo.carregar_livros()
                repo.carregar_emprestimos()
                repo.dados_emprestimos.devolucao(repo.dados_livros)
            case "Consultar livros emprestados":
                repo.carregar_cidades()
                repo.carregar_cursos()
                repo.carregar_alunos()
                repo.carregar_autores()
                repo.carregar_categorias()
                repo.carregar_livros()
                livros_emprestados = repo.dados_livros.leitura_exaustiva_emprestados()
                console.print(livros_empresta)
            case "Empréstimos com devolução atrasada":
                repo.carregar_cidades()
                repo.carregar_cursos()
                repo.carregar_alunos()
                repo.carregar_autores()
                repo.carregar_categorias()
                repo.carregar_livros()
                repo.carregar_emprestimos()
                repo.dados_emprestimos.leitura_exaustiva_atrasado()
            case "Qtd. de livros emprestados por período":
                repo.carregar_cidades()
                repo.carregar_cursos()
                repo.carregar_alunos()
                repo.carregar_autores()
                repo.carregar_categorias()
                repo.carregar_livros()
                repo.carregar_emprestimos()
                repo.dados_emprestimos.qtd_emprestimo_periodo()
        input()