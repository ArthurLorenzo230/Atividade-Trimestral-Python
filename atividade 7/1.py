def main():
    notas = []

    for i in range(1, 6):
        nota = float(input(f"Digite a nota do aluno {i}: "))
        notas.append(nota)

    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(notas) / len(notas)

    print("\nResultados:")
    print(f"Maior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")
    print(f"Média das notas: {media:.1f}")

if __name__ == "__main__":
    main()
