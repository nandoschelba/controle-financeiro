import PySimpleGUI as sg

class TelaUsuario:
    def __init__(self):
        self.__window = None

    def loga_usuario(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('-------- Login ----------', font=("Helvica", 25))],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('CPF/CNPJ:', size=(15, 1)), sg.InputText('', key='identificador')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Login').Layout(layout)

        button, values = self.open()
        email = values['email']
        identificador = values['identificador']

        if button in (None, 'Cancelar'):
            self.__window.close()
            return None
        elif button == 'Confirmar':

            if not email.strip():
                return self.mostra_mensagem("Email não pode estar vazio.")
            try:
                identificador = int(identificador)
            except ValueError:
                return self.mostra_mensagem("CPF/CNPJ deve ser um número inteiro.")

            self.close()
            return {"email": email, "id": identificador}

    def tela_opcoes(self):
        self.init_opcoes_usuario()
        button, values = self.__window.Read()
        opcao = 0
        if values.get('1'):
            opcao = 1
        if values.get('2'):
            opcao = 2
        if values.get('0') or button in (None, 'Voltar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes_usuario(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('-------- Configurações de usuário ----------', font=("Helvica", 25))],
            [sg.Radio('Editar cadastro', "RD1", default=True, key='1')],
            [sg.Radio('Encerrar conta', "RD1", key='2')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

    def pega_dados_usuario(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('-------- Cadastro ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Radio('Pessoa Física', "RD1", default=True, key='pessoa_fisica')],
            [sg.Radio('Pessoa Jurídica', "RD1", key='pessoa_juridica')],
            [sg.Text('CPF/CNPJ:', size=(15, 1)), sg.InputText('', key='identificador')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Login').Layout(layout)

        button, values = self.open()
        email = values['email']
        nome = values['nome']
        identificador = values['identificador']
        pessoa_fisica = values['pessoa_fisica']
        pessoa_juridica = values['pessoa_juridica']

        if button in (None, 'Cancelar'):
            self.__window.close()
            return None
        elif button == 'Confirmar':
            if not nome.strip():
                self.mostra_mensagem("Nome não pode estar vazio.")
                return self.close()
            if not email.strip():
                self.mostra_mensagem("Email não pode estar vazio.")
                return self.close()
            if pessoa_fisica:
                if not identificador.isdigit():
                    self.mostra_mensagem("CPF deve ser um número inteiro.")
                    return self.close()
                if len(identificador) != 11:
                    self.mostra_mensagem("Um CPF válido deve ter 11 digitos.")
                    return self.close()
                novo_usuario = {"nome": nome, "email": email, "cpf": int(identificador)}
                self.close()
                return novo_usuario
            if pessoa_juridica:
                if not identificador.isdigit():
                    self.mostra_mensagem("CNPJ deve ser um número inteiro.")
                    return self.close()
                if len(identificador) != 14:
                    self.mostra_mensagem("Um CNPJ válido deve ter 14 digitos.")
                    return self.close()
                novo_usuario = {"nome": nome, "email": email, "cnpj": int(identificador)}
                self.close()
                return novo_usuario

    def pega_dados_usuario_edicao(self, nome: str, email: str):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('-------- Editar usuário ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText(nome, key='nome')],
            [sg.Text('email:', size=(15, 1)), sg.InputText(email, key='email')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Edição usuario').Layout(layout)

        button, values = self.open()
        email = values['email']
        nome = values['nome']

        if button in (None, 'Cancelar'):
            self.close()
            return None
        elif button == 'Confirmar':
            if not nome.strip():
                self.mostra_mensagem("Nome não pode estar vazio.")
                return self.close()
            if not email.strip():
                self.mostra_mensagem("Email não pode estar vazio.")
                return self.close()
            self.close()
            return {"nome": nome, "email": email}

    def confirmar_deletar_conta(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('Tem certeza que deseja excluir sua conta? Esta ação é irreversível.', font=("Helvica", 25))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Deletar conta').Layout(layout)


        button, values = self.__window.Read()

        if button in (None, 'Cancelar'):
            self.close()
            return 0
        elif button == 'Confirmar':
            self.close()
            return 1

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values