from partida import Partida
from repositorios import Repositorios
from random import choice


class ServicesPartidas():
    def iniciar_partida(self, nombre_jugador, dificultad, nombre_palabra,
                        tipo_palabra):
        if dificultad < 1 or dificultad > 10:
            raise ValueError("no puede ser menor a 1 o mayor a 10")
        if nombre_palabra == "" and tipo_palabra == "":
            listado = list(Repositorios.palabraList2)
            tipo_palabra = choice(listado)
            listado = list(Repositorios.palabraList2[tipo_palabra])
            nombre_palabra = choice(listado)
        intentos = len(nombre_palabra) * dificultad
        return Partida(nombre_palabra, intentos, tipo_palabra, nombre_jugador)

    def get_random_palabra(self):
        listado = list(Repositorios.palabraList2)
        tipo_palabra = choice(listado)
        listado = list(Repositorios.palabraList2[tipo_palabra])
        nombre_palabra = choice(listado)
        return {'palabra': nombre_palabra, 'tipo_palabra': tipo_palabra}

    def intentar_letra(self, partida, letra):
        if partida == Repositorios.partida_anterior:
            raise ValueError("no puede ingresar mas letras para esa palabra")
        Repositorios.intentos += 1
        if letra in partida._palabra:
            Repositorios.aciertos += 1
            if Repositorios.aciertos == len(partida._palabra):
                Repositorios.intentos = 0
                Repositorios.aciertos = 0
                Repositorios.partida_anterior = partida
                return 'Gano'
        if Repositorios.intentos == partida._intentos:
            Repositorios.intentos = 0
            Repositorios.aciertos = 0
            Repositorios.partida_anterior = partida
            return 'Perdio'
        return 'Continua'
