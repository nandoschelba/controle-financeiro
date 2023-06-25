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

    def pega_codigo_categoria(self, categorias):
        sg.ChangeLookAndFeel('Dark')
        layout = [[sg.Listbox(values=[categoria.nome for categoria in categorias],
                              key='listbox',
                              select_mode=sg.LISTBOX_SELECT_MODE_SINGLE,
                              size=(100, 10),
                              enable_events=True)],
                  [sg.Button('Confirmar')]]

        window = sg.Window('Selecionar categoria', layout)

        while True:
            event, values = window.read()

            if event == 'Confirmar':
                selected_item = values['listbox'][0] if values['listbox'] else None
                if selected_item:
                    categoria_selecionada = next(
                        (categoria for categoria in categorias if categoria.nome == selected_item),
                        None)
                    window.close()
                    return categoria_selecionada
                else:
                    self.mostra_mensagem('Selecione pelo menos uma categoria para continuar')

    def editar_categoria(self, categorias):
        sg.ChangeLookAndFeel('Dark')
        col = [[sg.Text('Nome', text_color='white'),
                sg.Input('', key='nome')],
               [sg.Text('Descrição', text_color='white'),
                sg.Input('', key='descricao')]]

        layout = [[sg.Listbox(values=[categoria.nome for categoria in categorias],
                              key='listbox',
                              select_mode=sg.LISTBOX_SELECT_MODE_SINGLE,
                              size=(20, 10),
                              enable_events=True),
                   sg.Column(col)],
                  [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]

        window = sg.Window('Editar Categoria', layout)

        while True:
            event, values = window.read()

            if event in (None, 'Cancelar'):
                window.close()
                return None
            elif event == 'Confirmar':
                selected_item = values['listbox'][0] if values['listbox'] else None
                if selected_item:
                    categoria_selecionada = next(
                        (categoria for categoria in categorias if categoria.nome == selected_item),
                        None)
                    nome = values['nome']
                    descricao = values['descricao']
                    codigo = categoria_selecionada.codigo
                    if not nome.strip():
                        self.mostra_mensagem("Nome não pode estar vazio.")
                        return window.close()
                    if not descricao.strip():
                        self.mostra_mensagem("A descrição não pode estar vazia.")
                        return window.close()
                    categoria_editada = {"nome": nome, "descricao": descricao, "codigo": codigo}
                    window.close()
                    return categoria_editada
                else:
                    self.mostra_mensagem("É necessário selecionar pelo menos uma categoria para editar")

            elif event == 'listbox':
                selected_item = values['listbox'][0]
                categoria_selecionada = next(
                    (categoria for categoria in categorias if categoria.nome == selected_item), None)
                if categoria_selecionada:
                    window['nome'].update(categoria_selecionada.nome)
                    window['descricao'].update(categoria_selecionada.descricao)

    def mostrar_categoria_exclusao(self, categorias):
        sg.ChangeLookAndFeel('Dark')
        layout = [[sg.Text('-------- Excluir categoria ----------', font=("Helvica", 25))],
                  [sg.Listbox(values=[categoria.nome for categoria in categorias],
                              key='listbox',
                              select_mode=sg.LISTBOX_SELECT_MODE_SINGLE,
                              size=(100, 10),
                              enable_events=True)],
                  [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]

        window = sg.Window('Excluir Categoria', layout)

        while True:
            event, values = window.read()

            if event in (None, 'Cancelar'):
                window.close()
                return None
            elif event == 'Confirmar':
                selected_item = values['listbox'][0] if values['listbox'] else None
                if selected_item:
                    categoria_selecionada = next(
                        (categoria for categoria in categorias if categoria.nome == selected_item),

                        None)
                    window.close()
                    return categoria_selecionada
                else:
                    self.mostra_mensagem("Selecione a categoria que gostaria de excluir antes de confirmar")


    def confirmar_deletar_categoria(self, categoria):
        sg.ChangeLookAndFeel('Dark')
        layout = [
            [sg.Text(f'Tem certeza que deseja excluir a categoria - {categoria.nome}? Esta ação é irreversível.',
                     font=("Helvica", 25))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Excluir categoria').Layout(layout)

        button, values = self.__window.Read()

        if button in (None, 'Cancelar'):
            self.close()
            return None
        elif button == 'Confirmar':
            self.close()
            return 1

    def listar_categorias(self, categorias):
        data = [[categoria.nome, categoria.descricao] for categoria in categorias]

        layout = [
            [sg.Table(values=data,
                      headings=['Nome', 'Descrição'],
                      auto_size_columns=True,
                      col_widths=[50, 50],
                      justification='center',
                      key='-TABLE-')],
            [sg.Button('Voltar')]
        ]

        window = sg.Window('Lista de Categorias', layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'Voltar':
                break

        window.close()

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
