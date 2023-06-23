import PySimpleGUI as sg


class TelaCategoria:
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('-------- Categorias ----------', font=("Helvica", 25))],
            [sg.Radio('Adicionar categoria', "RD1", default=True, key='1')],
            [sg.Radio('Listar categoria', "RD1", key='2')],
            [sg.Radio('Editar categoria', "RD1", key='3')],
            [sg.Radio('Excluir categoria', "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Categorias').Layout(layout)

        button, values = self.__window.Read()
        opcao = 0
        if values.get('1'):
            opcao = 1
        if values.get('2'):
            opcao = 2
        if values.get('3'):
            opcao = 3
        if values.get('4'):
            opcao = 4
        if values.get('0') or button in (None, 'Voltar'):
            opcao = 0
        self.close()
        return opcao

    def pega_dados_categoria(self):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text('-------- Nova categoria ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Descrição:', size=(15, 1)), sg.InputText('', key='descricao')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Nova categoria').Layout(layout)

        button, values = self.open()
        descricao = values['descricao']
        nome = values['nome']

        if button in (None, 'Cancelar'):
            self.close()
            return None
        elif button == 'Confirmar':
            if not nome.strip():
                self.mostra_mensagem("Nome não pode estar vazio.")
                return self.close()
            if not descricao.strip():
                self.mostra_mensagem("A descrição não pode estar vazia.")
                return self.close()
            self.close()
            return {"nome": nome, "descricao": descricao}

    def mostra_categoria(self, dados_categoria):
        print("\n----------------------")
        print("Código:", dados_categoria["codigo"])
        print("Nome:", dados_categoria["nome"])
        print("Descrição:", dados_categoria["descricao"])

    def pega_codigo_categoria(self, mensagem_input: str):
        codigo = input("\n" + mensagem_input)
        if not codigo.isdigit():
            print("\nO código deve ser um número inteiro")
            return
        return int(codigo)

    def pega_novos_dados_categoria(self, categoria_selecionada):
        print("\n------ Categoria selecionada ------")
        print("Código:", categoria_selecionada.codigo)
        print("Nome:", categoria_selecionada.nome)
        print("Descrição:", categoria_selecionada.descricao)
        while True:
            nome = input("\nNovo nome da categoria: ")
            if not nome.strip():
                return print("\nNome não pode estar vazio.")
            descricao = input("Nova descricao: ")
            if not descricao.strip():
                return print("\nDescrição não pode estar vazio.")
            else:
                return {"nome": nome, "descricao": descricao, "codigo": categoria_selecionada.codigo}

    def confirmar_deletar_categoria(self):
        opcoes_validas = [0, 1]
        print("\n------ Tem certeza que deseja excluir a categoria? Esta ação é irreversível. ------")
        print("1 - Sim")
        print("0 - Voltar")
        opcao = input("Escolha a opção desejada: ")
        if not opcao.isdigit():
            return
        if int(opcao) not in opcoes_validas:
            return
        return int(opcao)

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values