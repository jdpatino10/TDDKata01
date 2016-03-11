from unittest import TestCase

from Secuencia import Secuencia


class TestSecuencia(TestCase):
    def test_cadenaVacia(self):
        self.assertEqual(Secuencia().verificarSecuencia("")[0], 0, "Cadena vacia")

    def test_conUnNumero(self):
        self.assertEqual(Secuencia().verificarSecuencia("2")[0], 1, "Con un numero")

    def test_conDosNumeros(self):
        self.assertEqual(Secuencia().verificarSecuencia("2,4")[0], 2, "Con dos numeros")

    def test_conNNumeros(self):
        self.assertEqual(Secuencia().verificarSecuencia("2,4,4,3,2,1")[0], 6, "Con N numeros")

    def test_Iteracion2cadenaVacia(self):
        self.assertEqual(Secuencia().verificarSecuencia("")[0], 0, "Cadena vacia")
        self.assertEqual(Secuencia().verificarSecuencia("")[1], 0, "Cadena vacia")

    def test_Iteracion2conUnNumero(self):
        self.assertEqual(Secuencia().verificarSecuencia("2")[0], 1, "Con un numero")
        self.assertEqual(Secuencia().verificarSecuencia("2")[1], 2, "Con un numero")