from entidade.meta import Meta
from entidade.orcamento import Orcamento
from limite.tela_orcamento import TelaOrcamento


class ControladorOrcamentos:
    def __init__(self, controlador_principal):
        self.controlador_principal = controlador_principal
        self.__orcamentos = []
        self.__metas = []
        self.__tela_orcamento = TelaOrcamento()

    def abre_tela(self):
        lista_opcoes = {1: self.lista_orcamentos, 2: self.adiciona_orcamento, 3: self.deleta_orcamento, 4: self.atualiza_orcamento,
                        5: self.adiciona_meta, 6: self.deleta_meta, 7: self.atualiza_meta,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_orcamento.tela_opcoes()]()
        pass

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def lista_orcamentos(self):
        for orcamento in self.__orcamentos:
            self.__tela_orcamento.mostra_orcamento({"codigo": orcamento.codigo, "valor_disponivel" : orcamento.valor_disponivel(),
                 "mes": orcamento.mes, "ano": orcamento.ano})
            for meta in orcamento.metas:
                self.__tela_orcamento.mostra_meta({"codigo": meta.codigo, "meta": meta.meta, "descricao": meta.descricao, "categoria": meta.categoria})

    def pega_orcamento_por_codigo(self, codigo):
        for orcamento in self.__orcamentos:
            if str(orcamento.codigo) == str(codigo):
                return orcamento
        return None

    def adiciona_orcamento(self):
        print("adiciona_orcamento")
        dados_orcamento = self.__tela_orcamento.pega_dados_orcaento()
        metas = []

        while True:
            metas.append(self.add_meta())
            self.__tela_orcamento.mostra_mensagem("Meta adicionada com sucesso")
            dado_add_novo = self.__tela_orcamento.pega_add_novo()
            if dado_add_novo["adicionar_meta"] != "s":
                break
        self.__orcamentos.append(
            Orcamento(dados_orcamento["mes"], dados_orcamento["ano"], 3, metas))
        self.__tela_orcamento.mostra_mensagem("Orcamento registrado com sucesso")

    def add_meta(self):
        self.lista_metas()
        codigo_meta = self.__tela_orcamento.seleciona_meta()
        meta = self.pega_meta_por_codigo(codigo_meta)
        return meta

    def deleta_orcamento(self):
        # implement code to delete an existing budget
        pass

    def atualiza_orcamento(self):
        # implement code to update an existing budget
        pass

    def emite_relatorio(self, mes, ano):
        # implement code to generate a report for the specified month and year
        pass

    def lista_metas(self):
        for meta in self.__metas:
            self.__tela_orcamento.mostra_meta({"codigo": meta.codigo, "meta": meta.meta, "descricao": meta.descricao, "categoria": meta.categoria})

    def pega_meta_por_codigo(self, codigo):
        for meta in self.__metas:
            if str(meta.codigo) == str(codigo):
                return meta
        return None

    def adiciona_meta(self):
        print("adiciona_meta")
        dados_meta = self.__tela_orcamento.pega_dados_meta()
        self.__metas.append(
            Meta(dados_meta["meta"], dados_meta["descricao"], "categoria"))
        self.__tela_orcamento.mostra_mensagem("Meta registrada com sucesso")

    def atualiza_meta(self, codigo):
        # implement code to update an existing goal
        pass

    def deleta_meta(self):
        # implement code to delete an existing goal
        pass