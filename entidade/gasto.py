class Gasto:
    def __init__(self, codigo, estabelecimento, mes, ano, desconto=0, itens=[]):
        self.codigo = codigo
        self.estabelecimento = estabelecimento
        self.mes = mes
        self.ano = ano
        self.desconto = desconto
        self.itens = itens

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

    def desconto(self, desconto=None):
        if desconto is not None:
            self.desconto = desconto
        else:
            return self.desconto

    def itens(self, itens=None):
        if itens is not None:
            self.itens = itens
        else:
            return self.itens