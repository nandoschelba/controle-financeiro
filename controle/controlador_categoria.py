from entidade.categoria import Categoria


class ControladorCategoria():
    def __init__(self, controlador_sistema):
        from limite.tela_categoria import TelaCategoria
        self.__controlador_sistema = controlador_sistema
        self.__tela_categoria = TelaCategoria(self)
        self.categorias = []

    def adicionar_categoria(self):
        dados_categoria = self.__tela_categoria.pega_dados_categoria()
        print(dados_categoria)
        codigo = len(self.categorias) + 1
        categoria = Categoria(codigo, dados_categoria["nome"], dados_categoria["descricao"])
        self.categorias.append(categoria)

    def buscar_categoria_por_codigo(self, codigo):
        for categoria in self.categorias:
            if categoria.codigo == codigo:
                return categoria
        return None

    def listar_categorias(self):
        for categoria in self.categorias:
            self.__tela_categoria.mostra_categoria({"codigo": categoria.codigo, "nome": categoria.nome,
                                                    "descricao": categoria.descricao})

    def remover_categoria(self):
        pass

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_categoria, 2: self.listar_categorias, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_categoria.tela_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()
