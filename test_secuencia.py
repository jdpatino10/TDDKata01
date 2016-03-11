from unittest import TestCase

from Secuencia import Secuencia


class TestSecuencia(TestCase):
    def test_cadenaVacia(self):
        self.assertEqual(Secuencia().verificarSecuencia(""), 0, "Cadena vacia")
