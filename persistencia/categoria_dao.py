from persistencia.dao import DAO
from entidade.categoria import Categoria


class CategoriaDAO(DAO):
    def __init__(self):
        super().__init__('categorias.pkl')

    def add(self, codigo: int, categoria: Categoria):
        super().add(codigo, categoria)

    def remove(self, codigo: int):
        super().remove(codigo)

    def get_all(self):
        return super().get_all()

    def get(self, codigo: int):
        return super().get(codigo)