class TelaSistema:
    def tela_opcoes_usuario_deslogado(self):
        opcoes_validas = [0, 1, 2]
        print("\n-------- Gestão de gastos ---------")
        print("1 - Login")
        print("2 - Realizar cadastro no sistema")
        print("0 - Finalizar sistema")
        opcao = input("Escolha a opção desejada: ")
        if not opcao.isdigit():
            return
        if int(opcao) not in opcoes_validas:
            return
        return int(opcao)

    def tela_opcoes_usuario_logado(self):
        opcoes_validas = [0, 1, 2, 3, 4, 5]
        print("\n-------- Gestão de gastos ---------")
        print("1 - Opções de usuário")
        print("2 - Categorias")
        print("3 - Orçamentos")
        print("4 - Gastos")
        print("5 - Logout")
        print("0 - Finalizar sistema")
        opcao = input("Escolha a opção desejada: ")
        if not opcao.isdigit():
            return
        if int(opcao) not in opcoes_validas:
            return
        return int(opcao)

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)