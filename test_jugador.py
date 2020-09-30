import unittest
from jugador import Jugador
from parameterized import parameterized
from jugadorService import JugadorService
from repositorios import Repositorios


class TestJugador(unittest.TestCase):
    def setUp(self):
        Repositorios.jugadorList = {}

    def test_constructor_con_valores_iniciales(self):
        jugador = Jugador('Martin', 3)
        self.assertDictEqual(jugador.__dict__, {'_nombre': 'Martin',
                                                '_dificultad': 3})

    @parameterized.expand([
        ("", 2),
        ("Martin", -3),
        ('Juan', 4),
    ])
    def test_Validate_vacio_y_valor_incorrecto(self, nombre, dificultad):
        with self.assertRaises(ValueError):
            Jugador(nombre, dificultad)

    @parameterized.expand([
            ('Martin', 2),
            ('Juan', 2)
        ])
    def test_add_jugador(self, nombre, dificultad):
        jugador = Jugador(nombre, dificultad)
        jugadorKey = JugadorService().add_jugador(jugador)
        self.assertDictEqual(Repositorios.jugadorList[jugadorKey],
                             jugador. __dict__)

    @parameterized.expand([
            ('Martin', 2, 'Juan', 2, 'pedro', 2)
        ])
    def test_Validate_cant_jugadores(self, nombre1, dificultad1, nombre2,\
                                     dificultad2, nombre3, dificultad3):
        jugador1 = Jugador(nombre1, dificultad1)
        jugador2 = Jugador(nombre2, dificultad2)
        jugador3 = Jugador(nombre3, dificultad3)
        JugadorService().add_jugador(jugador1)
        JugadorService().add_jugador(jugador2)
        with self.assertRaises(ValueError):
            JugadorService().add_jugador(jugador3)

    def test_delete_jugador(self):
        jugador = Jugador("pedro", 3)
        jugadorKey = JugadorService().add_jugador(jugador)
        JugadorService().delete_jugador(jugadorKey)
        self.assertEqual(Repositorios.jugadorList.get(jugadorKey), None)

    def test_delete_jugador_value_error(self):
        long_list = len(Repositorios.jugadorList)
        with self.assertRaises(ValueError):
            JugadorService().delete_jugador(long_list+1)


if __name__ == '__main__':
    unittest.main()
