menu = """"

[d] Depositar
[s] Sacar
[e] Extarto
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
        valor = float(input("Infore o valor a ser depositado:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}/n"

        else:
            print("Erro na operação! o valor informado é invalido.")    

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Erro na operação! Você não tem saldo sufuciente.")

        elif excedeu_limite:
            print("Erro na operação! O valor de saque excede o limite.")

        elif excedeu_saques:
            print("Erro na operação! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}/n"
            numero_saques +=1    

        else:
            print("Erro na operação! O valor informado é inválido.")