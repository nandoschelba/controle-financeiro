
class MetaInvalidaError(Exception):
    def __init__(self):
        self.mensagem = "Essa meta não existe! Adicione para poder proceguir"
        super().__init__(self.mensagem)