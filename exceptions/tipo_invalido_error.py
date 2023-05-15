class TipoInvalidoError(Exception):

    def __init__(self):
        self.mensagem = "Tipo inválido, por favor digite um número"
        super().__init__(self.mensagem)
