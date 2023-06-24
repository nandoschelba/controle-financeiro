from entidade.usuario import Usuario


class Gasto:
    ultimo_codigo = 0
    def __init__(self, usuario: Usuario, estabelecimento: str, mes: int, ano: int, itens=[]):
        Gasto.ultimo_codigo += 1
        self.__codigo = Gasto.ultimo_codigo
        self.__usuario = usuario
        self.__estabelecimento = estabelecimento
        self.__mes = mes
        self.__ano = ano
        self.__itens = itens

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, value):
        self.__codigo = value

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, value):
        self.__usuario = value

    @property
    def estabelecimento(self):
        return self.__estabelecimento

    @estabelecimento.setter
    def estabelecimento(self, value):
        self.__estabelecimento = value

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
    def itens(self):
        return self.__itens

    @itens.setter
    def itens(self, value):
        self.__itens = value