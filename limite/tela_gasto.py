class TelaGasto:
    def tela_opcoes(self):
        print("-------- AMIGOS ----------")
        print("Escolha a opcao")
        print("1 - Listar Gastos")
        print("2 - Adicionar novo gasto")
        print("3 - Deletar gasto")
        print("4 - Atualizar gasto")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao
    # code to display the main menu options for managing expenses

    def pega_dados_gasto(self):
        print("-------- DADOS GERAIS DO GASTO ----------")
        estabelecimento = input("Estabelecimento: ")
        mes = input("Mes: ")
        ano = input("Ano: ")
        desconto = input("Desconto: ")

        return {"estabelecimento": estabelecimento, "mes": mes, "ano": ano, "desconto": desconto }

    def pega_dados_item(self):
        print("-------- DADOS DO ITEM ----------")
        valor = input("Valor: ")
        descricao = input("descricao: ")

        return {"valor": valor, "descricao": descricao}

    def pega_add_novo(self):
        adicionar_item = input("Adicionar mais um item?(s/n) ")

        return {"add": adicionar_item}

    def mostra_gasto(self, gasto):
        ...
    # code to display the details of an expense

    def mostra_item(self, item):
        ...
    # code to display the details of an item

    def seleciona_gasto(self, gastos):
        ...
    # code to display a list of expenses and prompt the user to select one

    def mostra_mensagem(self, mensagem):
        print(mensagem)