idade = input("Informe sua idade: ")

if idade.isdigit():
    idade = int(idade)
    if idade < 0:
        print("Valor informado é inválido.")
    elif idade < 18:
        print("Você é menor de idade.")
    elif idade < 60:
        print("Você é adulto.")
    else:
        print("Você é idoso.")
else:
    print("Valor informado é inválido.")
