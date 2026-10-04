# minimum.py
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

if a <= b and a <= c:
    minimum = a
elif b <= a and b <= c:
    minimum = b
else:
    minimum = c

print("Минимальное число:", minimum)

# calculator.py

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
op = input("Введите операцию (+, -, *, /): ").strip()

if op == '+':
    result = a + b
    print(f"{result:.2f}")
elif op == '-':
    result = a - b
    print(f"{result:.2f}")
elif op == '*':
    result = a * b
    print(f"{result:.2f}")
elif op == '/':
    if b == 0:
        print("Деление на ноль запрещено")
    else:
        result = a / b
        print(f"{result:.2f}")
else:
    print("Неизвестная операция")

# point.py

x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

if 0 <= x <= 5 and 0 <= y <= 3:
    print("Внутри или на границе")
else:
    print("Снаружи")

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