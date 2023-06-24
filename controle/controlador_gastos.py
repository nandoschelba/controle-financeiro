from entidade.gasto import Gasto
from exceptions.categoria_invalida_error import CategoriaInvalidaError
from exceptions.tipo_invalido_error import TipoInvalidoError
from limite.tela_gasto import TelaGasto
from entidade.item import Item
from persistencia.gastos_dao import GastoDAO


class ControladorGastos:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__gastos_dao = GastoDAO()
        self.__tela_gasto = TelaGasto()

    def abre_tela(self):
        lista_opcoes = {1: self.lista_gastos, 2: self.adiciona_gasto, 3: self.deleta_gasto, 4: self.atualiza_gasto,
                        5: self.emite_relatorio, 0: self.retornar}

        while True:
            try:
                lista_opcoes[self.__tela_gasto.tela_opcoes()]()
            except KeyError:
                print("\nOpção inválida. Digite um número válido.")

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def lista_gastos(self):
        usuario_logado = self.__controlador_principal.controlador_usuarios.pega_codigo_usuario_logado()
        #add usuario_logado.codigo
        gastos = []
        for gasto in self.__gastos_dao.get_all():
            if str(usuario_logado) == str(gasto.usuario):
                gastos.append({"codigo": gasto.codigo, "estabelecimento": gasto.estabelecimento, "mes": gasto.mes, "ano": gasto.ano, "itens": gasto.itens})
        self.__tela_gasto.mostra_gasto(gastos)

    def emite_relatorio(self):
        dados = self.__tela_gasto.pega_dados_relatorio()
        gastos = self.pega_gastos_por_usuario(dados["mes"], dados["ano"])

        gastos_selecionados = []
        for gasto in gastos:
            gastos_selecionados.append({"codigo": gasto.codigo, "estabelecimento": gasto.estabelecimento, "mes": gasto.mes,
                               "ano": gasto.ano, "itens": gasto.itens})

        self.mostra_gasto(gastos_selecionados)

    def pega_gastos_por_usuario(self, mes, ano):
        usuario_logado = self.__controlador_principal.controlador_usuarios.pega_codigo_usuario_logado()
        #add usuario_logado.codigo
        gastos = []
        for gasto in self.__gastos_dao.get_all():
            if str(usuario_logado) == str(gasto.usuario) and str(gasto.mes) == str(mes) and str(gasto.ano) == str(ano):
                gastos.append(gasto)

        return gastos

    def pega_gasto_por_codigo(self, codigo):
        for gasto in self.__gastos_dao.get_all():
            if str(gasto.codigo) == str(codigo):
                return gasto
        return None

    def pega_item_por_codigo(self, codigo, gasto):
        for item in gasto.itens:
            if str(item.codigo) == str(codigo):
                return item
        return None

    def mostra_gasto(self, gastos):
        self.__tela_gasto.mostra_gasto(gastos)
    def adiciona_gasto(self):
        dados_gasto = self.__tela_gasto.pega_dados_gasto()
        itens = []

        while True:
            try:
                itens.append(self.add_item())
            except CategoriaInvalidaError as e:
                print(e)
                return
            except TipoInvalidoError as e:
                print(e)
                return
            self.__tela_gasto.mostra_mensagem("Item adicionado com sucesso")
            dado_add_novo = self.__tela_gasto.pega_add_novo()
            if dado_add_novo["adicionar_item"]:
                break
        usuario_logado = self.__controlador_principal.controlador_usuarios.pega_codigo_usuario_logado()
        # add usuario_logado como obj
        self.__gastos_dao.add(Gasto(usuario_logado, dados_gasto["estabelecimento"], dados_gasto["mes"],
                                   dados_gasto["ano"], itens))
        self.__tela_gasto.mostra_mensagem("Gasto registrado com sucesso")

    def deleta_gasto(self):
        self.lista_gastos()
        gastos_nomes = self.gastos_list()
        codigo_gasto = self.__tela_gasto.seleciona_gasto(gastos_nomes)
        gasto = self.pega_gasto_por_codigo(codigo_gasto)
        if (gasto is not None):
            self.__gastos_dao.remove(gasto.codigo)
            self.lista_gastos()
        else:
            self.__tela_gasto.mostra_mensagem("ATENCAO: Gasto não existente")

    def gastos_list(self):
        usuario_logado = self.__controlador_principal.controlador_usuarios.pega_codigo_usuario_logado()
        gastos = []
        for gasto in self.__gastos_dao.get_all():
            if str(usuario_logado) == str(gasto.usuario):
                gastos.append(str(gasto.codigo) + "-" + str(gasto.mes) + "-" + str(gasto.ano))
        return gastos

    def add_item(self):
        dados_item = self.__tela_gasto.pega_dados_item()
        if self.isfloat(dados_item["valor"]):
            self.__controlador_principal.controlador_categorias.listar_categorias()
            codigo_categoria = self.__controlador_principal.controlador_categorias.seleciona_categoria()
            categoria = self.__controlador_principal.controlador_categorias.buscar_categoria_por_codigo(
                codigo_categoria)
            if categoria is not None:
                return Item(float(dados_item["valor"]), dados_item["descricao"], categoria)
            else:
                raise CategoriaInvalidaError
        else:
            raise TipoInvalidoError


    def atualiza_gasto(self):
        self.lista_gastos()
        gastos_nomes = self.gastos_list()
        codigo_gasto = self.__tela_gasto.seleciona_gasto(gastos_nomes)
        gasto = self.pega_gasto_por_codigo(codigo_gasto)

        if gasto is not None:
            dados_gasto = self.__tela_gasto.pega_dados_gasto()
            itens = []

            while True:
                try:
                    itens.append(self.add_item())
                except CategoriaInvalidaError as e:
                    print(e)
                    return
                except TipoInvalidoError as e:
                    print(e)
                    return
                self.__tela_gasto.mostra_mensagem("Item adicionado com sucesso")
                dado_add_novo = self.__tela_gasto.pega_add_novo()
                if dado_add_novo["adicionar_item"] != "s":
                    break

            gasto.estabelecimento = dados_gasto["estabelecimento"]
            gasto.mes = dados_gasto["mes"]
            gasto.ano = dados_gasto["ano"]
            gasto.itens = itens
        else:
            self.__tela_gasto.mostra_mensagem("ATENCAO: Gasto não existente")

    def deleta_item(self):
        self.lista_gastos()
        gastos_nomes = self.gastos_list()
        codigo_gasto = self.__tela_gasto.seleciona_gasto(gastos_nomes)
        gasto = self.pega_gasto_por_codigo(codigo_gasto)

        itens = []
        for item in gasto.itens:
            itens.append({"codigo": item.codigo, "descricao": item.descricao, "categoria": item.categoria.nome})

        codigo_item = self.__tela_gasto.seleciona_item(itens)
        item = self.pega_item_por_codigo(codigo_item, gasto)
        if item is not None:
            gasto.itens.remove(item)
        else:
            self.__tela_gasto.mostra_mensagem("ATENCAO: Item não existente")

    #def update_item

    def isfloat(self, input):
        try:
            float(input)
            return True
        except ValueError:
            return False
