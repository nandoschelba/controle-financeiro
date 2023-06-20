from entidade.usuario import Usuario


class Categoria:
    def __init__(self, codigo: int, nome: str, descricao: str, usuario: int):
        self.__codigo = codigo
        self.__nome = nome
        self.__descricao = descricao
        self.__usuario = usuario

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
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario: Usuario):
        self.__usuario = usuario
