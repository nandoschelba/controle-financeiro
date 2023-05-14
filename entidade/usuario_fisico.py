from entidade.usuario import Usuario


class UsuarioFisico(Usuario):
    def __init__(self, nome: str, email: str, cpf: int):
        super().__init__(nome, email)
        self.__cpf = cpf

    def identificador(self):
        return self.__cpf
