import unittest
from parameterized import parameterized
from adivinanza import Adivinanza
from repositorios import Repositorios


class TestAdivinanza(unittest.TestCase):
    def test_guiaPalabra(self,):
        self.assertEqual(Adivinanza().guiaPalabra("pato"), ['__ ', '__ ', '__ ', '__ '])
    
    @parameterized.expand([
        ("t", [0, 3] ),
        ("o", [1]),
        ("a", [4]),
    ])
    def test_check_letras(self, letra, indice):
        self.assertEqual(Adivinanza().check_letras(letra), indice)

    @parameterized.expand([
        ("t", [0, 3], ["t", "__ ", "__ ", "t", "__ "]),
        ("o", [1], ["__ ", "o", "__ ", "__ ", "__ "]),
        ("a", [4], ["__ ", "__ ", "__ ", "__ ", "a"]),
    ])
    def test_add_letras(self, letra, posicion, guiaComleta):
        guia = Adivinanza().guiaPalabra("torta")
        self.assertEqual(Adivinanza().add_letras(letra, posicion, guia), guiaComleta)


if __name__ == '__main__':
    unittest.main()
