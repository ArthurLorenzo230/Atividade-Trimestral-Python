valor = input("Digite um número inteiro: ")

if valor.isdigit() or (valor.startswith('-') and valor[1:].isdigit()):
    numero = int(valor)
    print(numero % 2 == 0)
else:
    print("Valor inválido. Por favor, insira um número inteiro.")
