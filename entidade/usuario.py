from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nome: str, email: str, categorias: list):
        self.__nome = nome
        self.__email = email
        self.__categorias = categorias

    @abstractmethod
    def identificador(self):
        pass

    def nome(self, nome):
        self.__nome = nome
        return self.__nome

    def email(self, email):
        self.__email = email
        return self.__email

    def add_categoria(self, categoria):
        if categoria not in self.__categorias:
            self.__categorias.append(categoria)

    def delete_categoria(self, categoria):
        if categoria in self.__categorias:
            self.__categorias.remove(categoria)

    def editar_categoria(self, categoria_antiga, categoria_nova):
        pass

    def listar_categorias(self):
        pass