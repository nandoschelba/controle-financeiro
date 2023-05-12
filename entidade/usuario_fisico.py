from entidade.usuario import Usuario
from entidade.categoria import Categoria


class UsuarioFisico(Usuario):
    def __init__(self, nome: str, email: str, cpf: str):
        super().__init__(nome, email)
        self.__cpf = cpf

    def identificador(self):
        return self.__cpf
