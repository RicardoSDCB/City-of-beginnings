def calculador(number, number2, operation):
    if operation == "+":
        results.append(number+number2)
        return results[-1]
    elif operation == "-":
        results.append(number - number2)
        return results[-1]
    elif operation == "/":
        results.append(number / number2)
        return results[-1]
    elif operation == "*":
        results.append(number * number2)
        return results[-1]


def continue_calculating(number, operation):
    if operation == "+":
        results.append(results[-1] + number)
        return results[-1]
    elif operation == "-":
        results.append(results[-1] - number)
        return results[-1]
    elif operation == "/":
        results.append(results[-1] / number)
        return results[-1]
    elif operation == "*":
        results.append(results[-1] * number)
        return results[-1]


if __name__ == "__main__":
    keep = True
    primeiro = True
    results = [0]

    if primeiro:
        num = float(input("Type the number for the operation: \n"))
        operacao = input("Type the operation do you want: (+ - / *)\n ")
        num2 = float(input("Type the other number for the operation: \n"))

        resultado = calculador(num, num2, operacao)

        print(f"The result of your operation is: {resultado}")

        primeiro = False

        continuar = input("Do you want to continue the operation? (yes or no) \n")
        if continuar != "yes":
            keep = False

    while keep:
        num = float(input("Type the number for the operation: \n"))
        operacao = input("Type the operation do you want: (+ - / *)\n ")

        resultado = continue_calculating(num, operacao)
        print(f"The result of your operation is: {resultado}")

        continuar = input("Do you want to continue? (yes or no)\n")
        if continuar != "yes":
            keep = False

    print(f"\n\nThank you for using this calculator program.")
