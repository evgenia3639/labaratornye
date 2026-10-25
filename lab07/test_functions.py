from functions import average, normalize_text, sum_digits, select_numbers

# Базовые проверки
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

# Дробное среднее — сравнение с допуском
assert abs(average([1, 2]) - 1.5) < 1e-9

# --- Индивидуальный вариант: select_numbers(numbers, threshold) ---
# Условие: не больше порога, т.е. value <= threshold

# Контрольный пример из задания: [-5, 0, 2, 5], порог 2 -> [-5, 0]
assert select_numbers([-5, 0, 2, 5], 2) == [-5, 0]

# Пустой список
assert select_numbers([], 5) == []

# Граница: значение, равное порогу, включается (<=)
assert select_numbers([1, 2, 3], 2) == [1, 2]
# Рядом с границей
assert select_numbers([1, 2, 3], 1) == [1]
assert select_numbers([3, 4], 2) == []
assert select_numbers([2, 2, 3], 2) == [2, 2]

# Повторы подходящего значения сохраняются
assert select_numbers([1, 1, 5, 1], 1) == [1, 1, 1]

# Исходный список не изменяется
original = [-5, 0, 2, 5]
saved = original[:]
select_numbers(original, 2)
assert original == saved

# Порог 0: подходят только значения <= 0
assert select_numbers([-1, 0, 1], 0) == [-1, 0]

print("Базовые проверки пройдены")