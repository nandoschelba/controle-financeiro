

class Categoria:
    def __init__(self, codigo: int, nome: str, descricao: str, id_usuario: int):
        self.__codigo = codigo
        self.__nome = nome
        self.__descricao = descricao
        self.__id_usuario = id_usuario

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def id_usuario(self):
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario
