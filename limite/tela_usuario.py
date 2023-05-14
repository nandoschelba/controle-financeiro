from controle.controlador_usuarios import ControladorUsuarios
from exceptions.tipo_invalido_error import TipoInvalidoError


class TelaUsuario:
    def __init__(self, controlador_usuario: ControladorUsuarios):
        self.__controlador_usuario = controlador_usuario

    def tela_opcoes(self):
        print("\n------ Opções de Usuário ------")
        print("1 - Editar cadastro")
        print("2 - Encerrar conta")
        print("0 - Voltar")
        opcao = int(input("Escolha a opção desejada: "))
        return opcao

    def pega_dados_usuario(self):
        nome = input("\nNome: ")
        email = input("Email: ")
        tipo_usuario = input("Tipo de usuário (1 - Pessoa Física | 2 - Pessoa Jurídica): ")
        try:
            tipo_usuario = int(tipo_usuario)
            if tipo_usuario == 1:
                cpf = input("CPF: ")
                if not cpf.isdigit():
                    raise TipoInvalidoError("CPF deve ser um número inteiro.")
                return self.__controlador_usuario.adiciona_usuario_fisico(nome, email, int(cpf))
            elif tipo_usuario == 2:
                cnpj = input("CNPJ: ")
                if not cnpj.isdigit():
                    raise TipoInvalidoError("CNPJ deve ser um número inteiro.")
                return self.__controlador_usuario.adiciona_usuario_juridico(nome, email, int(cnpj))
            else:
                raise TipoInvalidoError("Tipo de usuário inválido.")
        except ValueError:
            raise TipoInvalidoError("Tipo de usuário deve ser um número inteiro.")

    def pega_dados_usuario_edicao(self):
        while True:
            nome = input("\nNovo nome: ")
            email = input("Novo email: ")
            if nome == "" or email == "":
                print("\nNome e email não podem ser vazios.")
            else:
                return {"nome": nome, "email": email}

    def mostra_usuario(self, usuario):
        print("\n------ Dados do Usuário ------")
        print("Nome:", usuario.nome())
        print("Email:", usuario.email())

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def loga_usuario(self):
        email = input("\nInsira seu email: ")
        identificador = input("Insira seu CPF/CNPJ: ")
        if not isinstance(identificador, int):
            try:
                identificador = int(identificador)
            except ValueError:
                raise TypeError("CPF/CNPJ deve ser um número inteiro.")
        return {"email": email, "id": identificador}

    def confirmar_deletar_conta(self):
        print("\n------ Tem certeza que deseja excluir sua conta? Esta ação é irreversível. ------")
        print("1 - Sim")
        print("0 - Voltar")
        opcao = int(input("Escolha a opção desejada: "))
        return opcao