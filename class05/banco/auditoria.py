'''
    Classe Auditoria
'''
import time;
class Auditoria:
    def __init__(self, cpf, data_hora, valor, tipo):
        self.__cpf = cpf
        self.__data_hora = data_hora
        self.__valor = valor
        self.__tipo = tipo

    def cpf(self):
        return self.__cpf

    def data_hora(self):
        return self.__data_hora

    def valor(self):
        return self.__valor

    def tipo(self):
        return self.__tipo

    def __str__(self):
        '''
        Imprime o registro de auditoria
        Parameters:
        -
        Returns: 
        string: dados da conta
        '''
        return f"CPF: {self.__cpf}\n Data/Hora: {self.__data_hora}\n Valor R$ {self.__valor}\n Tipo {self.__tipo}"