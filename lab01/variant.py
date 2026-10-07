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