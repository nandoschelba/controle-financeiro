from controle.controlador_usuarios import ControladorUsuarios


class TelaUsuario:
    def __init__(self, controlador_usuario: ControladorUsuarios):
        self.__controlador_usuario = controlador_usuario

    def tela_opcoes(self):
        print("\n------ Opções de Usuários ------")
        print("1 - Adicionar usuário")
        print("2 - Listar usuários")
        #print("3 - Vincular categoria ao usuário")
        #print("4 - Editar usuário")
        print("0 - Voltar")
        opcao = int(input("Escolha a opção desejada: "))
        return opcao

    def pega_dados_usuario(self):
        nome = input("Nome: ")
        email = input("Email: ")
        tipo_usuario = int(input("Tipo de usuário (1 - Pessoa Física | 2 - Pessoa Jurídica): "))
        if tipo_usuario == 1:
            cpf = input("CPF: ")
            return self.__controlador_usuario.adiciona_usuario_fisico(nome, email, cpf)
        elif tipo_usuario == 2:
            cnpj = input("CNPJ: ")
            return self.__controlador_usuario.adiciona_usuario_juridico(nome, email, cnpj)

    def mostra_usuario(self, usuario):
        print("\n------ Dados do Usuário ------")
        print("Nome:", usuario.nome())
        print("Email:", usuario.email())
        if usuario.is_fisico():
            print("CPF:", usuario.identificador())
        elif usuario.is_juridico():
            print("CNPJ:", usuario.identificador())
        input("Pressione enter para continuar...")

    def seleciona_usuario(self):
        id = int(input("Digite o ID do usuário que deseja selecionar: "))
        return id

    def mostra_usuario(self, dados_usuario):
        print("NOME DO USUARIO: ", dados_usuario["nome"])
        print("EMAIL DO USUARIO: ", dados_usuario["email"])
        #verificar necessidade de mostrar cpf/cnpj
        print("\n")

    def mostra_mensagem(self, mensagem):
        print(mensagem)
        input("Pressione enter para continuar...")
