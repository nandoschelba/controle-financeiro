from entidade.usuario import Usuario


class Orcamento:
    ultimo_codigo = 0

    def __init__(self, mes: int, ano: int, usuario: Usuario, metas: []):
        Orcamento.ultimo_codigo += 1
        self.__codigo = Orcamento.ultimo_codigo
        self.__mes = mes
        self.__ano = ano
        self.__usuario = usuario
        self.__metas = metas

    def valor_disponivel(self):
        total = 0
        for meta in self.__metas:
            total += float(meta.meta)
        return total

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, value):
        self.__codigo = value

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, value):
        self.__mes = value

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, value):
        self.__ano = value

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, value):
        self.__usuario = value

    @property
    def metas(self):
        return self.__metas

    @metas.setter
    def metas(self, value):
        self.__metas = value
