from entidade.orcamento import Orcamento
from persistencia.dao import DAO

class OrcamentoDAO(DAO):
    def __init__(self):
        super().__init__('orcamentos.pkl')

    def add(self, orcamento: Orcamento):
        if isinstance(orcamento.codigo, int) and orcamento is not None and isinstance(orcamento, Orcamento):
            super().add(orcamento.codigo, orcamento)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
