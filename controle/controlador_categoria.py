from entidade.categoria import Categoria


class ControladorCategoria:
    def __init__(self, controlador_sistema):
        from limite.tela_categoria import TelaCategoria
        self.__controlador_sistema = controlador_sistema
        self.__tela_categoria = TelaCategoria(self)
        self.categorias = []

    def adicionar_categoria(self):
        dados_categoria = self.__tela_categoria.pega_dados_categoria()
        codigo = len(self.categorias) + 1
        categoria = Categoria(codigo, dados_categoria["nome"], dados_categoria["descricao"],
                              self.pega_id_usuario_logado())
        self.categorias.append(categoria)

    def buscar_categoria_e_editar(self):
        categorias_usuario_logado = self.retorna_categorias_usuario_logado()
        if categorias_usuario_logado:
            codigo = self.__tela_categoria.pega_codigo_categoria("Insira o ID da categoria que você quer editar: ")
            if not codigo:
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
            if categoria.id_usuario == self.pega_id_usuario_logado():
                categorias_usuario_logado.append(categoria)
        if categorias_usuario_logado:
            for categoria in categorias_usuario_logado:
                self.__tela_categoria.mostra_categoria({"codigo": categoria.codigo, "nome": categoria.nome,
                                                        "descricao": categoria.descricao})
        else:
            print("\nNão existem categorias cadastradas.")

    def busca_categoria_e_exclui(self):
        categorias_usuario_logado = self.retorna_categorias_usuario_logado()
        if categorias_usuario_logado:
            codigo = self.__tela_categoria.pega_codigo_categoria("Insira o ID da categoria que você quer excluir: ")
            if not codigo:
                return None
            for categoria in categorias_usuario_logado:
                if categoria.codigo == codigo:
                    if self.__tela_categoria.confirmar_deletar_categoria() == 1:
                        return self.excluir_categoria(codigo)
                    else:
                        return
        self.__tela_categoria.mostra_mensagem("\nCategoria não encontrada.")

    def excluir_categoria(self, codigo):
        for categoria in self.categorias:
            if categoria.codigo == codigo and categoria.id_usuario == self.pega_id_usuario_logado():
                self.categorias.remove(categoria)
                self.__tela_categoria.mostra_mensagem("\nCategoria excluída com sucesso!")
                break

    def seleciona_categoria(self):
        return self.__tela_categoria.seleciona_categoria()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_categoria, 2: self.listar_categorias, 3: self.buscar_categoria_e_editar,
                        4: self.busca_categoria_e_exclui, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_categoria.tela_opcoes()]()

    def retorna_categorias_usuario_logado(self):
        categorias_usuario_logado = [categoria for categoria in self.categorias
                                     if
                                     categoria.id_usuario == self.pega_id_usuario_logado()]

        if not categorias_usuario_logado:
            return self.__tela_categoria.mostra_mensagem("\nNão existem categorias cadastradas.")
        else:
            return categorias_usuario_logado

    def buscar_categoria_por_codigo(self, codigo: int):
        for categoria in self.categorias:
            if categoria.codigo == codigo and categoria.id_usuario == self.pega_id_usuario_logado():
                return categoria
        self.__tela_categoria.mostra_mensagem("\nCategoria não encontrada.")
        return None

    def pega_id_usuario_logado(self):
        return self.__controlador_sistema.controlador_usuarios.usuario_logado.identificador()

    def retornar(self):
        self.__controlador_sistema.abre_tela()
