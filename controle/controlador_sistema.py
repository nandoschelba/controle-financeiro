from controle.controlador_gastos import ControladorGastos
from controle.controlador_orcamentos import ControladorOrcamentos
from limite.tela_sistema import TelaSistema
from controle.controlador_usuarios import ControladorUsuarios
from controle.controlador_categoria import ControladorCategoria


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
        lista_opcoes = {1: self.cadastra_usuarios,
                        2: self.cadastra_categorias,
                        3: self.cadastra_orcamento,
                        4: self.cadastra_gastos,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastra_usuarios(self):
        self.__controlador_usuarios.abre_tela()

    def cadastra_categorias(self):
        self.__controlador_categorias.abre_tela()
    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios

    #@property
    #def controlador_categorias(self):
    #   return self.__controlador_categorias

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

