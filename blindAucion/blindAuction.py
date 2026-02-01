def auction(name, value):
    buyers[name] = value


if __name__ == "__main__":
    buyers = {}
    keep = True
    count = 1

    while keep:
        # clear_screen()
        nome = input("Type your name here, please:\n")
        valor = float(input("Type your bid:\nR$"))

        auction(nome, valor)

        keep = input("Has anyone else to make a bid? (yes or no)\n")
        if keep != "yes":
            keep = False

    for key in buyers:
        print(f"{count}º buyer:")
        print(f"{key} who placed the bid of {buyers[key]}")
        count = count + 1

    print("="*40)
    maior_valor = max(buyers.values())
    nome_maior = max(buyers, key=buyers.get)
    print(f"The winner was {nome_maior} with the bid of R${maior_valor:.2f}.")
