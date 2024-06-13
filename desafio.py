menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Insira o valor a ser depositado: "))

        if valor > 0: 
            saldo += valor
            extrato += f"Foi depositado o valor de R$ {valor:.2f}\n"
    
    elif opcao == "s":
        valor = float(input("Insira o valor a ser debitado: "))

        if valor <= saldo and valor <= limite and numero_saques < LIMITE_SAQUES:
            saldo -= valor
            numero_saques += 1
            extrato += f"Foi debitado o valor de R$ {valor:.2f}\n"

        elif valor > saldo:
            print ("Operação falhou! Você não possui saldo suficiente.")

        elif valor > limite:
            print ("Operação falhou! Você execeu o valor limite do saque.")
        
        elif numero_saques >= LIMITE_SAQUES:
            print ("Operação falhou! Você atingiu a sua cota de saques diários.")

    elif opcao == "e":
        print("================================================")
        print("\n")
        print("EXTRATO BANCÁRIO")
        print("\n")
        print(extrato)
        print("\n")
        print(f"SALDO ATUAL: R$ {saldo:.2f}")
        print("\n")
        print("================================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

