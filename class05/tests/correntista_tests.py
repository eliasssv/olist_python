import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from banco.correntista import Correntista
from unittest.mock import Mock

class TestCorrentista(unittest.TestCase):

    def setUp(self):
        auditoria = Mock()
        self.__correntista = Correntista('Elias', '12345678901', 10.0, auditoria)

    def test_atributos(self):
        self.assertEqual(self.__correntista.nome(),'Elias')
        self.assertEqual(self.__correntista.cpf(),'12345678901')
        self.assertEqual(self.__correntista.saldo(),10.0)
 
    def test_depositar(self):
        auditoria = Mock()
        self.__correntista.depositar(10.0, auditoria)
        self.assertEqual(self.__correntista.saldo(),20.0)
        auditoria.salvar_auditoria.assert_called_with(self.__correntista.cpf(), 'D', 10.0)

    def test_depositar_erros(self):
        auditoria = Mock()
        with self.assertRaises(ValueError):
            self.__correntista.depositar(0.0, auditoria)
        with self.assertRaises(ValueError):
            self.__correntista.depositar(-10.0, auditoria)
        with self.assertRaises(TypeError):
            self.__correntista.depositar("a", auditoria)    

        auditoria.salvar_auditoria.assert_not_called()

    def test_sacar(self):
        auditoria = Mock()

        self.__correntista.sacar(10.0, auditoria)
        self.assertEqual(self.__correntista.saldo(),0.0)

        auditoria.salvar_auditoria.assert_called_with(self.__correntista.cpf(), 'S', 10.0)

    def test_sacar_erros(self):
        auditoria = Mock()

        with self.assertRaises(ValueError):
            self.__correntista.sacar(0.0, auditoria)
        with self.assertRaises(ValueError):
            self.__correntista.sacar(-10.0, auditoria)
        with self.assertRaises(TypeError):
            self.__correntista.sacar("a", auditoria) 

        auditoria.salvar_auditoria.assert_not_called()

    def test_sacar_nao_permitido(self):
        auditoria = Mock()

        with self.assertRaises(ValueError):
            self.__correntista.sacar(50.0, auditoria)

        auditoria.salvar_auditoria.assert_not_called()

if __name__ == '__main__':
    unittest.main()