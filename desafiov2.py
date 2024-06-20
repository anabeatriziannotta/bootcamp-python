def ver_menu():

    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [q] Sair

    => """

    return input(menu)

def depositar (saldo, valor, extrato, /):

    if valor > 0: 
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, numero_saques,limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = int(numero_saques >= limite_saques)
    
    if excedeu_saldo:
        print ("Operação falhou! Você não possui saldo suficiente.")

    elif excedeu_limite:
        print ("Operação falhou! Você execeu o valor limite do saque.")

    elif excedeu_saques:
        print ("Operação falhou! Você atingiu a sua cota de saques diários.")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def ver_extrato (saldo, /, *, extrato):

    print("================================================")
    print("\n")
    print("EXTRATO BANCÁRIO")
    print("\n")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print("\n")
    print(f"SALDO ATUAL: R$ {saldo:.2f}")
    print("\n")
    print("================================================")

def cadastrar_usuario (usuarios, /):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado)")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco })
    print("Usuário cadastrado com sucesso!")

def filtrar_usuario (cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta (agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:

        opcao = ver_menu()

        if opcao == "d":
            valor = float(input("Insira o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor, extrato)
    
        elif opcao == "s":
            valor = float(input("Insira o valor a ser debitado: "))
            saldo, extrato, numero_saques = sacar(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)

        elif opcao == "e":
            ver_extrato (saldo, extrato = extrato)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "nu":
            cadastrar_usuario(usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()