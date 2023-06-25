import pickle
from abc import ABC


class DAO(ABC):
    def __init__(self, datasource: str):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def get(self, codigo):
        try:
            return self.__cache[codigo]
        except KeyError:
            pass

    def add(self, codigo, obj):
        self.__cache[codigo] = obj
        self.__dump()

    def remove(self, codigo):
        try:
            self.__cache.pop(codigo)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return self.__cache.values()

    def update(self, codigo, obj):
        self.__cache[codigo] = obj
        self.__dump()
