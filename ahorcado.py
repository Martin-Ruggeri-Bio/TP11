from servicesPartidas import ServicesPartidas
from repositorios import Repositorios


class Ahorcado():
    def un_jugador(self):
        nombre_jugador, dificultad = Ahorcado().jugador()
        partida = ServicesPartidas().iniciar_partida(nombre_jugador,
                                                     dificultad)
        guia_palabra = Ahorcado().guiaPalabra(partida._palabra)
        print(guia_palabra)
        juego = Ahorcado().letras_de_jugador(0, partida, guia_palabra)
        return juego

    def dos_jugadores(self):
        partida = Ahorcado().partida_de_uno_de_los_jugadores()
        guia_palabra = Ahorcado().guiaPalabra(partida._palabra)
        juego1 = Ahorcado().letras_de_jugador(0, partida, guia_palabra)
        partida = Ahorcado().partida_de_uno_de_los_jugadores()
        guia_palabra = Ahorcado().guiaPalabra(partida._palabra)
        juego2 = Ahorcado().letras_de_jugador(1, partida, guia_palabra)
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

    def letras_de_jugador(self, nro_jugador, partida, guia_palabra):
        juego = 'Continua'
        while juego == 'Continua':
            letra = input("ingrese una letra jugador:\n")
            if letra == 'salir' or letra == '3':
                break
            juego = ServicesPartidas().intentar_letra(partida, letra)
            completando_palabra = Ahorcado().add_letras(
                letra, partida._palabra, guia_palabra)
            Repositorios().historial[nro_jugador] = {partida: [letra, juego]}
            print(completando_palabra)
            print('cantidad de aciertos ' + str(Repositorios().aciertos))
            print('cantidad de intentos ' + str(Repositorios().intentos))
            print(juego)
        return True

    def guiaPalabra(self, palabra_elegida):
        guia_palabra = [' __ ' for i in palabra_elegida]
        return guia_palabra

    def add_letras(self, letra, palabra_elegida, guia_palabra):
        for i in range(len(palabra_elegida)):
            if guia_palabra[i] == ' __ ':
                if letra.upper() == palabra_elegida[i]:
                    guia_palabra[i] = letra
                    break
        return guia_palabra
