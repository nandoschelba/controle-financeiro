from usuario import Usuario


class UsuarioFisico(Usuario):
    def __init__(self, nome: str, email: str, cpf: str, categorias: list):
        super().__init__(nome, email, categorias)
        self.__cpf = cpf

    def identificador(self):
        return self.__cpf
