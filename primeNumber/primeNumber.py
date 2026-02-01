def prime_number(n):
    if n <= 1:
        print("O valor indicado é menor ou igual a 1, ou seja, não possui um número primo válido.")
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print(f"{n} não é um número primo pois ele também é divisível por {i}.")
            return False

    print(f"{n} é um número primo pois só é divisível por 1 e por ele mesmo.")
    return True


if __name__ == "__main__":
    prime_number(15)
