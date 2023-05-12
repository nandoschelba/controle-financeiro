from entidade.usuario import Usuario
from entidade.categoria import Categoria


class UsuarioJuridico(Usuario):
    def __init__(self, nome: str, email: str, cnpj: str):
        super().__init__(nome, email)
        self.__cnpj = cnpj

    def identificador(self):
        return self.__cnpj
