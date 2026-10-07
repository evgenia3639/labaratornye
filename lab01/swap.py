#swap.py
first_class = input("Название первой аудитории: ")
second_class = input("Название второй аудитории: ")

print("Исходные значения:")
print("Название первой аудитории:", first_class)
print("Название второй аудитории:", second_class)

# Обмен
obmen = first_class
first_room = second_class
second_room = obmen

print("После обмена:")
print("Название первой аудитории:", first_room)
print("Название второй аудитории:", second_room)