from entidade.categoria import Categoria


class ControladorCategoria():
    def __init__(self, controlador_sistema, controlador_usuarios):
        from limite.tela_categoria import TelaCategoria
        self.__controlador_sistema = controlador_sistema
        self.__controlador_usuarios = controlador_usuarios
        self.__tela_categoria = TelaCategoria(self)
        self.categorias = []

    def adicionar_categoria(self):
        dados_categoria = self.__tela_categoria.pega_dados_categoria()
        codigo = len(self.categorias) + 1
        categoria = Categoria(codigo, dados_categoria["nome"], dados_categoria["descricao"],
                              self.__controlador_usuarios.usuario_logado.identificador())
        self.categorias.append(categoria)

    def buscar_categoria_por_codigo(self):
        categorias_usuario_logado = [categoria for categoria in self.categorias
                                     if
                                     categoria.id_usuario == self.__controlador_usuarios.usuario_logado.identificador()]

        if not categorias_usuario_logado:
            return self.__tela_categoria.mostra_mensagem("\nNão existem categorias cadastradas.")

        codigo = self.__tela_categoria.pega_codigo_categoria_edicao()
        if not codigo:
            return None
        elif not isinstance(codigo, int):
            self.__tela_categoria.mostra_mensagem("\nO código deve ser um número inteiro.")
            return None

        for categoria in categorias_usuario_logado:
            if categoria.codigo == codigo:
                novos_dados_categoria = self.__tela_categoria.pega_novos_dados_categoria(categoria)
                return self.edita_categoria(novos_dados_categoria, categorias_usuario_logado)
        self.__tela_categoria.mostra_mensagem("\nCategoria não encontrada.")

    def edita_categoria(self, novos_dados_categoria, categorias_usuario_logado):
        codigo = novos_dados_categoria["codigo"]
        for categoria in categorias_usuario_logado:
            if categoria.codigo == codigo:
                categoria.nome = novos_dados_categoria["nome"]
                categoria.descricao = novos_dados_categoria["descricao"]
                self.__tela_categoria.mostra_mensagem("\nCategoria editada com sucesso.")
                break

    def listar_categorias(self):
        categorias_usuario_logado = []
        for categoria in self.categorias:
            if categoria.id_usuario == self.__controlador_usuarios.usuario_logado.identificador():
                categorias_usuario_logado.append(categoria)
        if categorias_usuario_logado:
            for categoria in categorias_usuario_logado:
                self.__tela_categoria.mostra_categoria({"codigo": categoria.codigo, "nome": categoria.nome,
                                                        "descricao": categoria.descricao})
        else:
            print("\nNão existem categorias cadastradas.")

    def selecionar_categoria_exclusao(self):
        categorias_usuario_logado = [categoria for categoria in self.categorias
                                     if
                                     categoria.id_usuario == self.__controlador_usuarios.usuario_logado.identificador()]

        if not categorias_usuario_logado:
            return self.__tela_categoria.mostra_mensagem("\nNão existem categorias cadastradas.")

        codigo = self.__tela_categoria.pega_codigo_categoria_excluir()
        if not codigo:
            return None
        elif not isinstance(codigo, int):
            self.__tela_categoria.mostra_mensagem("\nO código deve ser um número inteiro.")
            return None

        for categoria in categorias_usuario_logado:
            if categoria.codigo == codigo:
                self.__tela_categoria.mostra_categoria(categoria)
                return self.excluir_categoria(categoria.codigo)
        self.__tela_categoria.mostra_mensagem("\nCategoria não encontrada.")

    def excluir_categoria(self, codigo):
        for categoria in self.categorias:
            if categoria.codigo == codigo and categoria.id_usuario == self.__controlador_usuarios.usuario_logado.identificador():
                self.categorias.remove(categoria)
                self.__tela_categoria.mostra_mensagem("\nCategoria excluída com sucesso!")
                break

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_categoria, 2: self.listar_categorias, 3: self.buscar_categoria_por_codigo,
                        4: self.selecionar_categoria_exclusao, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_categoria.tela_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()
