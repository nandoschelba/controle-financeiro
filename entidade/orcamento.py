class Orcamento:
    ultimo_codigo = 0
    def __init__(self, mes: int, ano: int, usuario: int, metas: []):
        Orcamento.ultimo_codigo += 1
        self.__codigo = Orcamento.ultimo_codigo
        self.__mes = mes
        self.__ano = ano
        self.__usuario = usuario
        self.__metas = metas

    def codigo(self, codigo: int = None):
        if codigo is not None:
            self.__codigo = codigo
        else:
            return self.__codigo

    def usuario(self, usuario: str = None):
        if usuario is not None:
            self.__usuario = usuario
        else:
            return self.__usuario

    def valor_disponivel(self, valor: float = None):
        total = 0
        for meta in self.__metas:
            total += meta.valor
        return total

    def mes(self, mes: int = None):
        if mes is not None:
            self.__mes = mes
        else:
            return self.__mes

    def ano(self, ano: int = None):
        if ano is not None:
            self.__ano = ano
        else:
            return self.__ano

    def metas(self, metas: [] = None):
        if metas is not None:
            self.__metas = metas
        else:
            return self.__metas