from entidade.categoria import Categoria
from entidade.usuario import Usuario


class Meta:
    ultimo_codigo = 0

    def __init__(self, meta: float, categoria: Categoria, usuario: Usuario):
        Meta.ultimo_codigo += 1
        self.__codigo = Meta.ultimo_codigo
        self.__meta = meta
        self.__categoria = categoria
        self.__usuario = usuario

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def meta(self):
        return self.__meta

    @meta.setter
    def meta(self, meta):
        self.__meta = meta

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario
