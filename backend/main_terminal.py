from backend.repository.Repositorio import Repositorio
import os

def exibir_menu():
    print("=" * 58)
    print("{:^60}".format("📚 MENU PRINCIPAL 📚"))
    print("=" * 58)
    print(f"| {'Opção':^6} | {'Descrição':^45} |")
    print("-" * 58)
    print(f"| {'1':^6} | {'Consultar alunos':45} |")
    print(f"| {'2':^6} | {'Consultar autores':45} |")
    print(f"| {'3':^6} | {'Incluir livros':45} |")
    print(f"| {'4':^6} | {'Consultar livros':45} |")
    print(f"| {'5':^6} | {'Realizar empréstimo':45} |")
    print(f"| {'6':^6} | {'Consultar empréstimos':45} |")
    print(f"| {'7':^6} | {'Realizar devolução':45} |")
    print(f"| {'8':^6} | {'Consultar livros emprestados':45} |")
    print(f"| {'9':^6} | {'Livros com devolução atrasada':45} |")
    print(f"| {'10':^6} | {'Qtd. de livros emprestados por período':45} |")
    print("=" * 58)

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    repo = Repositorio.iniciar_repositorio()
    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))
        match opcao:
            case 0:
                print("Saindo do sistema")
                break
            case 1:
                repo.carregar_cidades()
                repo.carregar_cursos()
                repo.carregar_alunos()
                repo.dados_alunos.leitura_exaustiva()
            case 2:
                repo.carregar_cidades()
                repo.carregar_autores()
                repo.dados_autores.leitura_exaustiva()
            case 3:
                repo.carregar_cidades()
                repo.carregar_autores()
                repo.carregar_categorias()
                repo.dados_livros.leitura(repo.dados_autores, repo.dados_categorias)
            case 4:
                repo.carregar_cidades()
                repo.carregar_autores()
                repo.carregar_categorias()
                repo.carregar_livros()
                repo.dados_livros.leitura_exaustiva()
            case 5:
                repo.carregar_cidades()
                repo.carregar_cursos()
                repo.carregar_alunos()
                repo.carregar_autores()
                repo.carregar_categorias()
                repo.carregar_livros()
                repo.dados_emprestimos.leitura(repo.dados_livros, repo.dados_alunos)
            case 6:
                repo.carregar_cidades()
                repo.carregar_cursos()
                repo.carregar_alunos()
                repo.carregar_autores()
                repo.carregar_categorias()
                repo.carregar_livros()
                repo.carregar_emprestimos()
                repo.dados_emprestimos.leitura_exaustiva()
            case 7:
                repo.carregar_cidades()
                repo.carregar_cursos()
                repo.carregar_alunos()
                repo.carregar_autores()
                repo.carregar_categorias()
                repo.carregar_livros()
                repo.carregar_emprestimos()
                repo.dados_emprestimos.devolucao(repo.dados_livros)

        input()
        print("\n" * 50)