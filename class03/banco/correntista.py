'''
    Classe Correntista
'''
import time;
class Correntista:
    def __init__(self, nome, saldo):
        self._nome = nome
        self._saldo = saldo
        self._historico = [{'dataHora': time.time(), 'valor': saldo, 'tipo':'D'}]
        self._idx = 0

    def depositar(self, valor):
        '''
        Faz um depósito na Conta
        Parameters:
        valor (float): Valor a ser depositado
        Returns: 
        string: mensagem
        '''
        if (valor <= 0):
            return "O valor deve ser maior que ZERO! Depósito não efetuado"
        else:
            self._saldo += valor
            self._historico.append({'dataHora': time.time(), 'valor': valor, 'tipo':'D'})
            self._idx = len(self._historico)
            return f"Depósito de {valor} efetuado com sucesso. Saldo: R$ {self._saldo}"

    def sacar(self, valor):
        '''
        Faz um saque na Conta
        Parameters:
        valor (float): Valor a ser sacado
        Returns: 
        string: mensagem
        '''
        if (valor <= 0):
            return "O valor deve ser maior que ZERO! Saque não efetuado"
        elif (valor > self._saldo):
            return f"O valor do saque deve ser menor ou igual ao saldo (R$ {self._saldo})! Saque não efetuado"
        else:
            self._saldo -= valor 
            self._historico.append({'dataHora': time.time(), 'valor': valor, 'tipo':'S'})  
            self._idx = len(self._historico)
            return f"Saque de {valor} efetuado com sucesso. Saldo: R$ {self._saldo}"   

    def nome(self):
        return self._nome

    def saldo(self):
        return self._saldo


    def __str__(self):
        '''
        Retorna os dados da conta
        Parameters:
        -
        Returns: 
        string: dados da conta
        '''
        return f"Correntista: {self._nome}\nSaldo R$ {self._saldo}"

    def __iter__(self):
        return self

    def __next__(self):
        if (self._idx == 0): 
            raise StopIteration
       
        self._idx -= 1
        ret = self._historico[self._idx]
        return ret  

