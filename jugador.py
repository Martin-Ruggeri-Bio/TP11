class Jugador():
    
    def __init__(self, nombre="", dificultad=3):
        self.nombre = nombre
        self.dificultad = dificultad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if value == "":
            raise ValueError("no puede ser vacio")
        self._nombre = value

    @property
    def dificultad(self):
        return self._dificultad

    @dificultad.setter
    def dificultad(self, value):
        if value < 0 or value > 3:
            raise ValueError("no puede ser negativo o mayor a 3")
        self._dificultad = value
