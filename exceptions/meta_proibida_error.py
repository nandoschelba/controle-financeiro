class MetaProibidaError(Exception):
    def __init__(self):
        self.mensagem = "Uma meta com essa categoria já foi adicionada nesse orçamento"
        super().__init__(self.mensagem)