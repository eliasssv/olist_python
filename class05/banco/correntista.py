'''
    Classe Correntista
'''
import time;

class Correntista:
    def __init__(self, nome, cpf, saldo, auditoria):
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = saldo
        auditoria.salvar_auditoria(self, cpf, 'D', saldo)

    def nome(self):
        return self.__nome

    def cpf(self):
        return self.__cpf

    def saldo(self):
        return self.__saldo
    
    def depositar(self, valor, auditoria):
        '''
        Faz um depósito na Conta
        Parameters:
        valor (float): Valor a ser depositado
        Returns: 
        string: mensagem
        '''
        if (not isinstance(valor, float)):
            raise TypeError("Valor inválido")

        if (valor <= 0):
            raise ValueError("O valor deve ser maior que ZERO! Depósito não efetuado")
        else:   
            self.__saldo += valor
            auditoria.salvar_auditoria(self.__cpf, 'D', valor)
            return f"Depósito de {valor} efetuado com sucesso. Saldo: R$ {self.__saldo}"

    def sacar(self, valor, auditoria):
        '''
        Faz um saque na Conta
        Parameters:
        valor (float): Valor a ser sacado
        Returns: 
        string: mensagem
        '''
        if (not isinstance(valor, float)):
            raise TypeError("Valor inválido")
        if (valor <= 0):
            raise ValueError("O valor deve ser maior que ZERO! Saque não efetuado")
        elif (valor > self.__saldo):
            raise ValueError(f"O valor do saque deve ser menor ou igual ao saldo (R$ {self.__saldo})! Saque não efetuado")
        else:
            self.__saldo -= valor  
            auditoria.salvar_auditoria(self.__cpf, 'S', valor)
            return f"Saque de {valor} efetuado com sucesso. Saldo: R$ {self.__saldo}"  



    def __str__(self):
        '''
        Retorna os dados da conta
        Parameters:
        -
        Returns: 
        string: dados da conta
        '''
        return f"Correntista: {self.__nome} - CPF: {self.__cpf}\nSaldo R$ {self.__saldo}"

    def __iter__(self):
        return self

    def __next__(self):
        if (self.__idx == 0): 
            raise StopIteration
       
        self._idx -= 1
        ret = self.__auditoria[self.__idx]
        return ret  

