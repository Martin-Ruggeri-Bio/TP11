from servicesPartidas import ServicesPartidas
from repositorios import Repositorios


class Ahorcado():
    def un_jugador(self):
        nombre_jugador, dificultad = Ahorcado().jugador()
        partida = ServicesPartidas().iniciar_partida(nombre_jugador,
                                                     dificultad)
        juego = Ahorcado().letras_de_jugador(0, partida)
        return juego

    def dos_jugadores(self):
        partida = Ahorcado().partida_de_uno_de_los_jugadores()
        juego1 = Ahorcado().letras_de_jugador(0, partida)
        partida = Ahorcado().partida_de_uno_de_los_jugadores()
        juego2 = Ahorcado().letras_de_jugador(1, partida)
        if juego1 and juego2:
            return True

    def jugador(self):
        nombre_jugador = input("Ingrese nombre de jugador:\n")
        dificultad = input("Ingrese dificultad de jugador:\n")
        return nombre_jugador, dificultad

    def partida_de_uno_de_los_jugadores(self):
        nombre_jugador, dificultad = Ahorcado().jugador()
        palabra_adivinar = input("Ingrese palabra:\n")
        tipo_palabra_adivinar = input("Ingrese tipo de palabra\n")
        partida = ServicesPartidas().iniciar_partida(
            nombre_jugador, dificultad,
            palabra_adivinar, tipo_palabra_adivinar)
        return partida

    def letras_de_jugador(self, nro_jugador, partida):
        juego = 'Continua'
        while juego == 'Continua':
            letra = input("ingrese una letra jugador:\n")
            if letra == 'salir' or letra == '3':
                break
            juego = ServicesPartidas().intentar_letra(partida, letra)
            Repositorios().historial[nro_jugador] = {partida: [letra, juego]}
        return True
