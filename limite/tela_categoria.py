from controle.controlador_categoria import ControladorCategoria


class TelaCategoria:
    def __init__(self, controlador_categoria: ControladorCategoria):
        self.__controlador_categoria = controlador_categoria

    def tela_opcoes(self):
        print("\n------ Opções de Categoria ------")
        print("1 - Adicionar categoria")
        print("2 - Listar categoria")
        print("0 - Voltar")
        opcao = int(input("Escolha a opção desejada: "))
        return opcao

    def pega_dados_categoria(self):
        print("-------- ADICIONAR NOVA CATEGORIA --------")
        nome = input("Digite o nome da categoria: ")
        descricao = input("Digite a descrição da categoria: ")
        return {"nome": nome, "descricao": descricao}

    def mostra_categoria(self, dados_categoria):
        print("-------- INFORMAÇÕES DA CATEGORIA --------")
        print("Código:", dados_categoria["codigo"])
        print("Nome:", dados_categoria["nome"])
        print("Descrição:", dados_categoria["descricao"])

    def seleciona_categoria(self, categorias):
        pass

    def mostra_mensagem(self, mensagem):
        print(mensagem)
