from repositorios import Repositorios


class Adivinanza():

    def guiaPalabra(self, palabra_elegida=""):
        palabraGuia = []
        for i in palabra_elegida:
            palabraGuia.append("__ ")
        return palabraGuia

    def check_letras(self, letra):
        indices = []
        for i in range(len(Repositorios.palabraElegida)):
            if letra == Repositorios.palabraElegida[i]:
                indices.append(i)
        return indices

    def add_letras(self, letra, posicion, guia):
        for i in posicion:
            guia[i] = letra
        return guia
