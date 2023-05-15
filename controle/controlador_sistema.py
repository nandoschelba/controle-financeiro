from limite.tela_sistema import TelaSistema
from controle.controlador_usuarios import ControladorUsuarios
from controle.controlador_categoria import ControladorCategoria
from controle.controlador_orcamentos import ControladorOrcamentos
from controle.controlador_gastos import ControladorGastos


class ControladorSistema:

    def __init__(self):
        self.__controlador_usuarios = ControladorUsuarios(self)
        self.__controlador_categorias = ControladorCategoria(self)
        self.__controlador_orcamentos = ControladorOrcamentos(self)
        self.__controlador_gastos = ControladorGastos(self)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        lista_opcoes_usuario_logado = {1: self.tela_usuarios, 2: self.tela_categorias, 3: self.cadastra_orcamento,
                                       4: self.cadastra_gastos, 5: self.logout, 0: self.encerra_sistema}

        lista_opcoes_usuario_deslogado = {1: self.login, 2: self.cadastra_usuarios, 0: self.encerra_sistema}

        while True:
            if self.__controlador_usuarios.usuario_logado:
                opcao_escolhida = self.__tela_sistema.tela_opcoes_usuario_logado()
                try:
                    funcao_escolhida = lista_opcoes_usuario_logado[opcao_escolhida]
                except KeyError:
                    self.__tela_sistema.mostra_mensagem("\nOpção inválida. Tente novamente.")
                    continue
                funcao_escolhida()
            else:
                opcao_escolhida = self.__tela_sistema.tela_opcoes_usuario_deslogado()
                try:
                    funcao_escolhida = lista_opcoes_usuario_deslogado[opcao_escolhida]
                except KeyError:
                    self.__tela_sistema.mostra_mensagem("\nOpção inválida. Tente novamente.")
                    continue
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

    @property
    def controlador_categorias(self):
        return self.__controlador_categorias

    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios

    @property
    def controlador_orcamentos(self):
        return self.__controlador_orcamentos

    def cadastra_orcamento(self):
        self.__controlador_orcamentos.abre_tela()

    @property
    def controlador_gastos(self):
        return self.__controlador_gastos

    def cadastra_gastos(self):
        self.__controlador_gastos.abre_tela()

    def encerra_sistema(self):
        exit(0)
