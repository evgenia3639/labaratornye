#variant5.py

n = int(input("Введите целое число от 0 до 100: "))

if n < 0 or n > 100:
    print("Ошибка диапазона")
elif n <= 24:
    print("Мало")
elif n >= 25 and n <= 74:
    print("Достаточно")
elif n >= 75:
    print("Много")