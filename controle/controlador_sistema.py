from limite.tela_sistema import TelaSistema
from controle.controlador_usuarios import ControladorUsuarios
from controle.controlador_categoria import ControladorCategoria


class ControladorSistema:

    def __init__(self):
        self.__controlador_usuarios = ControladorUsuarios(self)
        self.__controlador_categorias = ControladorCategoria(self, self.__controlador_usuarios)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.login,
                        2: self.cadastra_usuarios,
                        3: self.tela_usuarios,
                        4: self.tela_categorias,
                        5: self.logout,
                        0: self.encerra_sistema}

        while True:
            if self.__controlador_usuarios.usuario_logado:
                opcao_escolhida = self.__tela_sistema.tela_opcoes_usuario_logado()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            else:
                opcao_escolhida = self.__tela_sistema.tela_opcoes_usuario_deslogado()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()

    def login(self):
        self.__controlador_usuarios.efetuar_login()

    def cadastra_usuarios(self):
        self.__controlador_usuarios.pega_tipo_usuario()

    def tela_usuarios(self):
        self.__controlador_usuarios.abre_tela_usuario()

    def tela_categorias(self):
        self.__controlador_categorias.abre_tela()

    def logout(self):
        self.__controlador_usuarios.efetuar_logout()

    def encerra_sistema(self):
        exit(0)
