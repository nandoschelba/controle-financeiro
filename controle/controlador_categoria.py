from entidade.categoria import Categoria
from limite.tela_categoria import TelaCategoria
from persistencia.categoria_dao import CategoriaDAO


class ControladorCategoria:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_categoria = TelaCategoria()
        self.__categoria_dao = CategoriaDAO()

    def adicionar_categoria(self):
        dados_categoria = self.__tela_categoria.pega_dados_categoria()
        if dados_categoria:
            nome_categoria = dados_categoria["nome"]
            descricao_categoria = dados_categoria["descricao"]
            usuario = self.pega_usuario_logado()
            for categoria in self.retorna_categorias_usuario_logado(False):
                if categoria.nome == nome_categoria and categoria.usuario.identificador() == \
                                                        self.pega_id_usuario_logado():
                    self.__tela_categoria.mostra_mensagem("Já existe uma categoria com esse nome.")
                    return
            codigo = len(self.__categoria_dao.get_all()) + 1
            categoria = Categoria(codigo, nome_categoria, descricao_categoria, usuario)
            self.__categoria_dao.add(codigo, categoria)
            self.__tela_categoria.mostra_mensagem("\nCategoria cadastrada com sucesso!")

    def buscar_categoria_e_editar(self):
        categorias_usuario = self.retorna_categorias_usuario_logado()
        if categorias_usuario:
            novos_dados_categoria = self.__tela_categoria.editar_categoria(categorias_usuario)
            if novos_dados_categoria is not None:
                return self.edita_categoria(novos_dados_categoria, categorias_usuario)

    def edita_categoria(self, novos_dados_categoria, categorias_usuario_logado):
        codigo = novos_dados_categoria["codigo"]
        for categoria in categorias_usuario_logado:
            if categoria.codigo == codigo:
                categoria.nome = novos_dados_categoria["nome"]
                categoria.descricao = novos_dados_categoria["descricao"]
                self.__categoria_dao.update(categoria.codigo, categoria)
                self.__tela_categoria.mostra_mensagem("Categoria editada com sucesso.")
                break

    def listar_categorias(self):
        categorias_usuario_logado = self.retorna_categorias_usuario_logado()
        if categorias_usuario_logado:
            self.__tela_categoria.listar_categorias(categorias_usuario_logado)

    def busca_categoria_e_exclui(self):
        categorias_usuario = self.retorna_categorias_usuario_logado()
        if categorias_usuario:
            categoria_escolhida = self.__tela_categoria.mostrar_categoria_exclusao(categorias_usuario)
            if categoria_escolhida is not None:
                if self.__tela_categoria.confirmar_deletar_categoria(categoria_escolhida) == 1:
                    return self.excluir_categoria(categoria_escolhida.codigo)
                else:
                    return

    def excluir_categoria(self, codigo):
        for categoria in self.__categoria_dao.get_all():
            if categoria.codigo == codigo and categoria.usuario.identificador() == self.pega_id_usuario_logado():
                self.__categoria_dao.remove(categoria.codigo)
                self.__tela_categoria.mostra_mensagem("\nCategoria excluída com sucesso!")
                break

    def seleciona_categoria(self):
        categorias_usuario = self.retorna_categorias_usuario_logado()
        if categorias_usuario:
            return self.__tela_categoria.pega_codigo_categoria(categorias_usuario)

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_categoria, 2: self.listar_categorias, 3: self.buscar_categoria_e_editar,
                        4: self.busca_categoria_e_exclui, 0: self.retornar}
        while True:
            lista_opcoes[self.__tela_categoria.tela_opcoes()]()

    def retorna_categorias_usuario_logado(self, mostrar_mensagem: bool = True):
        categorias_usuario_logado = [categoria for categoria in self.__categoria_dao.get_all()
                                     if
                                     categoria.usuario.identificador() == self.pega_id_usuario_logado()]

        if not categorias_usuario_logado:
            if mostrar_mensagem:
                self.__tela_categoria.mostra_mensagem("\nNão existem categorias cadastradas.")
            return []
        else:
            return categorias_usuario_logado

    def buscar_categoria_por_codigo(self, codigo: int):
        categorias_usuario_logado = self.retorna_categorias_usuario_logado()
        if categorias_usuario_logado:
            for categoria in categorias_usuario_logado:
                if categoria.codigo == codigo:
                    return categoria
            return self.__tela_categoria.mostra_mensagem("\nCategoria não encontrada.")
        else:
            return None

    def pega_usuario_logado(self):
        return self.__controlador_sistema.controlador_usuarios.usuario_logado

    def pega_id_usuario_logado(self):
        return self.pega_usuario_logado().identificador()

    def retornar(self):
        self.__controlador_sistema.abre_tela()
