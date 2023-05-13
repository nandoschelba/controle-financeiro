class Meta:
    ultimo_codigo = 0
    def __init__(self, meta: float, descricao: str, categoria: str):
        Meta.ultimo_codigo += 1
        self.codigo = Meta.ultimo_codigo
        self.meta = meta
        self.descricao = descricao
        self.categoria = categoria

    def codigo(self, codigo: int = None):
        if codigo is not None:
            self.codigo = codigo
        else:
            return self.codigo

    def categoria(self, categoria: str = None):
        if categoria is not None:
            self.categoria = categoria
        else:
            return self.categoria

    def meta(self, meta: float = None):
        if meta is not None:
            self.meta = meta
        else:
            return self.meta