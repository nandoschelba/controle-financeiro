from abc import ABC, abstractmethod
from entidade.categoria import Categoria

class Usuario(ABC):
    def __init__(self, nome: str, email: str):
        self.__nome = nome
        self.__email = email
        self.__categorias = []
        self.__logado = False

    @abstractmethod
    def identificador(self):
        pass

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def login(self):
        self.__logado = True

    def logout(self):
        self.__logado = False

    def checa_status_logado(self):
        return self.__logado

    def add_categoria(self, categoria: Categoria):
        if categoria not in self.__categorias:
            self.__categorias.append(categoria)

    def delete_categoria(self, categoria: Categoria):
        if categoria in self.__categorias:
            self.__categorias.remove(categoria)

    def editar_categoria(self):
        pass

    def listar_categorias(self):
        pass
