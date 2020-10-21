from ahorcado import Ahorcado
from repositorios import Repositorios


class App_ahorcado():
    def menu_jugadores(self):
        print("\n\n\tMENU - Ahorcado")
        print("\tElija cantidad de jugadores, 1 o 2")
        print("\tsalir (otra tecla)")
        return int(input("\n\tElija una opción: "))


if __name__ == '__main__':
    juego = Ahorcado()
    while True:
        opcion_jugador = App_ahorcado().menu_jugadores()
        if opcion_jugador == 1:
            print("\nEligio jugar contra la maquina\n")
            juego.un_jugador()
            print(Repositorios().historial[0])
        elif opcion_jugador == 2:
            print("\nEligio jugar contra un amigo\n")
            juego.dos_jugadores()
            print(Repositorios().historial[0])
            print(Repositorios().historial[1])
        if opcion_jugador == 'salir':
            print(Repositorios().historial[0])
            print(Repositorios().historial[1])
            exit
        else:
            exit
