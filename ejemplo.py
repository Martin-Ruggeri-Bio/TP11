from repositorios import Repositorios


def guiaPalabra(palabra_elegida=""):
    for i in palabra_elegida:
        Repositorios.palabraGuia.append("__ ")
    palabra = Repositorios.palabraGuia
    return palabra

print(guiaPalabra("torta"))

def check_letras(letra):
    letraEncontrada = False
    indices = []
    for i in range(len(Repositorios.palabraElegida)):
        if letra == Repositorios.palabraElegida[i]:
            indices.append(i)
            letraEncontrada = True
    return indices

print(check_letras("t"))

def add_letras(letra, posicion):
    for i in posicion:
        Repositorios.palabraGuia[i] = letra
    palabra = Repositorios.palabraGuia
    return palabra

print(add_letras("t", [0, 3]))