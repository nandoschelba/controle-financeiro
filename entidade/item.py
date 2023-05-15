from entidade.categoria import Categoria


class Item:
    ultimo_codigo = 0
    def __init__(self, valor: float, descricao: str, categoria: Categoria):
        Item.ultimo_codigo += 1
        self.__codigo = Item.ultimo_codigo
        self.__valor = valor
        self.__descricao = descricao
        self.__categoria = categoria

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria
