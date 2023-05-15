
class CategoriaInvalidaError(Exception):
    def __init__(self):
        self.mensagem = "Essa categoria não existe! Adicione para poder proceguir"
        super().__init__(self.mensagem)