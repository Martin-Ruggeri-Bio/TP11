from repositorios import Repositorios


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

    def listarDisponibles(self):
        j = 0
        listado = {}
        for key in Repositorios.palabraList:
            if Repositorios.palabraList[key]['_estado'] == 'disponible':
                listado[j] = Repositorios.palabraList[key]
                j = j + 1
        return listado
