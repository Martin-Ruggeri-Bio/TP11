from jugadorService import JugadorService
from palabraService import PalabraService
from jugador import Jugador
from palabra import Palabra


class App_ahorcado():
    def menu_jugadores(self):
        print("\n\n\tMENU - Ahorcado")
        print("\tElija cantidad de jugadores, 1 o 2")
        print("\tSalir (otra tecla)")
        return int(input("\n\tElija una opción: "))

if __name__ == '__main__':
    jugadorService = jugadorService()
    while True:
        opcion_jugador = App_ahorcado().menu_jugadores()
        if opcion_jugador == 1:
            print("\nEligio jugar contra la maquina\n")
            jugador1 = JugadorService().add_jugador(
                Jugador(input("\nIngrese su nombre\n"),
                        input("\nIngrese su dificultad\n")))
            print("\nla maquina elege una palabra")

        if opcion_jugador == 2:
            print("\nEligio jugar contra un amigo\n")
            jugador1 = JugadorService().add_jugador(
                Jugador(input("\nIngrese su nombre\n"),
                        input("\nIngrese su dificultad\n")))
            jugador2 = JugadorService().add_jugador(
                Jugador(input("\nIngrese su nombre\n"),
                        input("\nIngrese su dificultad\n")))
        if opcion_jugador < 1 or opcion_jugador > 2:
            break
    