from controle.controlador_usuarios import ControladorUsuarios


class TelaUsuario:
    def __init__(self, controlador_usuario: ControladorUsuarios):
        self.__controlador_usuario = controlador_usuario

    def tela_opcoes(self):
        opcoes_validas = [0, 1, 2]
        print("\n------ Opções de Usuário ------")
        print("1 - Editar cadastro")
        print("2 - Encerrar conta")
        print("0 - Voltar")
        opcao = input("Escolha a opção desejada: ")
        if not opcao.isdigit():
            return
        if int(opcao) not in opcoes_validas:
            return
        return int(opcao)

    def pega_dados_usuario(self):
        tipo_usuarios_validos = [1, 2]
        nome = input("\nNome: ")
        if not nome.strip():
            return print("\nNome não pode estar vazio.")
        email = input("Email: ")
        if not email.strip():
            return print("\nEmail não pode estar vazio.")
        tipo_usuario = input("Tipo de usuário (1 - Pessoa Física | 2 - Pessoa Jurídica): ")
        if not tipo_usuario.isdigit():
            return print("\nTipo de usuário deve ser um número inteiro.")
        if int(tipo_usuario) not in tipo_usuarios_validos:
            return print("\nDigite uma opção válida.")
        tipo_usuario = int(tipo_usuario)
        if tipo_usuario == 1:
            cpf = input("CPF: ")
            if not cpf.isdigit():
                return print("\nCPF deve ser um número inteiro.")
            if len(cpf) != 11:
                return print("\nUm CPF válido deve ter 11 digitos.")
            return self.__controlador_usuario.adiciona_usuario_fisico(nome, email, int(cpf))
        elif tipo_usuario == 2:
            cnpj = input("CNPJ: ")
            if not cnpj.isdigit():
                return print("\nCNPJ deve ser um número inteiro.")
            if len(cnpj) != 14:
                return print("\nUm CNPJ válido deve ter 14 digitos.")
            return self.__controlador_usuario.adiciona_usuario_juridico(nome, email, int(cnpj))

    def pega_dados_usuario_edicao(self):
        while True:
            nome = input("\nNovo nome: ")
            if not nome.strip():
                return print("\nNome não pode estar vazio.")
            email = input("Novo email: ")
            if not email.strip():
                return print("\nEmail não pode estar vazio.")
            if nome == "" or email == "":
                print("\nNome e email não podem ser vazios.")
            else:
                return {"nome": nome, "email": email}

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)

    def loga_usuario(self):
        email = input("\nInsira seu email: ")
        if not email.strip():
            return print("\nEmail não pode estar vazio.")
        identificador = input("Insira seu CPF/CNPJ: ")
        try:
            identificador = int(identificador)
        except ValueError:
            print("CPF/CNPJ deve ser um número inteiro.")
            return None
        return {"email": email, "id": identificador}

    def confirmar_deletar_conta(self):
        opcoes_validas = [0, 1]
        print("\n------ Tem certeza que deseja excluir sua conta? Esta ação é irreversível. ------")
        print("1 - Sim")
        print("0 - Voltar")
        opcao = input("Escolha a opção desejada: ")
        if not opcao.isdigit():
            print("\n A opção selecionada deve ser um número.")
            return
        if int(opcao) not in opcoes_validas:
            print("\n Digite uma opção válida.")
        return int(opcao)
