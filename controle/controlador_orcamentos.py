from entidade.meta import Meta
from entidade.orcamento import Orcamento
from exceptions.categoria_invalida_error import CategoriaInvalidaError
from exceptions.meta_invalida_error import MetaInvalidaError
from exceptions.meta_proibida_error import MetaProibidaError
from exceptions.tipo_invalido_error import TipoInvalidoError
from limite.tela_orcamento import TelaOrcamento
from persistencia.meta_dao import MetaDAO
from persistencia.orcameto_dao import OrcamentoDAO


class ControladorOrcamentos:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__meta_dao = MetaDAO()
        self.__orcamento_dao = OrcamentoDAO()
        self.__tela_orcamento = TelaOrcamento()

    def abre_tela(self):
        lista_opcoes = {1: self.lista_orcamentos, 2: self.adiciona_orcamento, 3: self.deleta_orcamento,
                        4: self.atualiza_orcamento, 5: self.lista_metas, 6: self.adiciona_meta, 7: self.deleta_meta,
                        8: self.atualiza_meta, 9: self.emite_relatorio, 0: self.retornar}
        while True:
            try:
                lista_opcoes[self.__tela_orcamento.tela_opcoes()]()
            except KeyError:
                self.__tela_orcamento.mostra_error_mensagem("Opção inválida. Digite um número válido.")


    def retornar(self):
        self.__controlador_principal.abre_tela()

    def lista_orcamentos(self):
        orcamentos = []
        for orcamento in self.pega_lista_orcamentos():
            orcamentos.append({"codigo": orcamento.codigo, "valor_disponivel": orcamento.valor_disponivel(),
                               "mes": orcamento.mes, "ano": orcamento.ano, "metas": orcamento.metas})
        if len(orcamentos) == 0:
            self.__tela_orcamento.mostra_mensagem("ATENCAO: Não há orçamentos")
            return
        self.__tela_orcamento.mostra_orcamento(orcamentos)

    def pega_lista_orcamentos(self):
        usuario_logado = self.__controlador_principal.controlador_usuarios.pega_codigo_usuario_logado()
        orcamentos = []
        for orcamento in self.__orcamento_dao.get_all():
            if usuario_logado == orcamento.usuario.identificador():
                orcamentos.append(orcamento)
        return orcamentos

    def pega_orcamento_por_codigo(self, codigo):
        for orcamento in self.__orcamento_dao.get_all():
            if str(orcamento.codigo) == str(codigo):
                return orcamento
        return None

    def adiciona_orcamento(self):
        if len(self.pega_metas_usuario()) == 0:
            self.__tela_orcamento.mostra_error_mensagem("Você não tem metas. Crie metas primeiro")
        else:
            dados_orcamento = self.__tela_orcamento.pega_dados_orcaento()
            usuario_logado = self.__controlador_principal.controlador_usuarios.pega_codigo_usuario_logado()

            for orcamento in self.__orcamento_dao.get_all():
                if str(orcamento.mes) == str(dados_orcamento["mes"]) and str(orcamento.ano) == str(dados_orcamento["ano"]) and orcamento.usuario.identificador() == usuario_logado:
                    self.__tela_orcamento.mostra_error_mensagem("Você já tem um orçamento para o mesmo mês! Não é possível cadastrar outro orçamento.")
                    return
            metas = []

            while True:
                try:
                    metas.append(self.add_meta(metas))
                except MetaInvalidaError as e:
                    self.__tela_orcamento.mostra_error_mensagem(e)
                    return
                except MetaProibidaError as e:
                    self.__tela_orcamento.mostra_error_mensagem(e)
                    return
                self.__tela_orcamento.mostra_mensagem("Meta adicionada com sucesso")
                dado_add_novo = self.__tela_orcamento.pega_add_novo()
                if not dado_add_novo["adicionar_meta"]:
                    break

            usuario_logado_object = self.__controlador_principal.controlador_usuarios.pega_usuario_logado()
            self.__orcamento_dao.add(
                Orcamento(dados_orcamento["mes"], dados_orcamento["ano"], usuario_logado_object, metas))
            print(len(self.__orcamento_dao.get_all()))
            self.__tela_orcamento.mostra_mensagem("Orcamento registrado com sucesso")

    def add_meta(self, metas):
        metas_usuario = self.pega_metas_usuario()
        if len(metas_usuario) == 0:
            self.__tela_orcamento.mostra_mensagem("ATENCAO: Não há metas")
            return
        codigo_meta = self.__tela_orcamento.seleciona_meta(metas_usuario)
        meta = self.pega_meta_por_codigo(codigo_meta)
        if meta is not None:
            for meta_adicionada in metas:
                if meta_adicionada.categoria.nome == meta.categoria.nome:
                    raise MetaProibidaError
            return meta
        else:
            raise MetaInvalidaError

    def deleta_orcamento(self):
        orcamentos_usuario = self.pega_lista_orcamentos()
        if len(orcamentos_usuario) == 0:
            self.__tela_orcamento.mostra_mensagem("ATENCAO: Não há orçamentos")
            return
        codigo_orcamento = self.__tela_orcamento.seleciona_orcamento(orcamentos_usuario)
        orcamento = self.pega_orcamento_por_codigo(codigo_orcamento)

        if orcamento is not None:
            self.__orcamento_dao.remove(orcamento.codigo)
            self.lista_orcamentos()
        else:
            self.__tela_orcamento.mostra_mensagem("ATENCAO: Orçamento não existente")
        pass

    def atualiza_orcamento(self):
        orcamentos_usuario = self.pega_lista_orcamentos()
        if len(orcamentos_usuario) == 0:
            self.__tela_orcamento.mostra_mensagem("ATENCAO: Não há orçamentos")
            return
        codigo_orcamento = self.__tela_orcamento.seleciona_orcamento(orcamentos_usuario)
        orcamento = self.pega_orcamento_por_codigo(codigo_orcamento)

        if orcamento is not None:
            dados_orcamento = self.__tela_orcamento.pega_dados_orcaento()
            metas = []

            while True:
                try:
                    metas.append(self.add_meta(metas))
                except MetaInvalidaError as e:
                    self.__tela_orcamento.mostra_error_mensagem(e)
                    return
                except MetaProibidaError as e:
                    self.__tela_orcamento.mostra_error_mensagem(e)
                    return
                self.__tela_orcamento.mostra_mensagem("Meta adicionada com sucesso")
                dado_add_novo = self.__tela_orcamento.pega_add_novo()
                if not dado_add_novo["adicionar_meta"]:
                    break

            orcamento.mes = dados_orcamento["mes"]
            orcamento.ano = dados_orcamento["ano"]
            orcamento.metas = metas
        else:
            self.__tela_orcamento.mostra_mensagem("ATENCAO: Orçamento não existente")

    def emite_relatorio(self):
        dados = self.__tela_orcamento.pega_dados_relario()
        gastos = self.__controlador_principal.controlador_gastos.pega_gastos_por_usuario(dados["mes"], dados["ano"])
        orcamento_mes = None
        for orcamento in self.__orcamento_dao.get_all():
            if str(orcamento.mes) == str(dados["mes"]) and str(orcamento.ano) == str(dados["ano"]):
                orcamento_mes = orcamento

        if orcamento_mes is not None:
            relatorio = []

            for meta in orcamento_mes.metas:
                total_gasto = 0
                for gasto in gastos:
                    for item in gasto.itens:
                        if str(item.categoria.codigo) == str(meta.categoria.codigo):
                            total_gasto += item.valor
                relatorio.append({"mes": dados["mes"], "ano": dados["ano"], "categoria": meta.categoria.nome,
                                  "meta": meta.meta, "gasto": total_gasto})

            if len(relatorio) == 0:
                self.__tela_orcamento.mostra_mensagem("ATENCAO: Não há registros para o peeríodo selecionado")
                return
            self.__tela_orcamento.mostra_relatorio(relatorio)
        else:
            self.__tela_orcamento.mostra_mensagem("ATENCAO: Não há orçamento para o mês e ano selecionado")


    def lista_metas(self):
        metas = []
        for meta in self.pega_metas_usuario():
            metas.append({"codigo": meta.codigo, "meta": meta.meta,
                                               "categoria": meta.categoria.nome})
        self.__tela_orcamento.mostra_meta(metas)

    def pega_meta_por_codigo(self, codigo):
        for meta in self.pega_metas_usuario():
            if str(meta.codigo) == str(codigo):
                return meta
        return None

    def adiciona_meta(self):
        dados_meta = self.__tela_orcamento.pega_dados_meta()
        if dados_meta is None:
            return
        try:
            if self.isfloat(dados_meta["meta"]):
                categoria = self.__controlador_principal.controlador_categorias.seleciona_categoria()
                usuario_logado = self.__controlador_principal.controlador_usuarios.pega_usuario_logado()

                if categoria is not None:
                    self.__meta_dao.add(
                        Meta(float(dados_meta["meta"]), categoria, usuario_logado))
                    self.__tela_orcamento.mostra_mensagem("Meta registrada com sucesso")
                else:
                    raise CategoriaInvalidaError
            else:
                raise TipoInvalidoError
        except CategoriaInvalidaError as e:
            self.__tela_orcamento.mostra_error_mensagem(e)
            return
        except TipoInvalidoError as e:
            self.__tela_orcamento.mostra_error_mensagem(e)
            return

    def atualiza_meta(self):
        metas = self.pega_metas_usuario()
        if len(metas) == 0:
            self.__tela_orcamento.mostra_mensagem("ATENCAO: Não há metas")
            return
        codigo_meta = self.__tela_orcamento.seleciona_meta(metas)
        meta = self.pega_meta_por_codigo(codigo_meta)

        if meta is not None:
            dados_meta = self.__tela_orcamento.pega_dados_meta()

            meta.meta = dados_meta["meta"]
        else:
            self.__tela_orcamento.mostra_mensagem("ATENCAO: Orçamento não existente")

    def deleta_meta(self):
        metas = self.pega_metas_usuario()
        if len(metas) == 0:
            self.__tela_orcamento.mostra_mensagem("ATENCAO: Não há metas")
            return
        codigo_meta = self.__tela_orcamento.seleciona_meta(metas)
        meta = self.pega_meta_por_codigo(codigo_meta)

        if meta is not None:
            meta_utilizada = self.verifica_meta_utilizada(meta.codigo)
            if meta_utilizada:
                self.__tela_orcamento.mostra_error_mensagem("ATENCAO: Essa meta já está sendo utilizada em aluns dos seus orçamentos. A partir de agora não poderá mais adiciona-lá, mas ela continuará existindo")
            self.__meta_dao.remove(meta.codigo)
            self.lista_metas()
        else:
            self.__tela_orcamento.mostra_mensagem("ATENCAO: Meta não existente")

    def verifica_meta_utilizada(self, codigo):
        for orcamento in self.__orcamento_dao.get_all():
            for meta in orcamento.metas:
                if meta.codigo == codigo:
                    return True
        return False

    def pega_metas_usuario(self):
        usuario_logado = self.__controlador_principal.controlador_usuarios.pega_codigo_usuario_logado()
        metas = []
        for meta in self.__meta_dao.get_all():
            if usuario_logado == meta.usuario.identificador():
                metas.append(meta)
        return metas

    def isfloat(self, input):
        try:
            float(input)
            return True
        except ValueError:
            return False
