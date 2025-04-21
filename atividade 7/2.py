def main():
    convidados = []
    num_convidados = int(input("Quantos convidados deseja adicionar? "))

    for i in range(1, num_convidados + 1):
        nome = input(f"Digite o nome do convidado {i}: ")
        convidados.append(nome)


# ╱╭━━┳━┳━┳╮ NADA AQUI!
# ━┫╱┓┣┳━━━╯
# ╱╱╱┃┃╯
# ━┫╱╰┛╯
# ╱╰━━━╯


    lista_final = sorted(set(convidados))

    print("\nLista final de convidados (sem duplicatas e ordenada):")
    print(lista_final)

if __name__ == "__main__":
    main()
