from entidade.usuario import Usuario


class UsuarioJuridico(Usuario):
    def __init__(self, nome: str, email: str, cnpj: int):
        super().__init__(nome, email)
        self.__cnpj = cnpj

    def identificador(self):
        return self.__cnpj
