class TelaSistema:
    def tela_opcoes_usuario_deslogado(self):
        print("\n-------- Gestão de gastos ---------")
        print("1 - Login")
        print("2 - Realizar cadastro no sistema")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao desejada: "))
        return opcao

    def tela_opcoes_usuario_logado(self):
        print("\n-------- Gestão de gastos ---------")
        print("3 - Opções de usuário")
        print("4 - Categorias")
        print("5 - Orçamentos")
        print("6 - Gastos")
        print("7 - Logout")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao desejada: "))
        return opcao
