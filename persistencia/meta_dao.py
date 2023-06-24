from persistencia.dao import DAO
from entidade.meta import Meta


class MetaDAO(DAO):
    def __init__(self):
        super().__init__('metas.pkl')

    def add(self, meta: Meta):
        if isinstance(meta.codigo, int) and meta is not None and isinstance(meta, Meta):
            super().add(meta.codigo, meta)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
