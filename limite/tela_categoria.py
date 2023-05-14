from controle.controlador_categoria import ControladorCategoria

class TelaCategoria:
    def __init__(self, controlador_categoria: ControladorCategoria):
        self.__controlador_categoria = controlador_categoria

    def tela_opcoes(self):
        print("\n------ Opções de Categoria ------")
        print("1 - Adicionar categoria")
        print("2 - Listar categoria")
        print("3 - Editar categoria")
        print("4 - Excluir categoria")
        print("0 - Voltar")
        opcao = int(input("Escolha a opção desejada: "))
        return opcao

    def pega_dados_categoria(self):
        nome = input("\nDigite o nome da categoria: ")
        descricao = input("Digite a descrição da categoria: ")
        return {"nome": nome, "descricao": descricao}

    def mostra_categoria(self, dados_categoria):
        print("\n----------------------")
        print("Código:", dados_categoria.codigo)
        print("Nome:", dados_categoria.nome)
        print("Descrição:", dados_categoria.descricao)

    def pega_codigo_categoria_edicao(self):
        codigo = input("\nInsira o ID da categoria que você quer editar: ")
        if not isinstance(codigo, int):
            try:
                codigo = int(codigo)
            except ValueError:
                raise TypeError("O código deve ser um número inteiro.")
        return codigo

    def pega_codigo_categoria_excluir(self):
        codigo = input("\nInsira o ID da categoria que você quer excluir: ")
        if not isinstance(codigo, int):
            try:
                codigo = int(codigo)
            except ValueError:
                raise TypeError("O código deve ser um número inteiro.")
        return codigo

    def pega_novos_dados_categoria(self, categoria_selecionada):
        print("\n------ Categoria selecionada ------")
        print("Código:", categoria_selecionada.codigo)
        print("Nome:", categoria_selecionada.nome)
        print("Descrição:", categoria_selecionada.descricao)
        while True:
            nome = input("\nNovo nome da categoria: ")
            descricao = input("Nova descricao: ")
            if nome == "" or descricao == "":
                print("\nNome e descricao não podem ser vazios.")
            else:
                return {"nome": nome, "descricao": descricao, "codigo": categoria_selecionada.codigo}


    def mostra_mensagem(self, mensagem: str):
        print(mensagem)
