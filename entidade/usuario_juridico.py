from usuario import Usuario


class UsuarioJuridico(Usuario):
    def __init__(self, nome: str, email: str, cnpj: str, categorias: list):
        super().__init__(nome, email, categorias)
        self.__cnpj = cnpj

    def identificador(self):
        return self.__cnpj
