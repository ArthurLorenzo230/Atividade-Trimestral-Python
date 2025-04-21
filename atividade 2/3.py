num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f"A soma de {num1} e {num2} é {num1 + num2}")
print(f"A subtração de {num1} por {num2} é {num1 - num2}")
print(f"A multiplicação de {num1} e {num2} é {num1 * num2}")

if num2 == 0:
    print("Não é possível dividir por zero.")
else:
    print(f"A divisão de {num1} por {num2} é {num1 / num2}")
