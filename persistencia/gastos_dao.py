from entidade.gasto import Gasto
from persistencia.dao import DAO

class GastoDAO(DAO):
    def __init__(self):
        super().__init__('gastos.pkl')

    def add(self, gasto: Gasto):
        if isinstance(gasto.codigo, int) and gasto is not None and isinstance(gasto, Gasto):
            super().add(gasto.codigo, gasto)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
