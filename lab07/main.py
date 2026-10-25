from functions import sum_digits, average, normalize_text, select_numbers


def main():
    number = int(input("Введите целое число: "))
    print("Сумма цифр:", sum_digits(number))

    line = input("Введите числа через пробел: ")
    numbers = [int(x) for x in line.split()]
    avg = average(numbers)
    if avg is None:
        print("Среднее: Нет данных")
    else:
        print("Среднее:", avg)

    text = input("Введите произвольный текст: ")
    print("Нормализованный текст:", repr(normalize_text(text)))


    threshold = int(input("Введите порог (целое неотрицательное): "))
    while threshold < 0:
        threshold = int(input("Порог должен быть >= 0, повторите: "))
    print("Числа не больше порога:", select_numbers(numbers, threshold))


if __name__ == "__main__":
    main()