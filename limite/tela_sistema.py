class TelaSistema:
    def tela_opcoes_usuario_deslogado(self):
        opcoes_validas = [0, 1, 2]
        print("\n-------- Gestão de gastos ---------")
        print("1 - Login")
        print("2 - Realizar cadastro no sistema")
        print("0 - Finalizar sistema")
        opcao = input("Escolha a opção desejada: ")
        if not opcao.isdigit():
            print("\n A opção selecionada deve ser um número.")
            return
        if int(opcao) not in opcoes_validas:
            print("\n Digite uma opção válida.")
        return int(opcao)

    def tela_opcoes_usuario_logado(self):
        print("\n-------- Gestão de gastos ---------")
        print("1 - Opções de usuário")
        print("2 - Categorias")
        print("3 - Orçamentos")
        print("4 - Gastos")
        print("5 - Logout")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao desejada: "))
        return opcao
