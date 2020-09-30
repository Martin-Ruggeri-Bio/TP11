from repositorios import Repositorios


class Adivinanza():

    def guiaPalabra(self, palabra_elegida=""):
        for i in palabra_elegida:
            Repositorios.palabraGuia.append("__ ")
        palabra = Repositorios.palabraGuia
        return palabra

    def check_letras(self, letra):
        indices = []
        for i in range(len(Repositorios.palabraElegida)):
            if letra == Repositorios.palabraElegida[i]:
                indices.append(i)
        return indices

    def add_letras(self, letra, posicion):
        for i in posicion:
            Repositorios.palabraGuia[i] = letra
        palabra = Repositorios.palabraGuia
        return palabra
