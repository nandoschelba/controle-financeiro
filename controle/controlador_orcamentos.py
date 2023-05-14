from entidade.meta import Meta
from entidade.orcamento import Orcamento
from limite.tela_orcamento import TelaOrcamento


class ControladorOrcamentos:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__orcamentos = []
        self.__metas = []
        self.__tela_orcamento = TelaOrcamento()

    def abre_tela(self):
        lista_opcoes = {1: self.lista_orcamentos, 2: self.adiciona_orcamento, 3: self.deleta_orcamento, 4: self.atualiza_orcamento,
                        5: self.adiciona_meta, 6: self.deleta_meta, 7: self.atualiza_meta, 8: self.emite_relatorio,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_orcamento.tela_opcoes()]()
        pass

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def lista_orcamentos(self):
        for orcamento in self.__orcamentos:
            usuario_logado = self.__controlador_principal.controlador_usuarios.pega_codigo_usuario_logado()
            if usuario_logado == orcamento.usuario:
                self.__tela_orcamento.mostra_orcamento({"codigo": orcamento.codigo, "valor_disponivel" : orcamento.valor_disponivel(),
                 "mes": orcamento.mes, "ano": orcamento.ano})
                for meta in orcamento.metas:
                    self.__tela_orcamento.mostra_meta({"codigo": meta.codigo, "meta": meta.meta, "categoria": meta.categoria.nome})

    def pega_orcamento_por_codigo(self, codigo):
        for orcamento in self.__orcamentos:
            if str(orcamento.codigo) == str(codigo):
                return orcamento
        return None

    def adiciona_orcamento(self):
        #Precisa criar metas primeiro
        dados_orcamento = self.__tela_orcamento.pega_dados_orcaento()
        metas = []

        while True:
            metas.append(self.add_meta())
            self.__tela_orcamento.mostra_mensagem("Meta adicionada com sucesso")
            dado_add_novo = self.__tela_orcamento.pega_add_novo()
            if dado_add_novo["adicionar_meta"] != "s":
                break
        usuario_logado = self.__controlador_principal.controlador_usuarios.pega_codigo_usuario_logado()
        self.__orcamentos.append(
            Orcamento(dados_orcamento["mes"], dados_orcamento["ano"], usuario_logado, metas))
        self.__tela_orcamento.mostra_mensagem("Orcamento registrado com sucesso")

    def add_meta(self):
        self.lista_metas()
        codigo_meta = self.__tela_orcamento.seleciona_meta()
        meta = self.pega_meta_por_codigo(codigo_meta)
        #não permitir none
        return meta

    def deleta_orcamento(self):
        self.lista_orcamentos()
        codigo_orcamento = self.__tela_orcamento.seleciona_orcamento()
        orcamento = self.pega_orcamento_por_codigo(codigo_orcamento)

        if (orcamento is not None):
            self.__orcamentos.remove(orcamento)
            self.lista_orcamentos()
        else:
            self.__tela_orcamento.mostra_mensagem("ATENCAO: Orçamento não existente")
        pass

    def atualiza_orcamento(self):
        self.lista_orcamentos()
        codigo_orcamento = self.__tela_orcamento.seleciona_orcamento()
        orcamento = self.pega_orcamento_por_codigo(codigo_orcamento)

        if (orcamento is not None):
            dados_orcamento = self.__tela_orcamento.pega_dados_orcaento()
            metas = []

            while True:
                metas.append(self.add_meta())
                self.__tela_orcamento.mostra_mensagem("Meta adicionada com sucesso")
                dado_add_novo = self.__tela_orcamento.pega_add_novo()
                if dado_add_novo["adicionar_meta"] != "s":
                    break

            orcamento.mes = dados_orcamento["mes"]
            orcamento.ano = dados_orcamento["ano"]
            orcamento.metas = metas
        else:
            self.__tela_gasto.mostra_mensagem("ATENCAO: Orçamento não existente")

    def emite_relatorio(self):
        dados = self.__tela_orcamento.pega_dados_relario()
        gastos = self.__controlador_principal.controlador_gastos.pega_gastos_por_usuario(dados["mes"], dados["ano"])

        orcamento_mes = None
        for orcamento in self.__orcamentos:
            if orcamento.mes == dados["mes"] & orcamento.ano == dados["ano"]:
                orcamento_mes = orcamento

        if (orcamento_mes is not None):
            relatorio = []

            for meta in orcamento_mes.metas:
                total_gasto = 0
                for gasto in gastos.itens:
                    if str(gasto.categoria.codigo) == str(meta.categoria.codigo):
                        total_gasto += gasto.valor
                relatorio.append({"mes": dados["mes"], "ano": dados["ano"], "categoria": meta.categoria.nome, "meta": meta.meta, "gasto": total_gasto})

            for item in relatorio:
                self.__tela_orcamento.mostra_relatorio(item)
        else:
            self.__tela_gasto.mostra_mensagem("ATENCAO: Não há orçamento para o mês e ano selecionado")


    def lista_metas(self):
        for meta in self.__metas:
            usuario_logado = self.__controlador_principal.controlador_usuarios.pega_codigo_usuario_logado()
            if usuario_logado == meta.usuario:
                self.__tela_orcamento.mostra_meta({"codigo": meta.codigo, "meta": meta.meta, "categoria": meta.categoria.nome})

    def pega_meta_por_codigo(self, codigo):
        for meta in self.__metas:
            if str(meta.codigo) == str(codigo):
                return meta
        return None

    def adiciona_meta(self):
        print("adiciona_meta")
        dados_meta = self.__tela_orcamento.pega_dados_meta()

        self.__controlador_principal.controlador_categorias.listar_categorias()
        codigo_categoria = self.__controlador_principal.controlador_categorias.seleciona_categoria()
        categoria = self.__controlador_principal.controlador_categorias.buscar_categoria_por_codigo(codigo_categoria)

        usuario_logado = self.__controlador_principal.controlador_usuarios.pega_codigo_usuario_logado()

        self.__metas.append(
            Meta(dados_meta["meta"], categoria, usuario_logado))
        self.__tela_orcamento.mostra_mensagem("Meta registrada com sucesso")

    def atualiza_meta(self):
        self.lista_metas()
        codigo_meta = self.__tela_orcamento.seleciona_meta()
        meta = self.pega_meta_por_codigo(codigo_meta)

        if (meta is not None):
            dados_meta = self.__tela_orcamento.pega_dados_meta()

            meta.meta = dados_meta["meta"]
        else:
            self.__tela_gasto.mostra_mensagem("ATENCAO: Orçamento não existente")

    def deleta_meta(self):
        self.lista_metas()
        codigo_meta = self.__tela_orcamento.seleciona_meta()
        meta = self.pega_meta_por_codigo(codigo_meta)

        if (meta is not None):
            self.__metas.remove(meta)
            self.lista_metas()
        else:
            self.__tela_orcamento.mostra_mensagem("ATENCAO: Meta não existente")
        pass