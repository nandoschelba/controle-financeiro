from entidade.usuario import Usuario
from entidade.categoria import Categoria


class UsuarioFisico(Usuario):
    def __init__(self, nome: str, email: str, cpf: int):
        super().__init__(nome, email)
        self.__cpf = cpf
        self.__logado = False

    def identificador(self):
        return self.__cpf
