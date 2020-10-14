from palabraService import PalabraService
from repositorios import Repositorios
from random import choice


listado = list(Repositorios.palabraList2)
tipo_palabra = choice(listado)
listado = list(Repositorios.palabraList2[tipo_palabra])
palabra = choice(listado)

print(tipo_palabra)
print(palabra)
intentos = 5 
while intentos > 0:
    intentos -= 1
    print(intentos)
print(len(['pato', 'casa', 'perro']))



Repositorios.intentos += 1
if letra in partida._palabra:
    Repositorios.aciertos += 1
    if Repositorios.aciertos == len(partida._palabra):
        Repositorios.intentos = 0
        Repositorios.aciertos = 0
        return 'Gano'
if Repositorios.intentos == partida._intentos:
    Repositorios.intentos = 0
    Repositorios.aciertos = 0
    return 'Perdio'
return 'Continua'


def intentar_letra(self, partida, letra):
        if Repositorios.intentos == 0:
            Repositorios.intentos == partida._intentos
        Repositorios.intentos -= 1
        if letra in partida._palabra:
            Repositorios.aciertos += 1
            if Repositorios.aciertos == len(partida._palabra):
                Repositorios.intentos = 0
                Repositorios.aciertos = 0
                return 'Gano'
        if Repositorios.intentos == 0:
            Repositorios.aciertos = 0
            return 'Perdio'
        return 'Continua'