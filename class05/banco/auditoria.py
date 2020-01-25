'''
    Classe Auditoria
'''
import time;
class Auditoria:
    def __init__(self):
        self.__lista_auditoria = []

    def auditar(self, cpf, tipo, valor):
        self.__lista_auditoria.append({
            'cpf': cpf,
            'tipo': tipo,
            'valor': valor,
            'data': time.time()
        })

    def listar_auditoria(self, cpf = ''):
        
        if (cpf == ''):
            return self.__lista_auditoria

        retorno = []
        for a in self.__lista_auditoria:
            if (a['cpf'] == cpf):
                retorno.append(a)
        return retorno
    

    def __str__(self):
        '''
        Imprime o registro de auditoria
        Parameters:
        -
        Returns: 
        string: dados da conta
        '''
        retorno = ''
        for a in self.__lista_auditoria:
            retorno += f"CPF: {self.__cpf}\n Data/Hora: {self.__data_hora}\n Valor R$ {self.__valor}\n Tipo {self.__tipo}"
        
        return retorno