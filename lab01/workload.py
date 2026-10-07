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