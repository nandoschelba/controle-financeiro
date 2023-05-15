class TelaOrcamento:

    def tela_opcoes(self):
        opcoes_validas = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        print("-------- ORCAMENTOS ----------")
        print("Escolha a opcao")
        print("1 - Listar Orçamentos")
        print("2 - Adicionar novo orçamento")
        print("3 - Deletar orçamento")
        print("4 - Atualizar orçamento")
        print("5 - Adicionar nova meta")
        print("6 - Deletar meta")
        print("7 - Atualizar meta")
        print("8 - Emitir relatorio")
        print("0 - Retornar")

        opcao = input("Escolha a opção desejada: ")
        if not opcao.isdigit():
            return
        if int(opcao) not in opcoes_validas:
            return
        return int(opcao)

    def pega_dados_orcaento(self):
        print("-------- DADOS GERAIS DO ORCAMENTO ----------")
        mes = input("Mes: ")
        ano = input("Ano: ")

        return {"mes": mes, "ano": ano}

    def pega_dados_meta(self):
        print("-------- DADOS DO META ----------")
        meta = input("meta: ")
        descricao = input("descricao: ")

        return {"meta": meta, "descricao": descricao}

    def pega_dados_relario(self):
        print("-------- DADOS DO RELATÓRIO ----------")
        mes = input("MES: ")
        ano = input("ANO: ")

        return {"mes": mes, "ano": ano}

    def pega_add_novo(self):
        adicionar_meta = input("Adicionar mais uma meta?(s/n) ")

        return {"adicionar_meta": adicionar_meta}

    def mostra_orcamento(self, orcamento):
        print("VALOR DISPONÍVEL: ", orcamento["valor_disponivel"])
        print("DATA: ", orcamento["mes"] + "/" + orcamento["ano"])
        print("METAS: ")
        print("\n")

    def mostra_meta(self, meta):
        print("CODIGO: ", meta["codigo"])
        print("VALOR DA META: ", meta["meta"])
        print("CATEGORIA: ", meta["categoria"])

        print("\n")

    def mostra_relatorio(self, item_categoria):
        print("DATA: ", item_categoria["mes"] + "/" + item_categoria["ano"])
        print("CATEGORIA: ", item_categoria["categoria"])
        print("VALOR DA META: ", item_categoria["meta"])
        print("VALOR GASTO: ", item_categoria["gasto"])

        print("\n")

    def seleciona_orcamento(self):
        codigo = input("Código do orçamento que deseja selecionar: ")
        return codigo

    def seleciona_meta(self):
        codigo = input("Código da meta que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, mensagem):
        print(mensagem)