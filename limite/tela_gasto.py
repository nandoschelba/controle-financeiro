class TelaGasto:

    def tela_opcoes(self):
        opcoes_validas = [0, 1, 2, 3, 4, 5]
        print("-------- GASTOS ----------")
        print("Escolha a opcao")
        print("1 - Listar Gastos")
        print("2 - Adicionar novo gasto")
        print("3 - Deletar gasto")
        print("4 - Atualizar gasto")
        print("5 - Emite relatorio")
        print("0 - Retornar")

        opcao = input("Escolha a opção desejada: ")
        if not opcao.isdigit():
            return
        if int(opcao) not in opcoes_validas:
            return
        return int(opcao)

    def pega_dados_gasto(self):
        print("-------- DADOS GERAIS DO GASTO ----------")
        estabelecimento = input("Estabelecimento: ")
        mes = input("Mes: ")
        ano = input("Ano: ")

        return {"estabelecimento": estabelecimento, "mes": mes, "ano": ano}

    def pega_dados_item(self):
        print("-------- DADOS DO ITEM ----------")
        valor = input("Valor: ")
        descricao = input("descricao: ")

        return {"valor": valor, "descricao": descricao}

    def pega_dados_relario(self):
        print("-------- DADOS DO RELATÓRIO ----------")
        mes = input("MES: ")
        ano = input("ANO: ")

        return {"mes": mes, "ano": ano}

    def pega_add_novo(self):
        adicionar_item = input("Adicionar mais um item?(s/n) ")

        return {"adicionar_item": adicionar_item}

    def mostra_gasto(self, gasto):
        print("CÓDIGO: ", gasto["codigo"])
        print("NOME DO ESTABELECIMENTO: ", gasto["estabelecimento"])
        print("DATA: ", str(gasto["mes"]) + "/" + str(gasto["ano"]))
        print("ITENS: ")
        print("\n")

    def mostra_item(self, item):
        print("DESCRICAO: ", item["descricao"])
        print("VALOR: ", item["valor"])
        print("\n")

    def seleciona_gasto(self):
        codigo = input("Código do gasto que deseja selecionar: ")
        return codigo

    def seleciona_item(self):
        codigo = input("Código do item que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, mensagem):
        print(mensagem)