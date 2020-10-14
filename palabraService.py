from repositorios import Repositorios
from random import choice

class PalabraService():
    def get_palabraList(self):
        return Repositorios.palabraList

    def add_palabra(self, palabra):
        lastKey=-1
        for i in Repositorios.palabraList:
            lastKey = i
        palabrakey = lastKey + 1
        Repositorios.palabraList[palabrakey] = palabra.__dict__
        return palabrakey

    def delete_palabra(self, key):
        lastKey = -1
        for i in Repositorios.palabraList:
            lastKey = i
        if key > lastKey:
            raise ValueError("no se puede eliminar si el id no existe")
        del Repositorios.palabraList[key]

    def eleccion_de_maquina(self):
        listado = list(Repositorios.palabraList2)
        tipo_palabra = choice(listado)
        listado = list(Repositorios.palabraList2[tipo_palabra])
        palabra = choice(listado)
        return palabra, tipo_palabra
