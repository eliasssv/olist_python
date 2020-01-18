'''
    Classe Correntista
'''
import time;
class Correntista:
    def __init__(self, nome, cpf, saldo):
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = saldo
        self.__historico = [{'dataHora': time.time(), 'valor': saldo, 'tipo':'D'}]
        self.__idx = 0

    def depositar(self, valor):
        '''
        Faz um depósito na Conta
        Parameters:
        valor (float): Valor a ser depositado
        Returns: 
        string: mensagem
        '''
        try:
            if (valor <= 0):
                return "O valor deve ser maior que ZERO! Depósito não efetuado"
            else:   
                self.__saldo += valor
                self.__historico.append({'dataHora': time.time(), 'valor': valor, 'tipo':'D'})
                self.__idx = len(self.__historico)
                return f"Depósito de {valor} efetuado com sucesso. Saldo: R$ {self._saldo}"
        except ValueError:
            return f"Valor inválido!" 

    def sacar(self, valor):
        '''
        Faz um saque na Conta
        Parameters:
        valor (float): Valor a ser sacado
        Returns: 
        string: mensagem
        '''
        try:
            if (valor <= 0):
                raise ValueError("O valor deve ser maior que ZERO! Saque não efetuado")
            elif (valor > self.__saldo):
                raise ValueError(f"O valor do saque deve ser menor ou igual ao saldo (R$ {self.__saldo})! Saque não efetuado")
            else:
                self._saldo -= valor 
                self._historico.append({'dataHora': time.time(), 'valor': valor, 'tipo':'S'})  
                self._idx = len(self.__historico)
                return f"Saque de {valor} efetuado com sucesso. Saldo: R$ {self.__saldo}"  
        except TypeError:
            raise ValueError("Valor inválido!")

    def nome(self):
        return self.__nome

    def cpf(self):
        return self.__cpf

    def saldo(self):
        return self.__saldo


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
        ret = self.__historico[self.__idx]
        return ret  

