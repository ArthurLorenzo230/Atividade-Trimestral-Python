operacao = input("Qual operação deseja fazer? (soma, subtração, multiplicação, divisão): ").lower()

if operacao in ["soma", "subtração", "multiplicação", "divisão"]:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if operacao == "soma":
        print(n1 + n2)
    elif operacao == "subtração":
        print(n1 - n2)
    elif operacao == "multiplicação":
        print(n1 * n2)
    elif operacao == "divisão":
        if n2 == 0:
            print("Não é possível dividir por zero.")
        else:
            print(n1 / n2)
else:
    print("Operação inválida.")
