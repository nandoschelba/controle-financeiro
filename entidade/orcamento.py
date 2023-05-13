class Orcamento:
    ultimo_codigo = 0
    def __init__(self, mes: int, ano: int, usuario: str, metas: []):
        Orcamento.ultimo_codigo += 1
        self.codigo = Orcamento.ultimo_codigo
        self.mes = mes
        self.ano = ano
        self.usuario = usuario
        self.metas = metas

    def codigo(self, codigo: int = None):
        if codigo is not None:
            self.codigo = codigo
        else:
            return self.codigo

    def usuario(self, usuario: str = None):
        if usuario is not None:
            self.usuario = usuario
        else:
            return self.usuario

    def valor_disponivel(self, valor: float = None):
        return 0

    def mes(self, mes: int = None):
        if mes is not None:
            self.mes = mes
        else:
            return self.mes

    def ano(self, ano: int = None):
        if ano is not None:
            self.ano = ano
        else:
            return self.ano