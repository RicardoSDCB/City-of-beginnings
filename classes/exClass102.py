def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 != 0:
                return False
            return True
        return True


def days_in_month(year, month):
    if is_leap(year):
        leap_month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return leap_month_days[month-1]
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[month-1]


if __name__ == "__main__":
    ano = int(input("What year do you want to know if it is a leap or not leap year: \n"))
    mes = int(input("Type the month you wanna know the days: \n"))
    days = days_in_month(ano, mes)

    print(f"The month you want to know, has {days} days.")
