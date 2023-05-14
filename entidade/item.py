class Item:
    ultimo_codigo = 0
    def __init__(self, valor, descricao, categoria=None):
        Item.ultimo_codigo += 1
        self.codigo = Item.ultimo_codigo
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