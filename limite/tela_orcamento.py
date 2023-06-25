import PySimpleGUI as sg

class TelaOrcamento:

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def init_opcoes(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('-------- ORCAMENTOS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha a opcao', font=("Helvica", 15))],
            [sg.Radio('Listar orçamentos', "RD1", key='1')],
            [sg.Radio('Adicionar novo orçamento', "RD1", key='2')],
            [sg.Radio('Deletar orçamento', "RD1", key='3')],
            [sg.Radio('Atualizar orçamento', "RD1", key='4')],
            [sg.Radio('Listar metas', "RD1", key='5')],
            [sg.Radio('Adicionar nova meta', "RD1", key='6')],
            [sg.Radio('Deletar meta', "RD1", key='7')],
            [sg.Radio('Atualizar meta', "RD1", key='8')],
            [sg.Radio('Emitir relatorio', "RD1", key='9')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Sistema de registro de gastos').Layout(layout)

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        opcoes_validas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        opcao = 0
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
        if values['6']:
            opcao = 6
        if values['7']:
            opcao = 7
        if values['8']:
            opcao = 8
        if values['9']:
            opcao = 9

        if values['0']:
            opcao = 0

        if int(opcao) not in opcoes_validas:
            self.close()
            return

        self.close()
        return opcao

    def pega_dados_orcaento(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('-------- DADOS GERAIS DO ORCAMENTO ----------', font=("Helvica", 25))],
            [sg.Text('Mes:', size=(15, 1)), sg.InputText('', key='mes')],
            [sg.Text('Ano:', size=(15, 1)), sg.InputText('', key='ano')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de registro de gastos').Layout(layout)

        button, values = self.open()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        elif button == 'Confirmar':
            mes = values['mes']
            ano = values['ano']

            self.close()
            return {"mes": mes, "ano": ano}

    def pega_dados_meta(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('-------- DADOS GERAIS DO ORCAMENTO ----------', font=("Helvica", 25))],
            [sg.Text('Meta(R$):', size=(15, 1)), sg.InputText('', key='meta')],
            [sg.Text('Descrição:', size=(15, 1)), sg.InputText('', key='descricao')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de registro de gastos').Layout(layout)

        button, values = self.open()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        elif button == 'Confirmar':
            meta = values['meta']
            descricao = values['descricao']

            self.close()
            return {"meta": meta, "descricao": descricao}

    def pega_dados_relario(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('-------- DADOS DO RELATÓRIO ----------', font=("Helvica", 25))],
            [sg.Text('Mes:', size=(15, 1)), sg.InputText('', key='mes')],
            [sg.Text('Ano:', size=(15, 1)), sg.InputText('', key='ano')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de registro de gastos').Layout(layout)

        button, values = self.open()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        elif button == 'Confirmar':
            mes = values['mes']
            ano = values['ano']

            self.close()
            return {"mes": mes, "ano": ano}

    def pega_add_novo(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('-------- ADICIONAR MAIS UMA META? ----------', font=("Helvica", 25))],
            [sg.Yes("Sim")],
            [sg.No("Não")],
        ]
        self.__window = sg.Window('Sistema de registro de gastos').Layout(layout)

        button, values = self.open()
        adicionar_meta = False if button == "Sim" else True

        self.close()
        return {"adicionar_meta": adicionar_meta}

    def mostra_orcamento(self, orcamentos):
        sg.ChangeLookAndFeel('Dark')
        string_orcamentos = ""
        for orcamento in orcamentos:
            string_orcamentos = string_orcamentos + "VALOR DISPONÍVEL: " + str(orcamento["valor_disponivel"]) + '\n'
            string_orcamentos = string_orcamentos + "DATA: " + str(orcamento["mes"]) + "/" + str(orcamento["ano"]) + '\n'
            string_orcamentos = string_orcamentos + "METAS: " + '\n\n'
            for meta in orcamento["metas"]:
                string_orcamentos = string_orcamentos + "META: " + str(meta.meta) + '\n'
                string_orcamentos = string_orcamentos + "CATEGORIA: " + meta.categoria.nome + '\n\n'
            string_orcamentos = string_orcamentos + '\n\n'

        sg.Popup('-------- LISTA DE ORÇAMENTOS ----------', string_orcamentos)

    def mostra_meta(self, metas):
        sg.ChangeLookAndFeel('Dark')
        string_metas = ""
        for meta in metas:
            string_metas = string_metas + "META: " + str(meta["meta"]) + '\n'
            string_metas = string_metas + "CATEGORIA: " + meta["categoria"] + '\n\n'
        string_metas = string_metas + '\n\n'

        sg.Popup('-------- LISTA DE METAS ----------', string_metas)

    def mostra_relatorio(self, relatorio_itens):
        sg.ChangeLookAndFeel('Dark')
        string_relatorio = ""
        for item in relatorio_itens:
            string_relatorio = string_relatorio + "DATA: " + str(item["mes"]) + "/" + str(item["ano"]) + '\n'
            string_relatorio = string_relatorio + "CATEGORIA: " + item["categoria"] + '\n'
            string_relatorio = string_relatorio + "META: " + item["meta"] + '\n'
            string_relatorio = string_relatorio + "GASTO: " + item["gasto"] + '\n'

        sg.Popup('-------- RELATÓRIO ----------', string_relatorio)

    def seleciona_orcamento(self, orcamentos):
        sg.ChangeLookAndFeel('Dark')
        orcamentos_lista = []
        for orcamento in orcamentos:
            orcamentos_lista.append(str(orcamento.codigo) + "-" + str(orcamento.mes) + "-" + str(orcamento.ano))

        layout = [[sg.Text('Escolha um orçamento', size=(20, 1), font=("Helvica", 25))],
                  [sg.Combo(orcamentos_lista, default_value=orcamentos_lista[0], key='orcamento')],
                  [sg.Button('Confirmar', font=('Times New Roman', 12)),
                   sg.Button('Cancelar', font=('Times New Roman', 12))]]

        self.__window = sg.Window('Sistema de registro de gastos').Layout(layout)
        button, value = self.open()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        elif button == 'Confirmar':
            self.close()

            codigo = value["orcamento"].split("-")[0]
            return codigo

    def seleciona_meta(self, metas):
        sg.ChangeLookAndFeel('Dark')
        metas_lista = []

        for meta in metas:
            metas_lista.append(str(meta.codigo) + "-" + str(meta.meta) + "-" + str(meta.categoria.nome))

        layout = [[sg.Text('Escolha uma meta', size=(20, 1), font=("Helvica", 25))],
                  [sg.Combo(metas_lista, default_value=metas_lista[0], key='meta')],
                  [sg.Button('Confirmar', font=('Times New Roman', 12)),
                   sg.Button('Cancelar', font=('Times New Roman', 12))]]

        self.__window = sg.Window('Sistema de registro de gastos').Layout(layout)
        button, value = self.open()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        elif button == 'Confirmar':
            self.close()

            codigo = value["meta"].split("-")[0]
            return codigo

    def mostra_mensagem(self, mensagem):
        sg.ChangeLookAndFeel('Dark')
        sg.popup("", mensagem)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostra_error_mensagem(self, mensagem):
        sg.ChangeLookAndFeel('DarkRed1')
        sg.popup("", mensagem)
