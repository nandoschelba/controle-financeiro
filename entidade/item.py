class Item:
    def __init__(self, codigo, valor, descricao, categoria=None):
        self.codigo = codigo
        self.valor = valor
        self.descricao = descricao
        self.categoria = categoria

    def codigo(self, codigo=None):
        if codigo is not None:
            self.codigo = codigo
        else:
            return self.codigo

    def valor(self, valor=None):
        if valor is not None:
            self.valor = valor
        else:
            return self.valor

    def descricao(self, descricao=None):
        if descricao is not None:
            self.descricao = descricao
        else:
            return self.descricao

    def categoria(self, categoria=None):
        if categoria is not None:
            self.categoria = categoria
        else:
            return self.categoria