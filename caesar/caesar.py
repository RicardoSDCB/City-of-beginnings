alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar_cypher(texto, avancar, codificar):
    posicoes = []

    for letra in texto:
        if letra in alphabet:
            posicao = alphabet.index(letra)
            posicoes.append(posicao)
        else:
            posicoes.append(letra)

    if codificar == "encrypt":
        for valor in posicoes:
            if isinstance(valor, int):
                print(alphabet[(valor+avancar) % 26], end="")
            else:
                print(valor, end="")
    elif codificar == "decode":
        for valor in posicoes:
            if isinstance(valor, int):
                print(alphabet[(valor-avancar) % 26], end="")
            else:
                print(valor, end="")


if __name__ == "__main__":
    keep = True
    while keep:
        encode = input("Type\"encrypt\" or \"decode\" to chose one: \n").lower()
        text = input("Type the text you want to modify: \n").lower()
        shift = int(input("Type the shift amount you want: \n"))

        caesar_cypher(text, shift, encode)

        validator = input("\n\nDo you want to continue? (yes or no)").lower()
        if validator != "yes":
            print("Thank you for using our decrypter.")
            keep = False
