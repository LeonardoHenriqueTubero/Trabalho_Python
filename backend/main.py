from rich.console import Console
from rich.table import Table
import questionary

console = Console()

def mostrar_tabela():
    # Criando a tabela
    table = Table(title="Exemplo de Tabela com Rich")

    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Nome", style="magenta")
    table.add_column("Idade", justify="right", style="green")

    # Dados de exemplo
    pessoas = [
        {"id": "1", "nome": "Alice", "idade": 25},
        {"id": "2", "nome": "Bob", "idade": 30},
        {"id": "3", "nome": "Charlie", "idade": 22},
    ]

    for pessoa in pessoas:
        table.add_row(pessoa["id"], pessoa["nome"], str(pessoa["idade"]))

    console.print(table)

def main():
    while True:
        escolha = questionary.select(
            "O que deseja fazer?",
            choices=[
                "Mostrar tabela",
                "Adicionar pessoa",
                "Sair"
            ]
        ).ask()

        if escolha == "Mostrar tabela":
            mostrar_tabela()

        elif escolha == "Adicionar pessoa":
            nome = questionary.text("Digite o nome:").ask()
            idade = questionary.text(
                "Digite a idade:",
                validate=lambda val: val.isdigit() or "Digite um número válido"
            ).ask()
            console.print(f"[bold green]Pessoa adicionada:[/] {nome}, {idade} anos!")

        elif escolha == "Sair":
            console.print("[bold red]Saindo do programa...[/]")
            break

def main1():
    print("=== Bem-vindo ao Menu Interativo ===")

    # Pergunta de seleção
    escolha = questionary.select(
        "O que você quer fazer?",
        choices=[
            "Dizer Olá",
            "Somar dois números",
            "Sair"
        ]
    ).ask()

    if escolha == "Dizer Olá":
        nome = questionary.text("Qual é o seu nome?").ask()
        print(f"Olá, {nome}!")

    elif escolha == "Somar dois números":
        n1 = questionary.text("Digite o primeiro número:", validate=lambda val: val.isdigit() or "Digite um número válido").ask()
        n2 = questionary.text("Digite o segundo número:", validate=lambda val: val.isdigit() or "Digite um número válido").ask()
        print(f"A soma é: {int(n1) + int(n2)}")

    elif escolha == "Sair":
        print("Tchau!")
        return

    # Pergunta se quer continuar
    continuar = questionary.confirm("Quer continuar?").ask()
    if continuar:
        main()
    else:
        print("Programa encerrado.")

if __name__ == "__main__":
    main()
    main1()
