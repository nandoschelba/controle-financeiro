class TelaOrcamento:

    def tela_opcoes(self):
        print("-------- ORCAMENTOS ----------")
        print("Escolha a opcao")
        print("1 - Listar Orçamentos")
        print("2 - Adicionar novo orçamento")
        print("3 - Deletar orçamento")
        print("4 - Atualizar orçamento")
        print("5 - Adicionar nova meta")
        print("6 - Deletar meta")
        print("7 - Atualizar meta")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao
    # code to display the main menu options for managing expenses

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
        print("DESCRICAO: ", meta["descricao"])
        print("CATEGORIA: ", meta["categoria"])

        print("\n")

    def seleciona_orcamento(self):
        codigo = input("Código do orçamento que deseja selecionar: ")
        return codigo

    def seleciona_meta(self):
        codigo = input("Código da meta que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, mensagem):
        print(mensagem)