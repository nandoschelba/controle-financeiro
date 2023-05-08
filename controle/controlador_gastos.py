from entidade.gasto import Gasto
from limite.tela_gasto import TelaGasto
from entidade.item import Item


class ControladorGastos:
    def __init__(self, controlador_principal):
        self.controlador_principal = controlador_principal
        self.gastos = []
        self.__tela_gasto = TelaGasto()

    def abre_tela(self):
        lista_opcoes = {1: self.lista_gastos, 2: self.adiciona_gasto, 3: self.deleta_gasto, 4: self.atualiza_gasto,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_gasto.tela_opcoes()]()

    # code to open the GUI for the expense manager

    def retornar(self):
        print("retornar")
        ...

    # code to return to the main menu

    def lista_gastos(self):
        #precisa de usuario
        print("lista_gastos")
        ...

    # code to display a list of expenses for the given user

    def pega_gasto_por_codigo(self, codigo):
        print("pega_gasto_por_codigo")
        ...

    # code to retrieve an expense by its code

    def adiciona_gasto(self):
        print("adiciona_gasto")
        dados_gasto = self.__tela_gasto.pega_dados_gasto()
        print(dados_gasto)
        itens = []
        add_itens = True
        while add_itens:
            dados_item = self.__tela_gasto.pega_dados_item()
            print(dados_item)
            itens.append(Item(1, dados_item["valor"], dados_item["descricao"]))
            self.__tela_gasto.mostra_mensagem("Item adicionado com sucesso")
            add_itens = False if self.__tela_gasto.pega_add_novo() == 1 else True
        self.gastos.append(Gasto(1, dados_gasto["estabelecimento"], dados_gasto["mes"], dados_gasto["ano"], dados_gasto["desconto"], itens))

    # code to add a new expense

    def deleta_gasto(self):
        print("deleta_gasto")
        ...

    # code to delete an expense

    def add_item(self, gasto, valor, descricao, categoria):
        print("add_item")
        ...

    # code to add a new item to an expense

    def atualiza_gasto(self):
        #precisa de codigo
        print("atualiza_gasto")
        ...

    # code to update an existing expense

    def deleta_item(self):
        # precisa de codigo
        print("deleta_item")
        ...
    # code to delete an item from an expense