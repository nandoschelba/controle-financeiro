from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nome: str, email: str):
        self.__nome = nome
        self.__email = email

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
