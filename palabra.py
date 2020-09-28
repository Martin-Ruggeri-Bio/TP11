class Palabra():

    def __init__(self, nombre="", tipo=""):
        self.nombre = nombre
        self.tipo = tipo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if value == "":
            raise ValueError("no puede ser vacio")
        self._nombre = value

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        if value == "":
            raise ValueError("no puede ser vacio")
        self._tipo = value
