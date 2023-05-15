class TelaCategoria:

    def tela_opcoes(self):
        opcoes_validas = [0, 1, 2, 3, 4]
        print("\n------ Opções de Categoria ------")
        print("1 - Adicionar categoria")
        print("2 - Listar categoria")
        print("3 - Editar categoria")
        print("4 - Excluir categoria")
        print("0 - Voltar")
        opcao = input("Escolha a opção desejada: ")
        if not opcao.isdigit():
            return
        if int(opcao) not in opcoes_validas:
            return
        return int(opcao)

    def pega_dados_categoria(self):
        nome = input("\nDigite o nome da categoria: ")
        if not nome.strip():
            return print("\nNome não pode estar vazio.")
        descricao = input("Digite a descrição da categoria: ")
        if not descricao.strip():
            return print("\nDescrição não pode estar vazio.")
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

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)
