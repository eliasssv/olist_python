from correntista import Correntista

lista_correntista = []

def hr():
    '''
    Imprime uma linha tracejada
    '''
    print("---------------------------------")

def menu_inicial():
    '''
    Imprime o menu inicial
    '''
    opcao = None
    while opcao != '0' :
        hr()
        print("Opções iniciais:")
        print("1 - Cadastrar Correntista")
        print("2 - Selecionar Correntista")
        print("3 - Listar Correntistas")
        print("4 - Auditar Correntistas")
        print("0 - Sair")
        hr()
        opcao = input("Informe a opção: ")
        if opcao == '1':
            cadastrar_correntista()
        elif opcao == '2':
            selecionar_correntista()
        elif opcao == '3':
            listar_correntistas()
        elif opcao == '4':
            auditar_correntistas()
        elif opcao == '0':
            print("Saiu do sistema!") 
        else:
            print("Opção Inválida!")     

def listar_correntistas():
    '''
    Lista todos os correntistas cadastrados
    '''
    print("Contas Cadastradas:")
    for c in lista_correntista:
        print(c)
        hr()

def cadastrar_correntista():
    '''
    Cadastra um correntista
    '''
    hr()
    nome = input("Informe o nome do correntista:")
    cpf = input("Informe o CPF do correntista:")
    saldoInicial = float(input("Informe o Saldo Inicial do correntista:"))

    existe = False
    for c in lista_correntista:
        if c.cpf() == cpf:
            existe = True

    if existe:
        print(f"CPF: {cpf} já cadastrado!")
    else:
        lista_correntista.append(Correntista(nome, cpf, saldoInicial))
        print("Correntista cadastrado com sucesso!")

def selecionar_correntista():
    '''
    Seleciona um correntista
    '''
    hr()
    listar_correntistas()
    nome = input("Informe o Nome do correntista a ser selecionado:")
    existe = False
    for c in lista_correntista:
        if c.nome() == nome:
            menu_correntista(c)
            existe = True

    if existe == False:
        print("Correntista não encontrado!")

def auditar_correntistas():
    listar_correntistas()
    cpf = input("Informe o CPF do correntista a ser auditado:")
    existe = False
    for c in lista_correntista:
        if c.cpf() == cpf:
            for a in c.auditoria():
                print(a)
            existe = True

    if existe == False:
        print("Correntista não encontrado!")

def menu_correntista(correntista):
    '''
    Imprime o menu do correntista
    '''
    opcao = None
    while opcao != '0' :
        hr()
        print(correntista)
        hr()
        print("1 - Fazer depósito")
        print("2 - Fazer saque")
        print("3 - Ver histórico")
        print("0 - Sair")

        opcao = input("Informe a opção: ")
        if (opcao == '1'):
            print(correntista.depositar(float(input("Informe o valor do depósito: "))))
        elif (opcao == '2'):
            print(correntista.sacar(float(input("Informe o valor do saque: "))))   
        elif (opcao == '3'):
            for hist in correntista:
                print(hist)

if __name__ == "__main__":
    menu_inicial()