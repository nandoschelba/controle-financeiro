from entidade.usuario_juridico import UsuarioJuridico
from entidade.usuario_fisico import UsuarioFisico


class ControladorUsuarios:
    def __init__(self, controlador_sistema):
        from limite.tela_usuario import TelaUsuario
        self.__usuarios = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_usuario = TelaUsuario(self)

    def pega_tipo_usuario(self):
        self.__tela_usuario.pega_dados_usuario()
    def adiciona_usuario_juridico(self, nome, email, cnpj):
        usuario_juridico = UsuarioJuridico(nome, email, cnpj)
        self.__usuarios.append(usuario_juridico)

    def deleta_usuario_juridico(self, usuario_juridico: UsuarioJuridico):
        pass

    def edita_usuario_juridico(self, usuario_juridico: UsuarioJuridico):
        pass

    def adiciona_usuario_fisico(self, nome, email, cpf):
        usuario_fisico = UsuarioFisico(nome, email, cpf)
        self.__usuarios.append(usuario_fisico)
        print(self.__usuarios)

    def deleta_usuario_fisico(self, usuario_fisico: UsuarioFisico):
        pass

    def edita_usuario_fisico(self, usuario_fisico: UsuarioFisico):
        pass

    def vincular_categoria(self):
        pass

    def listar_usuarios(self):
        for usuario in self.__usuarios:
            self.__tela_usuario.mostra_usuario({"nome": usuario.nome, "email": usuario.email})

    def abre_tela(self):
        lista_opcoes = {1: self.pega_tipo_usuario, 2: self.listar_usuarios, 3: self.vincular_categoria,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_usuario.tela_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def login(self, email: str):
        pass

    def pega_codigo_usuario_logado(self):
        return 1

