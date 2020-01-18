import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from banco.correntista import Correntista

class TestCorrentista(unittest.TestCase):

    def setUp(self):
        self.__correntista = Correntista('Elias', '12345678901', 10.0)

    def test_atributos(self):
        self.assertEqual(self.__correntista.nome(),'Elias')
        self.assertEqual(self.__correntista.cpf(),'12345678901')
        self.assertEqual(self.__correntista.saldo(),10.0)
 
    def test_depositar(self):
        self.__correntista.depositar(10.0)
        self.assertEqual(self.__correntista.saldo(),20.0)

    def test_depositar_erros(self):
        with self.assertRaises(ValueError):
            self.__correntista.depositar(0.0)
        with self.assertRaises(ValueError):
            self.__correntista.depositar(-10.0)
        with self.assertRaises(TypeError):
            self.__correntista.depositar("a")    

    def test_sacar(self):
        self.__correntista.sacar(10.0)
        self.assertEqual(self.__correntista.saldo(),0.0)

    def test_sacar_erros(self):
        with self.assertRaises(ValueError):
            self.__correntista.sacar(0.0)
        with self.assertRaises(ValueError):
            self.__correntista.sacar(-10.0)
        with self.assertRaises(TypeError):
            self.__correntista.sacar("a") 

    def test_sacar_nao_permitido(self):
        with self.assertRaises(ValueError):
            self.__correntista.sacar(50.0)

    def test_auditoria(self):
        self.__correntista.sacar(10.0)
        self.__correntista.depositar(20.0)
        self.assertEqual(len(self.__correntista.auditoria()), 3)

if __name__ == '__main__':
    unittest.main()