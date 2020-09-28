import unittest
from palabra import Palabra
from parameterized import parameterized
from palabraService import PalabraService
from repositorios import Repositorios


class TestPalabra(unittest.TestCase):

    def test_constructor_con_valores_iniciales(self):
        palabra = Palabra("Lenovo 450", 'computadoras')
        self.assertDictEqual(palabra.__dict__, {'_nombre': 'Lenovo 450',
                                                 '_tipo': 'computadoras'})

    @parameterized.expand([
            ("", 'computadoras'),
            ('mac', "")
        ])
    def test_Validate(self, nombre, tipo):
        with self.assertRaises(ValueError):
            Palabra(nombre, tipo)

    @parameterized.expand([
            ("lenovo t490", 'computadoras'),
            ("samsung s10", 'celular'),
            ("samsung s20", 'celular'),
            ("acer", 'computadoras'),
            ("HP", 'computadoras'),
        ])

    def test_add_palabra(self, nombre, tipo):
        palabra = Palabra(nombre, tipo)
        palabraKey = PalabraService().add_palabra(palabra)
        self.assertDictEqual(Repositorios.palabraList[palabraKey],
                             palabra. __dict__)

    def test_delete_palabra(self):
        palabra = Palabra("HP", "PC")
        palabraKey = PalabraService().add_palabra(palabra)
        PalabraService().delete_palabra(palabraKey)
        self.assertEqual(Repositorios.palabraList.get(palabraKey), None)

    def test_delete_palabra_value_error(self):
        long_list = len(Repositorios.palabraList)
        with self.assertRaises(ValueError):
            PalabraService().delete_palabra(long_list+1)


if __name__ == '__main__':
    unittest.main()
