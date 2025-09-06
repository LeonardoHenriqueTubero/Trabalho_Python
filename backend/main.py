from backend.databases.BaseDadosAluno import BaseDadosAluno
from backend.databases.BaseDadosAutor import BaseDadosAutor
from backend.databases.BaseDadosCidade import BaseDadosCidade
from backend.databases.BaseDadosCurso import BaseDadosCurso
from backend.repository.Repositorio import Repositorio

if __name__ == '__main__':

    repo = Repositorio(
        BaseDadosAutor([], None),
        BaseDadosCidade([], None),
        BaseDadosCurso([], None),
        BaseDadosAluno([], None)
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
