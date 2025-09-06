from backend.databases.BaseDadosAluno import BaseDadosAluno
from backend.databases.BaseDadosAutor import BaseDadosAutor
from backend.databases.BaseDadosCategoria import BaseDadosCategoria
from backend.databases.BaseDadosCidade import BaseDadosCidade
from backend.databases.BaseDadosCurso import BaseDadosCurso
from backend.databases.BaseDadosEmprestimo import BaseDadosEmprestimo
from backend.databases.BaseDadosLivro import BaseDadosLivro
from backend.repository.Repositorio import Repositorio

if __name__ == '__main__':

    repo = Repositorio(
        BaseDadosAutor([]),
        BaseDadosCidade([]),
        BaseDadosCurso([]),
        BaseDadosAluno([]),
        BaseDadosCategoria([]),
        BaseDadosLivro([]),
        BaseDadosEmprestimo([])
    )


    print(f"===Cidades===")
    print(f"")

    repo.dados_cidades.leitura()
    repo.dados_cidades.incluir_arvore()
    repo.dados_cidades.leitura_exaustiva()

    print(f"")
    print(f"===Cursos===")
    print(f"")

    repo.dados_cursos.leitura()
    repo.dados_cursos.incluir_arvore()
    repo.dados_cursos.leitura_exaustiva()

    print(f"")
    print(f"===Alunos===")
    print(f"")

    repo.dados_alunos.leitura(repo.dados_cursos, repo.dados_cidades)
    repo.dados_alunos.incluir_arvore()
    repo.dados_alunos.leitura_exaustiva()

    print(f"")
    print(f"===Autor===")
    print(f"")

    repo.dados_autores.leitura(repo.dados_cidades)
    repo.dados_autores.incluir_arvore()
    repo.dados_autores.leitura_exaustiva()

    print(f"")
    print(f"===Categorias===")
    print(f"")

    repo.dados_categorias.leitura()
    repo.dados_categorias.incluir_arvore()
    repo.dados_categorias.leitura_exaustiva()

    print(f"")
    print(f"===Livros===")
    print(f"")

    repo.dados_livros.leitura(repo.dados_autores, repo.dados_categorias)
    repo.dados_livros.incluir_arvore()
    repo.dados_livros.leitura_exaustiva()

    print(f"")
    print(f"===Emprestimos===")
    print(f"")

    repo.dados_emprestimos.leitura(repo.dados_livros, repo.dados_alunos)
    repo.dados_emprestimos.incluir_arvore()
    repo.dados_emprestimos.leitura_exaustiva()
