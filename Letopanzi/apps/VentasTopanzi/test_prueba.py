import unittest
from prueba import validarUsuario,validarGrupo

class testProbar(unittest.TestCase):
    def test_usuario(self):
        self.assertAlmostEqual(validarUsuario('admin','admin'),True)
        self.assertAlmostEqual(validarUsuario('admin','asdasd'),True)
        self.assertAlmostEqual(validarUsuario('asdasd','adasdasmin'),True)

class testProbar2(unittest.TestCase):
    def test_grupo(self):
        self.assertAlmostEqual(validarGrupo('clientes'),True)
        self.assertAlmostEqual(validarGrupo('asdasd'),True)
        self.assertAlmostEqual(validarGrupo('asdasd'),False)
