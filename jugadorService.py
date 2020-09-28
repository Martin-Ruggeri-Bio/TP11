from repositorios import Repositorios
from jugador import Jugador


class JugadorService():

    def get_jugadorList(self):
        return Repositorios.jugadorList

    def add_jugador(self, jugador):
        lastKey = -1
        for i in Repositorios.jugadorList:
            lastKey = i
        jugadorkey = lastKey + 1
        if jugadorkey > 1:
            raise ValueError("no se puede crear mas de dos jugadores")
        Repositorios.jugadorList[jugadorkey] = jugador.__dict__
        return jugadorkey

    def delete_jugador(self, key):
        lastKey = -1
        for i in Repositorios.jugadorList:
            lastKey = i
        if key > lastKey:
            raise ValueError("no se puede eliminar si el id no existe")
        del Repositorios.jugadorList[key]


'''jugador = Jugador('Martin', 2)
jugador2 = Jugador('Juan', 2)
jugador3 = Jugador('pepe', 2)
jugadorKey = JugadorService().add_jugador(jugador)
jugadorKey2 = JugadorService().add_jugador(jugador2)
jugadorKey3 = JugadorService().add_jugador(jugador3)
print(jugadorKey)
print(jugadorKey2)
print(jugadorKey3)'''