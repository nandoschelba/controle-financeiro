from entidade.usuario_juridico import UsuarioJuridico
from entidade.usuario_fisico import UsuarioFisico


class ControladorUsuarios:
    def __init__(self, controlador_sistema):
        from limite.tela_usuario import TelaUsuario
        self.__usuarios = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_usuario = TelaUsuario(self)
        self.usuario_logado = None

    def pega_tipo_usuario(self):
        self.__tela_usuario.pega_dados_usuario()

    def adiciona_usuario_juridico(self, nome: str, email: str, cnpj: int):
        if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(cnpj, int):
            return self.__tela_usuario.mostra_mensagem("\nDados do usuário inválidos. Certifique-se de que o nome é uma"
                                                       " string, o email é uma string e o cnpj são apenas números.")
        for usuario in self.__usuarios:
            if isinstance(usuario, UsuarioFisico) and (usuario.email == email or usuario.identificador() == cnpj):
                return self.__tela_usuario.mostra_mensagem("\nJá existe um usuário cadastrado com este e-mail ou CNPJ.")
        usuario_juridico = UsuarioJuridico(nome, email, cnpj)
        self.__usuarios.append(usuario_juridico)
        self.__tela_usuario.mostra_mensagem("\nCadastro relizado com sucesso!")

    def adiciona_usuario_fisico(self, nome, email, cpf):
        if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(cpf, int):
            return self.__tela_usuario.mostra_mensagem("\nDados do usuário inválidos. Certifique-se de que o nome é uma"
                                                       " string, o email é uma string e o cpf são apenas números.")
        for usuario in self.__usuarios:
            if isinstance(usuario, UsuarioFisico) and (usuario.email == email or usuario.identificador() == cpf):
                return self.__tela_usuario.mostra_mensagem("\nJá existe um usuário cadastrado com este e-mail ou CPF.")
        usuario_fisico = UsuarioFisico(nome, email, cpf)
        self.__usuarios.append(usuario_fisico)
        self.__tela_usuario.mostra_mensagem("\nCadastro relizado com sucesso!")

    def abre_tela_usuario(self):
        lista_opcoes = {1: self.editar_usuario, 2: self.encerrar_conta, 0: self.retornar}
        while True:
            lista_opcoes[self.__tela_usuario.tela_opcoes()]()

    def editar_usuario(self):
        dados_edicao = self.__tela_usuario.pega_dados_usuario_edicao()
        if dados_edicao:
            self.usuario_logado.nome = dados_edicao["nome"]
            self.usuario_logado.email = dados_edicao["email"]
            for usuario in self.__usuarios:
                if usuario.identificador() == self.usuario_logado.identificador():
                    usuario.nome = dados_edicao["nome"]
                    usuario.email = dados_edicao["email"]
                    break
            self.__tela_usuario.mostra_mensagem("\nUsuário editado com sucesso!")

    def encerrar_conta(self):
        lista_opcoes = {1: self.deletar_usuario, 0: self.abre_tela_usuario}
        while True:
            try:
                opcao = self.__tela_usuario.confirmar_deletar_conta()
                lista_opcoes[opcao]()
            except KeyError:
                self.__tela_usuario.mostra_mensagem("\nOpção inválida. Tente novamente.")

    def deletar_usuario(self):
        self.__usuarios.remove(self.usuario_logado)
        self.usuario_logado = None
        self.__tela_usuario.mostra_mensagem("\nConta excluída com sucesso!")
        self.retornar()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def efetuar_login(self):
        input_login_usuario = self.__tela_usuario.loga_usuario()
        if input_login_usuario:
            for usuario in self.__usuarios:
                if usuario.identificador() == input_login_usuario["id"] and \
                        usuario.email == input_login_usuario["email"]:
                    self.usuario_logado = usuario
                    self.__tela_usuario.mostra_mensagem("\nLogin efetuado!")
                    break
            else:
                self.__tela_usuario.mostra_mensagem("\nUsuário não encontrado.")
                self.retornar()

    def efetuar_logout(self):
        if not self.usuario_logado:
            self.__tela_usuario.mostra_mensagem("\nNão há usuário logado!")
            self.retornar()
        else:
            self.usuario_logado = None
            self.__tela_usuario.mostra_mensagem("\nLogout efetuado!")
            self.retornar()

    def pega_codigo_usuario_logado(self):
        if self.usuario_logado:
            return self.usuario_logado.identificador()
        else:
            return 0
