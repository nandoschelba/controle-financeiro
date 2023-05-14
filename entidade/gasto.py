class Gasto:
    ultimo_codigo = 0
    def __init__(self, usuario: int, estabelecimento: str, mes: int, ano: int, itens=[]):
        Gasto.ultimo_codigo += 1
        self.codigo = Gasto.ultimo_codigo
        self.__usuario = usuario
        self.estabelecimento = estabelecimento
        self.mes = mes
        self.ano = ano
        self.itens = itens


    def usuario(self, usuario=None):
        if usuario is not None:
            self.__usuario = usuario
        else:
            return self.__usuario

    def codigo(self, codigo=None):
        if codigo is not None:
            self.codigo = codigo
        else:
            return self.codigo

    def estabelecimento(self, local=None):
        if local is not None:
            self.estabelecimento = local
        else:
            return self.estabelecimento

    def mes(self, mes=None):
        if mes is not None:
            self.mes = mes
        else:
            return self.mes

    def ano(self, ano=None):
        if ano is not None:
            self.ano = ano
        else:
            return self.ano

    def itens(self, itens=None):
        if itens is not None:
            self.itens = itens
        else:
            return self.itens