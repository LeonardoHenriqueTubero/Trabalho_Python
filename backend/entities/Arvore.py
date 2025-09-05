from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Arvore:
    codigo: int
    endereco: int
    esquerda: Arvore | None = None
    direita: Arvore | None = None

    def inserir(self, codigo: int, endereco: int) -> Arvore:
        if codigo < self.codigo:
            if self.esquerda is None:
                self.esquerda = Arvore(codigo, endereco, None, None)
            else:
                self.esquerda.inserir(codigo, endereco)
        elif codigo > self.codigo:
            if self.direita is None:
                self.direita = Arvore(codigo, endereco, None, None)
            else:
                self.direita.inserir(codigo, endereco)
        return self

    @classmethod
    def busca_no(cls, raiz: Arvore, codigo: int) -> Arvore | None:
        if raiz is None:
            return None
        if codigo < raiz.codigo:
            return cls.busca_no(raiz.esquerda, codigo)
        elif codigo > raiz.codigo:
            return cls.busca_no(raiz.direita, codigo)
        else:
            return raiz

    def em_ordem(self):
        if self.esquerda:
            self.esquerda.em_ordem()
        print(f"{self.codigo}, {self.endereco}")
        if self.direita:
            self.direita.em_ordem()

    def em_ordem_retorno(self) -> list[int]:
        resultado = []
        if self.esquerda:
            resultado.extend(self.esquerda.em_ordem_retorno())
        resultado.append(self.codigo)
        if self.direita:
            resultado.extend(self.direita.em_ordem_retorno())
        return resultado

    def pre_ordem(self):
        print(f"{self.codigo}, {self.endereco}")
        if self.esquerda:
            self.esquerda.em_ordem()
        if self.direita:
            self.direita.em_ordem()

    def pos_ordem(self):
        if self.esquerda:
            self.esquerda.em_ordem()
        if self.direita:
            self.direita.em_ordem()
        print(f"{self.codigo}, {self.endereco}")

    @classmethod
    def excluir(cls, raiz : Arvore, cod : int):
        if raiz is None:
            print(f"Elemento não existe.")
            return None
        else:
            if cod < raiz.codigo:
                raiz.esquerda = cls.excluir(raiz.esquerda, cod)
            elif cod > raiz.codigo:
                raiz.direita = cls.excluir(raiz.direita, cod)
            else:
                if raiz.esquerda is None:
                    temp = raiz.direita
                    return temp
                elif raiz.direita is None:
                    temp = raiz.esquerda
                    return temp
                else:
                    temp = cls.minimo(raiz.direita)

                    raiz.codigo = temp.codigo
                    raiz.endereco = temp.endereco

                    raiz.direita = cls.excluir(raiz.direita, temp.codigo)
        return raiz

    @classmethod
    def minimo(cls, raiz: Arvore):
        atual = raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual