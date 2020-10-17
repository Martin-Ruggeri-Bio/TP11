from partida import Partida
from repositorios import Repositorios
from random import choice


class ServicesPartidas():
    def iniciar_partida(self, nombre_jugador, dificultad, nombre_palabra="",
                        tipo_palabra=""):
        if int(dificultad) < 1 or int(dificultad) > 10:
            raise ValueError("no puede ser menor a 1 o mayor a 10")
        if nombre_palabra == "" and tipo_palabra == "":
            palabra_dict = ServicesPartidas().get_random_palabra()
            nombre_palabra = palabra_dict['palabra']
            tipo_palabra = palabra_dict['tipo_palabra']
        intentos = len(nombre_palabra) * int(dificultad)
        partida = Partida(nombre_palabra, intentos,
                          tipo_palabra, nombre_jugador)
        return partida

    def get_random_palabra(self):
        listado = list(Repositorios.palabraList2)
        tipo_palabra = choice(listado)
        listado = list(Repositorios.palabraList2[tipo_palabra])
        nombre_palabra = choice(listado)
        palabra_dict = {'palabra': nombre_palabra, 'tipo_palabra': tipo_palabra}
        return palabra_dict

    def intentar_letra(self, partida, letra):
        if partida == Repositorios.partida_anterior:
            raise ValueError("no puede ingresar mas letras para esa palabra")
        Repositorios.intentos += 1
        if letra in partida._palabra:
            Repositorios.aciertos += 1
            if Repositorios.aciertos == len(partida._palabra):
                ServicesPartidas().guardar_intentos(partida)
                return 'Gano'
        if Repositorios.intentos == partida._intentos:
            ServicesPartidas().guardar_intentos(partida)
            return 'Perdio'
        return 'Continua'

    def guardar_intentos(self, partida):
        Repositorios.intentos = 0
        Repositorios.aciertos = 0
        Repositorios.partida_anterior = partida
