import PySimpleGUI as sg

class TelaGasto:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def init_opcoes(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- GASTOS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha a opcao', font=("Helvica", 15))],
            [sg.Radio('Listar Gastos', "RD1", key='1')],
            [sg.Radio('Adicionar novo gasto', "RD1", key='2')],
            [sg.Radio('Deletar gasto', "RD1", key='3')],
            [sg.Radio('Atualizar gasto', "RD1", key='4')],
            [sg.Radio('Emite relatorio', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de registro de gastos').Layout(layout)

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        opcoes_validas = [0, 1, 2, 3, 4, 5]
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5

        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0

        if int(opcao) not in opcoes_validas:
            return

        self.close()
        return opcao

    def pega_dados_gasto(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS GERAIS DO GASTO ----------', font=("Helvica", 25))],
            [sg.Text('Estabelecimento:', size=(15, 1)), sg.InputText('', key='estabelecimento')],
            [sg.Text('Mes:', size=(15, 1)), sg.InputText('', key='mes')],
            [sg.Text('Ano:', size=(15, 1)), sg.InputText('', key='ano')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de registro de gastos').Layout(layout)

        button, values = self.open()
        estabelecimento = values['estabelecimento']
        mes = values['mes']
        ano = values['ano']

        self.close()
        return {"estabelecimento": estabelecimento, "mes": mes, "ano": ano}

    def pega_dados_item(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS DO ITEM ----------', font=("Helvica", 25))],
            [sg.Text('Valor:', size=(15, 1)), sg.InputText('', key='valor')],
            [sg.Text('Descricao:', size=(15, 1)), sg.InputText('', key='descricao')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de registro de gastos').Layout(layout)

        button, values = self.open()
        valor = values['valor']
        descricao = values['descricao']

        self.close()
        return {"valor": valor, "descricao": descricao}

    def pega_dados_relatorio(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS DO RELATÓRIO ----------', font=("Helvica", 25))],
            [sg.Text('Mes:', size=(15, 1)), sg.InputText('', key='mes')],
            [sg.Text('Ano:', size=(15, 1)), sg.InputText('', key='ano')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de registro de gastos').Layout(layout)

        button, values = self.open()
        mes = values['mes']
        ano = values['ano']

        self.close()
        return {"mes": mes, "ano": ano}

    def pega_add_novo(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- ADICIONAR MAIS UM ITEM? ----------', font=("Helvica", 25))],
            [sg.Yes()],
            [sg.No()],
        ]
        self.__window = sg.Window('Sistema de registro de gastos').Layout(layout)

        button, values = self.open()
        print(button)
        adicionar_item = False if button == "Yes" else False

        self.close()
        return {"adicionar_item": adicionar_item}

    def mostra_gasto(self, gastos):
        string_todos_gasto = ""
        for gasto in gastos:
            string_todos_gasto = string_todos_gasto + "CÓDIGO DO GASTO: " + str(gasto["codigo"]) + '\n'
            string_todos_gasto = string_todos_gasto + "NOME DO ESTABELECIMENTO: " + gasto["estabelecimento"] + '\n'
            string_todos_gasto = string_todos_gasto + "DATA: " + str(gasto["mes"]) + "/" + str(gasto["ano"]) + '\n\n'
            string_todos_gasto = string_todos_gasto + "ITENS: " + '\n'
            for item in gasto["itens"]:
                string_todos_gasto = string_todos_gasto + "DESCRICAO: " + item.descricao + '\n'
                string_todos_gasto = string_todos_gasto + "VALOR: " + str(item.valor) + '\n\n'
            string_todos_gasto = string_todos_gasto + '\n\n'

        sg.Popup('-------- LISTA DE GASTOS ----------', string_todos_gasto)

    def seleciona_gasto(self, gastos):
        layout = [[sg.Text('Escolha um gasto', size=(20, 1), font=("Helvica", 25))],
                  [sg.Combo(gastos, default_value=gastos[0], key='gasto')],
                  [sg.Button('Confirmar', font=('Times New Roman', 12)),
                   sg.Button('Cancelar', font=('Times New Roman', 12))]]

        self.__window = sg.Window('Sistema de registro de gastos').Layout(layout)
        button, value = self.open()
        self.close()

        codigo = value["gasto"].split("-")[0]
        return codigo

    def seleciona_item(self, itens):
        itens_lista = []
        for item in itens:
            itens_lista.append(str(item.codigo) + "-" + str(item.descricao) + "-" + str(item.categoria))

        layout = [[sg.Text('Escolha um item', size=(20, 1), font=("Helvica", 25))],
                  [sg.Combo(itens_lista, default_value=itens[0], key='item')],
                  [sg.Button('Confirmar', font=('Times New Roman', 12)),
                   sg.Button('Cancelar', font=('Times New Roman', 12))]]

        self.__window = sg.Window('Sistema de registro de gastos').Layout(layout)
        button, value = self.open()
        self.close()

        codigo = value["item"].split("-")[0]
        return codigo

    def mostra_mensagem(self, mensagem):
        sg.popup("", mensagem)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values