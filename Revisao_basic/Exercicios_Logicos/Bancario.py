menu =  """ 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
extrato = ""
limite = 500

numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação Falhou! Valor Invalido")

    elif opcao == "s":
        valor = float(input("Informe o valor do Saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saque:
            print("Saque exedido")
        
        elif excedeu_limite:
            print("Limite Exedido")
        
        elif excedeu_saque:
            print("Limite de Saques Exedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
        else:
            print("Operação de falhou !")

    elif opcao == "e":
        print('\n==================Extrato==================')
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, Gentileza selecionar a opção desejada.")

#
