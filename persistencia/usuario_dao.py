from persistencia.dao import DAO
from entidade.usuario import Usuario


class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__('usuarios.pkl')

    def add(self, codigo: int, usuario: Usuario):
        super().add(codigo, usuario)

    def remove(self, codigo: int):
        super().remove(codigo)

    def get_all(self):
        return super().get_all()

    def update(self, codigo, obj):
        super().update(codigo, obj)