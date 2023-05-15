from entidade.gasto import Gasto
from exceptions.categoria_invalida_error import CategoriaInvalidaError
from limite.tela_gasto import TelaGasto
from entidade.item import Item


class ControladorGastos:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__gastos = []
        self.__tela_gasto = TelaGasto()

    def abre_tela(self):
        lista_opcoes = {1: self.lista_gastos, 2: self.adiciona_gasto, 3: self.deleta_gasto, 4: self.atualiza_gasto,
                        5: self.emite_relatorio, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_gasto.tela_opcoes()]()

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def lista_gastos(self):
        usuario_logado = self.__controlador_principal.controlador_usuarios.pega_codigo_usuario_logado()
        for gasto in self.__gastos:
            if str(usuario_logado) == str(gasto.usuario):
                self.mostra_gasto(gasto)

    def emite_relatorio(self):
        dados = self.__tela_gasto.pega_dados_relatorio()
        gastos = self.pega_gastos_por_usuario(dados["mes"], dados["ano"])

        for gasto in gastos:
            self.mostra_gasto(gasto)

    def pega_gastos_por_usuario(self, mes, ano):
        usuario_logado = self.__controlador_principal.controlador_usuarios.pega_codigo_usuario_logado()
        gastos = []
        for gasto in self.__gastos:
            if str(usuario_logado) == str(gasto.usuario) and str(gasto.mes) == str(mes) and str(gasto.ano) == str(ano):
                gastos.append(gasto)

        return gastos

    def pega_gasto_por_codigo(self, codigo):
        for gasto in self.__gastos:
            if str(gasto.codigo) == str(codigo):
                return gasto
        return None

    def pega_item_por_codigo(self, codigo, gasto):
        for item in gasto.itens:
            if str(item.codigo) == str(codigo):
                return item
        return None

    def mostra_gasto(self, gasto):
        self.__tela_gasto.mostra_gasto({"codigo": gasto.codigo, "estabelecimento": gasto.estabelecimento,
             "mes": gasto.mes, "ano": gasto.ano})
        for item in gasto.itens:
            self.__tela_gasto.mostra_item({"valor": item.valor, "descricao": item.descricao})

    def adiciona_gasto(self):
        dados_gasto = self.__tela_gasto.pega_dados_gasto()
        itens = []

        while True:
            try:
                itens.append(self.add_item())
            except CategoriaInvalidaError as e:
                print(e)
                return
            self.__tela_gasto.mostra_mensagem("Item adicionado com sucesso")
            dado_add_novo = self.__tela_gasto.pega_add_novo()
            if dado_add_novo["adicionar_item"] != "s":
                break
        usuario_logado = self.__controlador_principal.controlador_usuarios.pega_codigo_usuario_logado()
        self.__gastos.append(Gasto(usuario_logado, dados_gasto["estabelecimento"], dados_gasto["mes"], dados_gasto["ano"], itens))
        self.__tela_gasto.mostra_mensagem("Gasto registrado com sucesso")

    def deleta_gasto(self):
        self.lista_gastos()
        codigo_gasto = self.__tela_gasto.seleciona_gasto()
        gasto = self.pega_gasto_por_codigo(codigo_gasto)

        if (gasto is not None):
            self.__gastos.remove(gasto)
            self.lista_gastos()
        else:
            self.__tela_gasto.mostra_mensagem("ATENCAO: Gasto não existente")

    def add_item(self):
        dados_item = self.__tela_gasto.pega_dados_item()

        self.__controlador_principal.controlador_categorias.listar_categorias()
        codigo_categoria = self.__controlador_principal.controlador_categorias.seleciona_categoria()
        categoria = self.__controlador_principal.controlador_categorias.buscar_categoria_por_codigo(codigo_categoria)

        if categoria is not None:
            return Item(dados_item["valor"], dados_item["descricao"], categoria)
        else:
           raise CategoriaInvalidaError

    def atualiza_gasto(self):
        self.lista_gastos()
        codigo_gasto = self.__tela_gasto.seleciona_gasto()
        gasto = self.pega_gasto_por_codigo(codigo_gasto)

        if (gasto is not None):
            dados_gasto = self.__tela_gasto.pega_dados_gasto()
            gasto.estabelecimento = dados_gasto["estabelecimento"]
            gasto.mes = dados_gasto["mes"]
            gasto.ano = dados_gasto["ano"]
        else:
            self.__tela_gasto.mostra_mensagem("ATENCAO: Gasto não existente")

    def deleta_item(self):
        self.lista_gastos()
        codigo_gasto = self.__tela_gasto.seleciona_gasto()
        gasto = self.pega_gasto_por_codigo(codigo_gasto)
        self.mostra_gasto(gasto)

        codigo_item = self.__tela_gasto.seleciona_item()
        item = self.pega_item_por_codigo(codigo_item, gasto)
        if (item is not None):
            self.gasto.itens.remove(item)
        else:
            self.__tela_gasto.mostra_mensagem("ATENCAO: Item não existente")
