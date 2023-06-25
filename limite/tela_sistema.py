import PySimpleGUI as sg


class TelaSistema:
    def __init__(self):
        self.__window = None

    def tela_opcoes_usuario_deslogado(self):
        self.inicia_componentes_deslogado()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def inicia_componentes_deslogado(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Bem vindo ao sistema de gestão de gastos!', font=("Helvica", 25))],
            [sg.Radio('Login', "RD1", default=True, key='1')],
            [sg.Radio('Realizar cadastro', "RD1", key='2')],
            [sg.Radio('Finalizar sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Gestão de gastos').Layout(layout)

    def tela_opcoes_usuario_logado(self, nome_usuario):
        self.inicia_componentes_logado(nome_usuario)
        button, values = self.__window.Read()
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
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def inicia_componentes_logado(self, nome_usuario):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text(f'Bem vindo a gestão de gastos, {nome_usuario}!', font=("Helvica", 25))],
            [sg.Radio('Configurações de usuário', "RD1", default=True, key='1')],
            [sg.Radio('Categorias', "RD1", key='2')],
            [sg.Radio('Orçamentos', "RD1", key='3')],
            [sg.Radio('Gastos', "RD1", key='4')],
            [sg.Radio('Logout', "RD1", key='5')],
            [sg.Radio('Finalizar sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Bem vindo!').Layout(layout)
