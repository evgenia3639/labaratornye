# profile.py

surname = input ('Фамилия:')
name = input ('имя: ')
group = input ('группа: ')
city = input ('город: ')
age = int (input ('возраст от 1 до 120: '))
sudject = input ('предмет: ')
weekly_hours = float (input (' колличество часов: ' ))
fullname = name + surname
future_age = age + 4
four_weeks_hours = weekly_hours * 4
daily_hours = weekly_hours / 7
print ('Учебная карточка')
print (f'Имя: {fullname}')
print (f'Возраст через четыре года: {future_age}')
print (f'За цетыре недели: {four_weeks_hours: 2f}ч')
print (f'В среднем в день: {daily_hours: 2f}ч')

#workload.py

subject1 = input("Введите название первого предмета: ")
count1 = int(input(f"Введите количество занятий по предмету «{subject1}» за неделю: "))
prod1 = int(input(f"Введите продолжительность одного занятия по предмету «{subject1}» в минутах: "))

subject2 = input("Введите название второго предмета: ")
count2 = int(input(f"Введите количество занятий по предмету «{subject2}» за неделю: "))
prod2 = int(input(f"Введите продолжительность одного занятия по предмету «{subject2}» в минутах: "))

minutes1 = count1 * prod1
minutes2 = count2 * prod2
full_minutes = minutes1 + minutes2
full_hours = full_minutes / 60

dostyp_hours = float(input("Введите доступное время на неделю в часах: "))
free_hours = dostyp_hours - full_hours

print(f"{subject1}: {minutes1} мин")
print(f"{subject2}: {minutes2} мин")
print(f"Общая нагрузка: {full_minutes} мин = {full_hours:.2f} ч")
print(f"Остаток свободного времени: {free_hours:.2f} ч")
print(f"Нагрузка за 4 недели: {full_minutes * 4} мин = {full_hours * 4:.2f} ч")

#debug.py
#Фрагмент А
first = '2'
second = '3'
print('Сумма чисел:', int(first) + int(second))

#Фрагмент Б
age = int(input('Возраст: '))
print('Возраст через год:', age + 1)

#Фрагмент В
first = 4
second = 7
third = 10
sred = (first + second + third) / 3
print('Среднее из трех чисел:', sred)


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

#variant5.py

# variant.py — расчёт заказа из двух позиций

#Спортивный магазин
zakaz_name = input("Название заказа: ")
zakazhic_name = input("Имя заказчика: ")

#Первая позиция
name_1 = input("Мячи: ")
count_1 = int(input(f"Количество «{name_1}»: "))
one_zena = float(input(f"Цена единицы «{count_1}» в рублях: "))

#Вторая позиция
name_2 = input("Скакалки: ")
count_2 = int(input(f"Количество «{name_2}»: "))
one_zena_2 = float(input(f"Цена единицы «{count_2}» в рублях: "))

#Доставка и внесённая сумма
dostavka = float(input("Стоимость доставки в рублях: "))
paid = float(input("Внесённая сумма в рублях не меньше стоимости обеих позиций с доставкой: "))

#Расчёты
cost_1 = count_1 * one_zena
cost_2 = count_2 * one_zena_2
bez_dostavki_cost = cost_1 + cost_2
total_cost = bez_dostavki_cost + dostavka
total_count = count_1 + count_2
sdacha = paid - total_cost

print("Заказ:", zakaz_name)
print("Заказчик:", zakazhic_name)
print(f"Название: {name_1} | Количество: {count_1} | Цена: {one_zena:.2f} | Стоимость: {cost_1:.2f}")
print(f"Название: {name_2} | Количество: {count_2} | Цена: {one_zena_2:.2f} | Стоимость: {cost_2:.2f}")
print(f"Стоимость товаров без доставки: {bez_dostavki_cost:.2f} руб.")
print(f"Стоимость доставки: {dostavka:.2f} руб.")
print(f"Итоговая сумма с доставкой: {total_cost:.2f} руб.")
print(f"Общее количество единиц: {total_count}")
print(f"Сдача: {sdacha:.2f} руб.")