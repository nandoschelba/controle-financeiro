from entidade.categoria import Categoria


class Meta:
    ultimo_codigo = 0
    def __init__(self, meta: float, categoria: Categoria, usuario: int):
        Meta.ultimo_codigo += 1
        self.__codigo = Meta.ultimo_codigo
        self.__meta = meta
        self.__categoria = categoria
        self.__usuario = usuario

    @property
    def codigo(self):
        return self.__codigo

    @property
    def categoria(self):
        return self.__categoria

    @property
    def meta(self):
        return self.__meta

    @property
    def usuario(self):
        return self.__usuario